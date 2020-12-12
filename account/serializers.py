from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        label=_('Password'),
        style={'input_type': 'password'},
        write_only=True,
        required=True,
    )

    confirmPassword = serializers.CharField(
        label=_('Confirm Password'),
        style={'input_type': 'password'},
        write_only=True,
        required=True,
    )

    class Meta:

        model = Account
        fields = (
            'id',
            'name',
            'email',
            'password',
            'confirmPassword',
        )

    def create(self, validated_data):
        account = Account(
            email=self.validated_data['email'],
            name=self.validated_data['name'],
        )

        password = validated_data['password']
        confirmPassword = validated_data['confirmPassword']

        if password != confirmPassword:
            raise serializers.ValidationError(
                {'password': ['Os campos senha e confirmar senha não coincidem.']})

        account.set_password(password)
        account.save()

        return account


""" class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'name',
            'email',
        ]
 """


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _(
                    'Não foi possível efetuar login com credenciais fornecidas. Email e/ou senha inválidos')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Deve-se incluir "email" e "senha".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
