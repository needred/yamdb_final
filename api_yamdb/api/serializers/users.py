from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role',)
        lookup_field = 'username'


class TokenSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True,
    )
    confirmation_code = serializers.UUIDField(
        required=True,
    )

    def validate(self, data):
        confirmation_code = data.get('confirmation_code')
        user = get_object_or_404(User, username=data.get('username'))
        if user.confirmation_code != confirmation_code:
            raise ValidationError('Неправильный confirmation code')
        token = RefreshToken.for_user(user)
        data['token'] = {
            'refresh': str(token),
            'access': str(token.access_token),
        }
        return data

    class Meta:
        model = User
        fields = ('email', 'confirmation_code')


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')

    def validate(self, attrs):
        if attrs.get('username') == 'me':
            raise ValidationError({'username': 'Username cannot be "me"'})
        return attrs
