from rest_framework import serializers
from .models import User, Profile
from django.contrib.auth.password_validation import validate_password





# create the serializer for Register user
class RegisterSerializers(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)
    addres = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'role', 'phone', 'addres']
    
    def create(self, validated_data):
        phone = validated_data.pop('phone')
        addres = validated_data.pop('addres')
        password = validated_data.pop('password')

        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        Profile.objects.create(
            user = user,
            first_name="",
            last_name="",
            phone =phone,
            addres = addres,
        )

        return user
    


# create the serializer for change Password
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


# create Serializer for Reset Password
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    new_password = serializers.CharField(write_only=True)