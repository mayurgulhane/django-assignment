# views.py
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings
import random


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        otp = ''.join(random.choices('0123456789', k=6))

        user.otp_secret_key = otp
        user.save()

        send_otp_email(user.email, otp)

        return Response({'message': f'OTP sent successfully to {user.email}. Please check your email to verify your account.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_otp_email(email, otp):
    subject = 'OTP for account verification'
    message = f'OTP for account verification is: {otp}\n\nPlease use this OTP to verify your account. Thank you.'
    from_email = settings.EMAIL_HOST_USER  
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)




@api_view(['POST'])
def verify(request):
    email_or_username = request.data.get('email_or_username')
    otp = request.data.get('otp')

    try:
        if '@' in email_or_username:
            user = User.objects.get(email=email_or_username, otp_secret_key=otp)
        else:
            user = User.objects.get(username=email_or_username, otp_secret_key=otp)

        if user:
            user.is_active = True
            user.save()

            login_url = 'http://127.0.0.1:8000/users/login_view/'  
            return Response({'message': 'Verification successful. Your account has been activated.', 'login_url': login_url}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def login_view(request):
    email_or_username = request.data.get('email_or_username')
    otp = request.data.get('otp')

    try:
        if '@' in email_or_username:
            user = User.objects.get(email=email_or_username)
        else:
            user = User.objects.get(username=email_or_username)

        if user and user.otp_secret_key == otp:
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)

            user_details = serializer.data
            user_details['refresh'] = str(refresh)
            user_details['access'] = str(refresh.access_token)

            return Response(user_details, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['POST'])
def forgot_password(request):
    email_or_username = request.data.get('email_or_username')
    password = request.data.get('password')
    try:
        if '@' in email_or_username:
            user = User.objects.get(email=email_or_username)
        else:
            user = User.objects.get(username=email_or_username)

        if user:
            user.set_password(password)
            user.save()

            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['POST'])
def reset_password(request):
    email_or_username = request.data.get('email_or_username')
    otp = request.data.get('otp')
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    try:
        if '@' in email_or_username:
            user = User.objects.get(email=email_or_username)
        else:
            user = User.objects.get(username=email_or_username)

        if user and user.otp_secret_key == otp:
            if not user.check_password(old_password):
                return Response({'error': 'Invalid old password'}, status=status.HTTP_401_UNAUTHORIZED)

            user.set_password(new_password)
            user.save()

            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

