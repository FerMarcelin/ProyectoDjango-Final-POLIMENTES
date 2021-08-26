"""
SERIALIZADORES
Aqui solo se hace la lógica de programación tal cual
"""
from rest_framework.serializers import *
from Users.models import User, ConnectionState


class UserSerializer(Serializer):
    name = CharField(allow_null=False)
    last_name = CharField(allow_null=False)
    email = EmailField(allow_null=False)
    password = CharField(allow_null=False)
    phone = CharField(allow_null=False)
    #state = IntegerField()  # porque sino indico lo contrario sera una persona fisica

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError({'status': "Correo invalido"})
        if User.objects.filter(phone=attrs['phone']).exists():
            raise ValidationError({'status': "Telefono invalido"})

        return attrs

    def create(self, validated_data):
        #validated_data.pop('state')
        return User.objects.create_user(**validated_data)

