from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import mysql.connector
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import bcrypt
from .models import Usuario


# Create your views here.

def Vlogin (request): # template
    return render(request, "Maqueta/login.html")

def VloginAdmin (request): # template
    return render(request, "Maqueta/loginAdmin.html")

def VistaUsuario (request): # template
    return render(request, "Maqueta/formVentas.html")

def RegistroUsuario (request):
    return render(request, "Maqueta/RegistroUsuario.html")

def registrar_usuario(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST['nombre']
        contrasena = request.POST['contrasena']

        # Conectar con la base de datos
        conexion = mysql.connector.connect(user='root', password='Wizard2023.', database='tapizados')
        cursor = conexion.cursor()

        # Insertar los datos del usuario en la tabla correspondiente
        consulta = "INSERT INTO aplicaciontapizados_usuario (Usuario, Clave) VALUES (%s, %s)"
        valores = (nombre, make_password(contrasena))
        cursor.execute(consulta, valores)

        # Guardar los cambios y cerrar la conexión
        conexion.commit()
        conexion.close()

        # Redireccionar al usuario a otra página
        messages.success(request, 'Usuario registrado correctamente.')
        return render(request, 'Maqueta/formVentas.html')
    else:
        # Si el método de solicitud no es POST, mostrar el formulario
        return render(request, 'Maqueta/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'].encode('utf-8')
        try:
            user = Usuario.objects.get(Usuario=username)
        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe')
            return redirect('login')
        if bcrypt.checkpw(password, user.Clave.encode('utf-8')):
            request.session['user_id'] = user.id
            messages.success(request, '¡Bienvenido de nuevo!')
            return redirect('index')
        else:
            messages.error(request, 'Contraseña incorrecta')
            return redirect('login')
    return render(request, 'login.html')

def VistaAdmin (request): # template
    return render(request, "Maqueta/rUsuario.html")

def Visualizar (request): # template
    return render(request, "Maqueta/Visualizar.html")

def Dash (request): # template
    return render(request, "Maqueta/dash.html")

def rUsuario (request): # template
    return render(request, "Maqueta/rUsuario.html")

def PVend (request): # template
    return render(request, "Maqueta/PVendedores.html")

def LOrdenes (request): # template
    return render(request, "Maqueta/LOrdenes.html")