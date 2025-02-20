from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(
                {'email': 'Email already exists'})

        return super().validate(attrs)

    # override create method
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)

        return user
