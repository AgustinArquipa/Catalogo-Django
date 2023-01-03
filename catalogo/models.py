from django.db import models
from django.urls import reverse

import uuid #Requerida para la instancia de los libros unicos

# Create your models here.
class Genero(models.Model):
    """
    Modelo que representa un genereo literario
    """
    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del genero (xej.Programacion, BD, SO, etc)")

    def __str__(self) -> str:
        return self.nombre

class Idioma(models.Model):
    """
    Modelo que va a representar el idioma del libro
    """
    nombre = models.CharField(max_length=50, help_text="Ingrese un Idioma")

    def __str__(self) -> str:
        return self.nombre


class Autor(models.Model):
    """
    Modelo que representa un autor
    """ 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNac = models.DateField(null=True, blank=True)
    fechaDeceso = models.DateField('Fallecio', null=True, blank=True)

    foto = models.ImageField(upload_to='upload/', null=True)

    def get_absolute_urls(self):
        """
        Devuelve la url para acceder a ese autor
        """
        return reverse('AutorInfo', args=[str(self.id)])

    def __str__(self) -> str:
        return '%s, %s ' % (self.nombre, self.apellido)

    #def __str__(self) -> str:
     #   cad = str(self.nombre)+', '+str(self.apellido)
      #  cad += '\nFecha de Naciemiento: '+str(self.fechaNac)
       # return cad
    class Meta:
        ordering = ["apellido", "nombre"]

        def __str__(self) -> str:
            return '%s, %s' % (self.apellido, self.nombre)

class Libro(models.Model):
    """
    Modelo que representa a un libro (No Ejemplar)
    """
    avatar = models.ImageField('Foto', upload_to="photos", null=True, blank=True)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    #ForeingKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros
    resumen = models.TextField(max_length=1000, help_text='Ingrese un resumen del libro')

    isbn = models.CharField('ISBN', max_length=13, help_text='13 caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genero = models.ManyToManyField(Genero, help_text='Seleccione un genero (o varios) para el libro')
    #ManyToManyField, porque un genero puede contener muchos libros y un libro puede cubrir varios generos 

    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True)

    def muestra_genero(self) -> str:
        return ', '.join([genero.nombre for genero in self.genero.all()[:3]])

    #def get_image(self):
     #   return format_html('<img src={} />', self.avatar.url)

    def get_absolute_url(self):
        return reverse('LibroInfo', args=[str(self.id)])
    
    def __str__(self) -> str:
        return self.titulo

class Ejemplar(models.Model):
    """
    Modelo que representa un ejemplar de un libro
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID unico para este libro particular en toda la biblioteca')

    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
    
    fechaDevolucion=models.DateField(null=True, blank=True)

    ESTADO_EJEMPLAR = (
        ('m', 'en Mantenimiento'),
        ('p', 'Prestado'),
        ('d', 'Disponible'),
        ('r', 'Reservado'),
    ) 
        
    estado = models.CharField(max_length=1, choices=ESTADO_EJEMPLAR, blank=True, default='d', help_text='Disponibilidad del ejemplar')

    class Meta:
        ordering = ["fechaDevolucion"]

    def __str__(self) -> str:
        return '%s (%s)' % (self.id, self.libro.titulo)

    def tituloEstado(self):
        return '(%s)' % (self.get_estado_display())