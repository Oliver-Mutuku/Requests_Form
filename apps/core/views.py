from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.core.paginator import Paginator
from .serializers import RequestSerializer, ApprovalSerializer, ReadApprovalSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Request, Approval
import json


def form(request):
    context = {}
    return render(request, 'core/new_request.html', context)

class ApprovalViewset(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadApprovalSerializer
        else:
            return ApprovalSerializer

class RequestViewset(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


    def list(self, request, *args, **kwargs):
        status_filter = request.GET.get('status', '')
        search_query = request.GET.get('search', '')

        requests = self.get_queryset().order_by('-id')

        if status_filter and status_filter != 'all':
            requests = requests.filter(status=status_filter)

        if search_query:
            requests = requests.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(application__icontains=search_query)
            )

        paginator = Paginator(requests, 10)  # 10 requests per page
        page_number = request.GET.get('page', 1)
        paginated_requests = paginator.get_page(page_number)

        return render(request, 'core/list_requests.html', {'requests': paginated_requests})

    @action(detail=True, methods=['get'])
    def admin_view(self, request, pk=None):
        request_obj = self.get_object()
        return render(request, 'core/admin_request_detail.html', {'request': request_obj})

    @action(detail=True, methods=['post'])
    def process(self, request, pk=None):
        request_obj = self.get_object()

        data = json.loads(request.body)
        status_value = data.get('status')
        admin_notes = data.get('admin_notes')
        admin_signature = data.get('admin_signature')

        # Create an approval record
        approval_data = {
            'request': request_obj.id,
            'admin': request.user.id,  # Assuming user authentication is set up
            'status': status_value,
            'notes': admin_notes,
            'signature': admin_signature
        }

        serializer = ApprovalSerializer(data=approval_data)
        if serializer.is_valid():
            serializer.save()

            # Update the request status
            request_obj.status = status_value
            request_obj.save()

            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)