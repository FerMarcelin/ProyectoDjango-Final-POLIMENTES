from django.test import TestCase
from ProyectoFinalPOLI.wsgi import *
from Users.models import User, ConnectionState

# Create your tests here.

#connection_type = ConnectionState.objects.create(state="offline")
#connection_type2 = ConnectionState.objects.create(state="inline")

p1 = User.objects.create_user(name='Calu', last_name='Marcelin', email='calu@correo.com', phone='+52554595876', password='calu123')