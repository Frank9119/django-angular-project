## rest framework
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Other import
from .serializers import RegisterSerializers, ChangePasswordSerializer, ResetPasswordSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

# Register View
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]


# Change Password View
class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.data.get('old_password')):
                return Response({
                    'Error': 'Wrong Password'}, status=400
                )

            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({
                'Message': 'Password Updated Succesfuly'}, status=200
            )
        return Response(serializer.errors, status=400)


# ResetPassword View
class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # validate data
        email = serializer.validated_data['email']
        new_password = serializer.validated_data['new_password']

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
        
        except User.DoesNotExist:
            return Response({'Error': "User Does Not Exist"}, status=404)


# Logout View
class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=205)
