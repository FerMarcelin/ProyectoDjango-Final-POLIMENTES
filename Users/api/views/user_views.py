"""
VISTAS
Aquí va tal cual la ejecución de la lógica de programacion creada en los serializadores
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import \
    RetrieveAPIView, \
    ListAPIView, \
    CreateAPIView  # clase que se encanrga SOLO DE OBTENER adatos, por ejemplo la LISTAPIVIEW es solo de listas y así
from Users.models import User, ConnectionState
from Users.api.serializers.user_serializers import *

"""
VISTA 1
La siguiente vista crea a un usuario por el metodo POST con los datos
name, last_name, email, password y phone 
"""


class CreateUser(CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
VISTA 2
La siguiente vista permite a un usuario dado de alta ingresar al sistema
mediante su correo y validando su contraseña, una vez conectado su estado 
cambia a "online" (linea 50) 
"""


class Login(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, **kwargs):
        return User.objects.get(**kwargs)

    def retrieve(self, request, *args, **kwargs):
        email = request.query_params['email']
        pwd = request.query_params['password']
        user = self.get_queryset(email=email)
        raw_pass = user.check_password(pwd)
        connection = ConnectionState.objects.get(id=2)
        if raw_pass:
            # serializers = self.serializer_class(instance=user)
            user.state = connection
            user.save()
            print(user.state.state)
            return Response({'message': 'WELCOME!'}, status=status.HTTP_200_OK)
        return Response({'error': 'invalid password'}, status=status.HTTP_404_NOT_FOUND)


"""
VISTA 3
Por medio del correo del usuario consulto su estado, es decir si está
online u offline
"""


class Connected(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, **kwargs):
        return User.objects.get(**kwargs)

    def retrieve(self, request, *args, **kwargs):
        email = request.query_params['email']
        user = self.get_queryset(email=email)
        print(user.state.state)  # línea de código usada para debuguear
        if user.state.state == "inline":
            print(user.state.state)  # línea de código usada para debuguear
            return Response({'status': 'Online user'}, status=status.HTTP_200_OK)
        return Response({'status': 'Offline user'}, status=status.HTTP_404_NOT_FOUND)


"""
VISTA 4
Vista que mediante un RETRIEVE que proporciona el correo del usuario cambia
su estado a desconectado
"""


class Logout(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, **kwargs):
        return User.objects.get(**kwargs)

    def retrieve(self, request, *args, **kwargs):
        email = request.query_params['email']
        user = self.get_queryset(email=email)
        connection = ConnectionState.objects.get(id=1)
        user.state = connection
        print(user.state.state)
        user.save()
        return Response({'message': 'BYE, HAVE A NICE DAY!'}, status=status.HTTP_200_OK)


"""
VISTA 5
Vista que lista por nombre de usuario e email aquellos que se encuentran
conectados
"""


class ListConnectedUsers(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(state=2)

    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        list = [i.return_connected() for i in users]
        if len(list) > 0:
            return Response(list, status=status.HTTP_200_OK)
        return Response({'message': 'There´s nobody online'}, status=status.HTTP_404_NOT_FOUND)
