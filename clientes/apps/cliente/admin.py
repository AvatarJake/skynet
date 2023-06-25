from django.contrib import admin
from django.conf import settings

from .models import Cliente
from .utils import get_google_maps_client


# Register your models here.

# class ClienteAdmin(admin.ModelAdmin):
#     list_display=('id','nombres','apellidos','telefono','activo',)
#     list_display_links=('id','nombres','apellidos',)
#     list_filter=('id','nombres','apellidos','activo',)
#     search_fields=('id','nombres','apellidos','activo',)
#     list_per_page = 20

#     def inactivar(self, request, queryset):

#         for row in queryset.filter(activo=True):
#             self.log_change(request, row, 'inactivar cliente')
#         rows_updated = 0

#         for obj in queryset:
#             if obj.activo:
#                 obj.activo = False
#                 obj.save()

#                 rows_updated += 1

#         if rows_updated == 1:
#             message_bit = "1 cliente se marco"
#         else:
#             message_bit = "%s clientes se marcaron" % rows_updated
#         self.message_user(
#             request, "%s satisfactoriamente como inactivas" % message_bit)
#     inactivar.short_description = 'Inactivar cliente'

#     def activar(self, request, queryset):

#         for row in queryset.filter(activo=False):
#             self.log_change(request, row, 'activar cliente')
#         rows_updated = 0

#         for obj in queryset:
#             if not obj.activo:
#                 obj.activo = True
#                 obj.save()

#                 rows_updated += 1

#         if rows_updated == 1:
#             message_bit = "1 cliente se marco"
#         else:
#             message_bit = "%s clientes se marcaron" % rows_updated
#         self.message_user(
#             request, "%s satisfactoriamente como activos" % message_bit)
#     activar.short_description = 'Activar cliente'

#admin.site.register(Cliente,ClienteAdmin)
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombres', 'apellidos', 'email', 'telefono', 'direccion', 'fecha_union', 'activo',]
    list_filter = ['activo']
    search_fields = ['nombres', 'apellidos', 'email', 'telefono', 'direccion',]
    
    # fieldsets = (
    #     (None, {
    #         'fields': ('nombres', 'apellidos', 'email', 'telefono', 'direccion', 'fecha_union', 'activo', 'notas', 'name', 'latitude', 'longitude',)
    #     }),
    # )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                    'all': ('css/admin/location_picker.css',)
                }
            js = (
                    "https://maps.googleapis.com/maps/api/js?key={}".format(
                        settings.GOOGLE_MAPS_API_KEY),
                    'js/admin/location_picker.js'
                )
