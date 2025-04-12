from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import RequestSerializer, ApprovalSerializer, ReadApprovalSerializer
from .models import Request, Approval

class ApprovalViewset(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadApprovalSerializer
        else:
            return ApprovalSerializer

class RequestViewset(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    @action(detail=False, methods=['get'])
    def form(self, request):
        context = {}
        return render(request, 'core/new_request.html', context)

