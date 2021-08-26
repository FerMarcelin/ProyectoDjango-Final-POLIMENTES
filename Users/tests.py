from django.test import TestCase
from ProyectoFinalPOLI.wsgi import *
from Users.models import User, ConnectionState

# Create your tests here.

# connection_type = ConnectionState.objects.create(state="offline")
# connection_type2 = ConnectionState.objects.create(state="inline")
"""
CREACIÓN DE 30 USUARIOS, con otros cuatro se hicieron las pruebas antes de llenar la DB

p1 = User.objects.create_user(name='Javier', last_name='Ibarra', email='javi@correo.com', phone='+5212345678',
                              password='tortas')
p2 = User.objects.create_user(name='Gabriel', last_name='Ayala', email='gabo@correo.com', phone='+5298765432',
                              password='tamales')
p3 = User.objects.create_user(name='Omar', last_name='Aldaco', email='omar@correo.com', phone='+5213467982',
                              password='chilaquiles')
p4 = User.objects.create_user(name='Alexis', last_name='Roldan', email='alexis@correo.com', phone='+5246197328',
                              password='molito')
p5 = User.objects.create_user(name='Raul', last_name='Gutierrez', email='raul@correo.com', phone='+525579841652',
                              password='fruta')
p6 = User.objects.create_user(name='Guillermo', last_name='Alvarado', email='guillermo@correo.com', phone='+5246917631',
                              password='papitas1234')
p7 = User.objects.create_user(name='Ruben', last_name='Sanchez', email='ruben@correo.com', phone='+5203129478',
                              password='chocolate')
p8 = User.objects.create_user(name='Arturo', last_name='Juarez', email='arturo@correo.com', phone='+5226341159',
                              password='palomitas')
p9 = User.objects.create_user(name='Israel', last_name='Contreras', email='israel@correo.com', phone='+5255448855',
                              password='mariscos')
p10 = User.objects.create_user(name='Axel', last_name='Tolentino', email='axel@correo.com', phone='+5211223344',
                               password='bolognesa')
p11 = User.objects.create_user(name='Francisco', last_name='Diaz', email='francisco@correo.com', phone='+5255669988',
                               password='sushito')
p12 = User.objects.create_user(name='Carlos', last_name='Lopez', email='carlos@correo.com', phone='+5277225544',
                               password='taquitos')
p13 = User.objects.create_user(name='Dante', last_name='Urrieta', email='dante@correo.com', phone='+5200664499',
                               password='lechugas')
p14 = User.objects.create_user(name='Eduardo', last_name='Juarez', email='eduardo@correo.com', phone='+5244330099',
                               password='espinacas')
p15 = User.objects.create_user(name='Jorge', last_name='Guarda', email='jorge@correo.com', phone='+5255112226',
                               password='zanahorias')
p16 = User.objects.create_user(name='Gustavo', last_name='Desentis', email='gustavo@correo.com', phone='+5255334956',
                               password='manzanas')
p17 = User.objects.create_user(name='Ricardo', last_name='Ramirez', email='ricardo@correo.com', phone='+5276854499',
                               password='elotes')
p18 = User.objects.create_user(name='Cesar', last_name='Murillo', email='cesar@correo.com', phone='+5277374462',
                               password='papasfritas')
p19 = User.objects.create_user(name='Isaac', last_name='Galicia', email='isaac@correo.com', phone='+5213080298',
                               password='papascurly')
p20 = User.objects.create_user(name='Santiago', last_name='Soliz', email='santiago@correo.com', phone='+5224647598',
                               password='pescado')
p21 = User.objects.create_user(name='Andres', last_name='Arriola', email='andres@correo.com', phone='+5230214597',
                               password='camarones')
p22 = User.objects.create_user(name='Rogelio', last_name='Ventura', email='rogelio@correo.com', phone='+5274102589',
                               password='pulpo')
p23 = User.objects.create_user(name='Sergio', last_name='Perez', email='sergio@correo.com', phone='+5255369852',
                               password='salchipulpos')
p24 = User.objects.create_user(name='Hector', last_name='Nuria', email='hector@correo.com', phone='+5285201697',
                               password='hamburguesas')
p25 = User.objects.create_user(name='Rodrigo', last_name='Martinez', email='rodrigo@correo.com', phone='+5216497532',
                               password='pastel')
p26 = User.objects.create_user(name='Luis', last_name='Mendez', email='luis@correo.com', phone='+5288441122',
                               password='helados567')
p27 = User.objects.create_user(name='Calu', last_name='Marcelin', email='calu@correo.com', phone='+52554595876',
                               password='helados567')
p28 = User.objects.create_user(name='Chris', last_name='Gil', email='chris@correo.com', phone='+52789564134',
                               password='enchiladas')       
p29 = User.objects.create_user(name='Fernanda', last_name='Marcelin', email='fer@correo.com', phone='+5256847968',
                               password='spaguetti')
p30 = User.objects.create_user(name='Daniel', last_name='Ramirez', email='dan@correo.com', phone='+5249783125',
                               password='tamales')                        
"""
