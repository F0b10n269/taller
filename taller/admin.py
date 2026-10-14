# Register your models here.
from django.contrib import admin
from .models import Cliente, Reparacion


admin.site.site_header = "Administracion Taller Norte"
admin.site.site_title = "Taller Norte"
admin.site.index_title = "Gestion del taller"


class ReparacionInline(admin.TabularInline):
    model = Reparacion
    extra = 0
    fields = ('descripcion', 'tipo', 'costo', 'estado')
    show_change_link = True


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'saldo_formateado', 'creado')
    list_filter = ('creado',)
    search_fields = ('nombre', 'email', 'telefono')
    ordering = ('nombre',)
    readonly_fields = ('creado',)
    inlines = [ReparacionInline]

    @admin.display(description='Saldo pendiente', ordering='saldo_pendiente')
    def saldo_formateado(self, obj):
        return f"${obj.saldo_pendiente:,}".replace(",", ".")


@admin.register(Reparacion)
class ReparacionAdmin(admin.ModelAdmin):
    list_display = (
        'descripcion', 'cliente', 'tipo',
        'costo_formateado', 'estado', 'fecha_ingreso', 'entregado',
    )
    list_filter = ('tipo', 'estado', 'entregado', 'fecha_ingreso')
    search_fields = ('descripcion', 'cliente__nombre')
    ordering = ('-fecha_ingreso',)
    list_editable = ('estado', 'entregado')
    list_select_related = ('cliente',)
    readonly_fields = ('fecha_ingreso',)

    @admin.display(description='Costo', ordering='costo')
    def costo_formateado(self, obj):
        return f"${obj.costo:,}".replace(",", ".")