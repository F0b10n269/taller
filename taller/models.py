# Create your models here.
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Email')
    telefono = models.CharField(max_length=15, verbose_name='Telefono')
    direccion = models.CharField(max_length=200, blank=True, verbose_name='Direccion')
    saldo_pendiente = models.PositiveIntegerField(
        default=0,
        verbose_name='Saldo pendiente en pesos',
    )
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    class Meta:
        ordering = ['nombre']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return f'{self.nombre} ({self.email})'


class Reparacion(models.Model):
    TIPOS = [
        ('MOTOR', 'Motor'),
        ('FRENOS', 'Frenos'),
        ('ELECT', 'Electricidad'),
        ('NEUM', 'Neumaticos'),
        ('OTRO', 'Otro'),
    ]
    ESTADOS = [
        ('PEND', 'Pendiente'),
        ('PROC', 'En proceso'),
        ('LIST', 'Listo'),
    ]
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='reparaciones',
        verbose_name='Cliente',
    )
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    tipo = models.CharField(
        max_length=6, choices=TIPOS, default='OTRO', verbose_name='Tipo'
    )
    costo = models.PositiveIntegerField(verbose_name='Costo en pesos')
    estado = models.CharField(
        max_length=4, choices=ESTADOS, default='PEND', verbose_name='Estado'
    )
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name='Fecha ingreso')
    entregado = models.BooleanField(default=False, verbose_name='Entregado')

    class Meta:
        ordering = ['-fecha_ingreso']
        verbose_name = 'reparacion'
        verbose_name_plural = 'reparaciones'

    def __str__(self):
        return f'{self.descripcion} - {self.cliente.nombre}'