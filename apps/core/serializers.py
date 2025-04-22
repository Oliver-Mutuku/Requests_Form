from rest_framework import serializers
from .models import Request, Approval
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'


class ReadApprovalSerializer(serializers.ModelSerializer):
    admin = UserSerializer(read_only=True)
    request = RequestSerializer(read_only=True)

    class Meta:
        model = Approval
        fields = '__all__'