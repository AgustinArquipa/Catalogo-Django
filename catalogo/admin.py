from django.contrib import admin
from django.utils.html import format_html
from catalogo.models import Autor, Genero, Idioma, Libro, Ejemplar

"""
Registro del superusuario:
username=agustin
correo=juanarquipa6675@gmail.com
password=arquipajuan777
"""

# Register your models here.
#admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Idioma)
#admin.site.register(Libro)
#admin.site.register(Ejemplar)

#Manera de mejorar el display del la interface de Administrador
class MyAutorAdmin(admin.ModelAdmin):
    list_display = ('fotxs', 'nombre', 'apellido', 'fechaNac')

    def fotxs(self, obj):
        return format_html('<img src={} widht="70" height="100" />', obj.foto.url)

class MyEjemplarAdmin(admin.ModelAdmin):
    list_display = ('id', 'libro')
    list_filter = ('estado', 'fechaDevolucion')

#class MyGeneroAdmin(admin.ModelAdmin):
 #   list_display = ('nombre')

#class MyIdiomaAdmin(admin.ModelAdmin):
 #   list_display = ('nombre')

class MyLibroAdmin(admin.ModelAdmin):
    list_display = ('foto', 'titulo', 'autor', 'isbn', 'muestra_genero')
    list_filter = ('idioma', 'genero')

    def foto(self, obj):
        return format_html('<img src={} width="70" height="100" />', obj.avatar.url)


#admin.site.register(Genero, MyGeneroAdmin)
#admin.site.register(Idioma, MyIdiomaAdmin)
admin.site.register(Autor, MyAutorAdmin)
admin.site.register(Ejemplar, MyEjemplarAdmin)
admin.site.register(Libro, MyLibroAdmin)