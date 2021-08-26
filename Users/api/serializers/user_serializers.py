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

    # state = IntegerField()  #

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError({'status': "Correo invalido"})
        if User.objects.filter(phone=attrs['phone']).exists():
            raise ValidationError({'status': "Telefono invalido"})

        return attrs

    def create(self, validated_data):
        # validated_data.pop('state')
        return User.objects.create_user(**validated_data)


class CheckPasswordSerializer(Serializer):
    user = SerializerMethodField

    def get_user(self, obj: user, pwd: str):
        query_set = User.objects.get(email=obj.email)
        # print(obj.password)
        # print(pwd)
        raw_pass = obj.check_password(pwd)
        # print(raw_pass)
        connection = ConnectionState.objects.get(id=2)
        if raw_pass:
            obj.state = connection
            obj.save()
            # print(obj.state.state)
            return True
        return False


class CheckStateSerializer(Serializer):
    user = SerializerMethodField

    def get_user(self, obj: user):
        query_set = User.objects.get(email=obj.email)
        if obj.state.state == "inline":
            return True
        return False


class ChangeStateSerializer(Serializer):
    user = SerializerMethodField

    def get_user(self, obj: user):
        connection = ConnectionState.objects.get(id=1)
        before = obj.state
        obj.state = connection
        #print(user.state.state)
        obj.save()
        if before != obj.state:
            return True
        return False

