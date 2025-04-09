from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import RequestSerializer
from .models import Request

class RequestViewset(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    @action(detail=False, methods=['get'])
    def form(self, request):
        context = {}
        return render(request, 'index.html', context)

