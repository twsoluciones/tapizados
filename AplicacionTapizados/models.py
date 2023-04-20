from django.db import models
import bcrypt

class Usuario(models.Model):
    Usuario = models.CharField(max_length=30)
    Clave = models.CharField(max_length=30)

    def verificar_contraseña(self, contraseña):
        return bcrypt.checkpw(contraseña.encode('utf-8'), self.Contraseña.encode('utf-8'))

 

    class Meta:
        db_table = 'aplicaciontapizados_usuario'

class Administrador(models.Model):
    Usuario = models.CharField(max_length=30)
    Clave = models.CharField(max_length=30)

class Vendedor(models.Model):
    NombreVendedor = models.CharField(max_length=100)
    Rut = models.CharField(max_length=20)
    Local = models.CharField(max_length=100)
    FechaIngreso = models.DateTimeField()

class Cliente(models.Model):
    NombreCliente = models.CharField(max_length=100)
    Rut = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=100)
    Telefono = models.IntegerField()

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete= models.CASCADE)
    FechaPedido = models.DateTimeField()
    NumeroPedido = models.IntegerField()

class Producto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    TipoProducto = models.CharField(max_length=100)
    NombreTela = models.CharField(max_length=100)
    Color = models.CharField(max_length=100)
    CantidadTela = models.CharField(max_length=100)
    RellenoNuevo = models.CharField(max_length=10)
    CojinesRespaldo = models.IntegerField()
    CojinesAsiento = models.IntegerField()
    ValorEstimado = models.IntegerField()
    ValorFinal = models.IntegerField()

class BaseMueble(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    Estado = models.CharField(max_length=100)
    Material = models.CharField(max_length=100)
    TipoPatas = models.CharField(max_length=100)


class DetalleProducto(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    baseMueble = models.ForeignKey(BaseMueble, on_delete=models.CASCADE)
    NombreVendedor = models.CharField(max_length=100)
    NombreCliente = models.CharField(max_length=100)
    NumeroCliente = models.IntegerField()
    FechaPedido = models.DateTimeField()
    TipoProducto = models.CharField(max_length=100)
    NombreTela = models.CharField(max_length=100)
    Color = models.CharField(max_length=100)
    CantidadTela =models.CharField(max_length=100)
    RellenoNuevo = models.CharField(max_length=10)
    CojinesRespaldo = models.IntegerField()
    CojinesAsiento = models.IntegerField()
    Cantidad = models.IntegerField()
    Estado = models.CharField(max_length=100)
    Material = models.CharField(max_length=100)
    TipoPatas = models.CharField(max_length=100)
    ValorFinal=models.IntegerField()


    



    