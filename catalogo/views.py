from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from catalogo.models import Genero, Idioma, Autor, Libro, Ejemplar
from django.http import Http404
from catalogo.forms import GeneroForm, AutorForm

# Create your views here.
def hello(request):
    return render(request, 'hello.html', {})

def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)

    if request.method == "POST":
        formulario = AutorForm(request.POST, request.FILES)
        if formulario.is_valid():
            autor.apellido = formulario.cleaned_data['apellido']
            autor.nombre = formulario.cleaned_data['nombre']
            autor.fechaNac = formulario.cleaned_data['fechaNac']
            autor.fechaDeceso = formulario.cleaned_data['fechaDeceso']
            autor.foto = formulario.cleaned_data['foto']
            autor.save()
            return redirect('autores')
    else:
        formulario = AutorForm(instance=autor)

    return render(request, 'autor_new.html', {'formulario':formulario})

def autor_new(request):
    if request.method == "POST":
        formulario = AutorForm(request.POST, request.FILES)
        if formulario.is_valid():
            autor = formulario.save(commit=False)
            autor.apellido = formulario.cleaned_data['apellido']
            autor.nombre = formulario.cleaned_data['nombre']
            autor.fechaNac = formulario.cleaned_data['fechaNac']
            autor.fechaDeceso = formulario.cleaned_data['fechaDeceso']
            autor.foto = formulario.cleaned_data['foto']
            autor.save()
        return redirect('autores')
    else:
        formulario = AutorForm()
    return render(request, 'autor_new.html', {'formulario':formulario})


#Creamos una clase para poder ver todos los autores
class AutoresListView(generic.ListView):
    model = Autor

    context_object_name = 'autores'

    queryset = Autor.objects.all()

    template_name = 'autores.html'

    def get_context_data(self, **kwargs):
        autores = Autor.objects.all()

        context = super(AutoresListView, self).get_context_data(**kwargs)
        context['autores'] = autores

        return context

class AutorDetailView(generic.DetailView):
    model = Autor
    template_name = 'autor.html'

    def autor_detail_view(request, pk):
        try: 
            autor = Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            raise Http404('Ooops! No existe el autor')

        return render(request, 'autor.html', {'autor':autor})

def genero_new(request):

    if request.method == "POST":
        formulario = GeneroForm(request.POST)
        if formulario.is_valid():
            genero = formulario.save(commit=False)
            genero.nombre = formulario.cleaned_data['nombre']
            genero.save()
            return redirect('generos')
    else:
        formulario = GeneroForm()

    context = {
        'formulario':formulario
    }

    return render(request, 'genero_new.html', context)

#Para actualizar genero mediante el formulario

def genero_update(request, pk):
    genero = get_object_or_404(Genero, pk=pk)

    if request.method == "POST":
        formulario = GeneroForm(request.POST, instance=genero)
        if formulario.is_valid():
            genero = formulario.save(commit=False)
            genero.nombre = formulario.cleaned_data['nombre']
            genero.save()
            return redirect('generos')
    else:
        formulario = GeneroForm(instance=genero)

    return render(request, 'genero_new.html', {'formulario':formulario})


def index(request):
    nroGenero = Genero.objects.all().count()
    nroIdiomas = Idioma.objects.all().count()

    nroLibros = Libro.objects.all().count()
    nroEjemplares = Ejemplar.objects.all().count()
    nroDisponibles = Ejemplar.objects.filter(estado__exact='d').count()

    nroAutores = Autor.objects.count() #El all() esta implicito por defecto

    context = {
        'nroGeneros':nroGenero,
        'nroIdiomas':nroIdiomas,
        'nroLibros':nroLibros,
        'nroEjemplares':nroEjemplares,
        'nroDisponibles':nroDisponibles,
        'nroAutores':nroAutores,
    }

    return render(request, 'index.html', context)

#Son clases que devuelven la lista de los datos cargados

class GeneroListView(generic.ListView):
    model = Genero
    
    context_object_name = 'generos'

    queryset = Genero.objects.all()

    template_name = 'genero.html'

    def get_context_data(self, **kwargs):
        generos = Genero.objects.all()

        context = super(GeneroListView, self).get_context_data(**kwargs)
        context['generos'] = generos

        return context
    
class LibroListView(generic.ListView):
    model = Libro
    paginate_by = 8
    
    context_object_name = 'libros'
    # en este caso va un modelo

    queryset = Libro.objects.all()
    # si quiero filtrar

    template_name = 'libros.html'
    # nombre del template

    def get_context_data(self, **kwargs):
        libros = Libro.objects.all()
        
        context = super(LibroListView, self).get_context_data(**kwargs)
        context['libros'] = libros
        
        return context

#Para esta clase solo se envian un listados de libros (un listado). Si queremos renderizar mas datos, se puede 
#implementar la funcion get_context_data

class LibroDetailView(generic.DetailView):
    model = Libro
    template_name = 'libro.html'
    # es obligatorio el nombre del template

    def libro_detail_view(request, pk):
        try:
            libro = Libro.objects.get(pk=pk)

        except Libro.DoesNotExist:
            raise Http404("Ooops! El Libro no existe")
        
        context = {
            'libro':libro,
        }
        return render(request, 'libro.html', context)

#Clase para poder visualizar los idiomas
class IdiomasListView(generic.ListView):
    model = Idioma
    context_object_name = 'idiomas'
    queryset = Idioma.objects.all()
    template_name = 'idiomas.html'

    def get_context_data(self, **kwargs):
        idiomas = Idioma.objects.all()

        context = super(IdiomasListView, self).get_context_data(**kwargs)
        context['idiomas'] = idiomas

        return context

class EjemplarListView(generic.ListView):
    model = Ejemplar
    context_object_name = 'ejemplares'
    queryset = Ejemplar.objects.all()
    template_name = 'ejemplares.html'

    def get_context_data(self, **kwargs):
        ejemplares = Ejemplar.objects.all()
        
        context = super(EjemplarListView, self).get_context_data(**kwargs)
        context['ejemplares'] = ejemplares

        return context

class EjemplarDetailView(generic.DetailView):
    model = Ejemplar
    template_name = 'ejemplar.html'
    
    def ejemplar_detail_view(request, pk):
        
        try:
            ejemplar = Ejemplar.objects.get(pk=pk)
        except:
            raise Http404("Ooops! El ejemplar no exite.")
        
        return render(request, 'ejemplar.html', {'ejemplar':ejemplar})