from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from .serializers import RegisterSerializer

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        if User.objects.filter(email=data['email']).exists():
            raise ValidationError({'email': 'Email already registered'})
        if User.objects.filter(phone=data['phone']).exists():
            raise ValidationError({'phone': 'Phone number already registered'})

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
