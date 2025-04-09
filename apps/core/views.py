from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RequestSerializer
from .models import Request


class RequestViewset(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

