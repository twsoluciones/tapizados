from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import mysql.connector


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
        conexion = mysql.connector.connect(user='root', password='123456', database='tapizados')
        cursor = conexion.cursor()

        # Insertar los datos del usuario en la tabla correspondiente
        consulta = "INSERT INTO aplicaciontapizados_usuario (Usuario, Clave) VALUES (%s, %s)"
        valores = (nombre, contrasena)
        cursor.execute(consulta, valores)

        # Guardar los cambios y cerrar la conexión
        conexion.commit()
        conexion.close()

        # Redireccionar al usuario a otra página
        return render(request, 'Maqueta/formVentas.html')
    else:
        # Si el método de solicitud no es POST, mostrar el formulario
        return render(request, 'Maqueta/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bienvenida')
        else:
            error_message = 'El usuario o la contraseña son incorrectos.'
            return render(request, 'Maqueta/login.html', {'error_message': error_message})
    else:
        return render(request, 'Maqueta/formVentas.html')

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