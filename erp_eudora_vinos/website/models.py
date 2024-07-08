from django.db import models
# aqui se crean los modelos de la base de datos
# a través de clases que heredan de models.Model

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    comuna = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero_de_casa = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Producto(models.Model):
    SKU = models.CharField(primary_key=True, max_length=50, unique=True)
    tipo_producto = models.CharField(max_length=50)
    cepa= models.CharField(max_length=50, null=True)
    cosecha = models.CharField(max_length=50, null=True)
    nombre_producto = models.CharField(max_length=50, null=True)
    viña= models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.SKU    

class Ventas(models.Model):
    pedido = models.CharField(primary_key=True ,unique=True, max_length=50, default='0')
    comprador = models.CharField(max_length=50,null=True)
    venta_total = models.IntegerField(null=True)
    flete = models.IntegerField(null=True)
    fecha_boleta = models.DateField(null=True)
    pago = models.IntegerField(null=True)
    def __str__(self):
        return self.pedido
    
      
class Proveedores(models.Model):
    nombre_prov = models.CharField(primary_key=True, unique=True, max_length=50)
    email_empresa = models.EmailField(null=True)
    telefono_empresa = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre_prov

class Inventario_Y_Stock(models.Model):

    id_inventario = models.AutoField(primary_key=True)
    SKU = models.ForeignKey(Producto, on_delete=models.CASCADE) # foreign key
    nombre_prov = models.ForeignKey(Proveedores, on_delete=models.CASCADE) # foreign key
    bodega = models.CharField(max_length=150)
    fecha_de_ingreso = models.DateField()
    cantidad = models.IntegerField() # es el ingreso
    salidas = models.IntegerField()
    mov_bodegas = models.IntegerField()
    stock = models.IntegerField() # stock total
    precio_unitario = models.IntegerField()
    precio_total = models.IntegerField()


    def str(self):
        return self.id_inventario
    
class Compra_proveedores(models.Model):
    OC = models.IntegerField(primary_key=True, unique=True)
    nombre_prov = models.ForeignKey(Proveedores, on_delete=models.CASCADE) #foreign 
    fecha_oc = models.DateField()
    SKU = models.ForeignKey(Producto, on_delete=models.CASCADE) #foreign
    cantidad = models.IntegerField()
    numero_factura = models.IntegerField()
    fecha_factura = models.DateField(null=True)
    status = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    fecha_pago = models.DateField(null=True, blank=True)
    costo_unitario = models.IntegerField(null=True)

    def __str__(self):
        return str(self.OC)

class Informes(models.Model):
    fecha_informe =models.DateField()
    cantidad_ventas = models.IntegerField()
    transacciones = models.IntegerField()
    cantidad_miembros = models.IntegerField()
    ingresos_ventas = models.IntegerField()
    gastos_ventas = models.IntegerField()
    gastos_no_ventas = models.IntegerField()
    
    def __str__(self):
        return self.fecha_informe

class Alerta_stock(models.Model):
    id_inventario=models.ForeignKey(Inventario_Y_Stock, on_delete=models.CASCADE, default='0')
    fecha_alerta = models.DateField()
    cantidad = models.IntegerField(default='0')
      # Corregido: No necesitas una relación ForeignKey aquí

    def __str__(self):
        return str(self.id_inventario.id) + ' ' + str(self.fecha_alerta) + ' ' + str(self.cantidad)

class Alerta_vencimiento(models.Model):
    OC = models.ForeignKey(Compra_proveedores, on_delete=models.CASCADE, default='0')
    fecha_alerta = models.DateField()
    status = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
      # Corregido: No necesitas una relación ForeignKey aquí

    def __str__(self):
        # Asumiendo que OC se refiere a un campo entero en Compra_proveedores, convertirlo a cadena
        return str(self.OC.id) + ' ' + str(self.fecha_alerta) + ' ' + str(self.fecha_vencimiento) + ' ' + self.status


