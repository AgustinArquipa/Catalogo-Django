from django.urls import path
from catalogo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros/', views.LibroListView.as_view(), name='libros'),
    path('libro/<pk>', views.LibroDetailView.as_view(), name='libro'),

    path('generos/', views.GeneroListView.as_view(), name='generos'),
    path('genero/new/', views.genero_new, name='genero_new'),
    path('genero/update/<pk>', views.genero_update, name='genero_update'),

    path('autores/', views.AutoresListView.as_view(), name='autores'),
    path('autor/<pk>', views.AutorDetailView.as_view(), name='autor'),
    path('autores/new/', views.autor_new, name='autor_new'),
    path('autores/update/<pk>', views.autor_update, name='autor_update'),

    path('idiomas/', views.IdiomasListView.as_view(), name='idiomas'),
    path('idiomas/new/', views.idioma_new, name='idioma_new'),
    path('idiomas/update/<pk>', views.idioma_update, name='idioma_update'),

    path('ejemplares/', views.EjemplarListView.as_view(), name='ejemplares'),
    path('ejemplar/<pk>', views.EjemplarDetailView.as_view(), name='ejemplar'),
    path('ejemplar/new/', views.ejemplar_new, name='ejemplar_new'),
    path('ejemplar/update/<pk>', views.ejemplar_update, name='ejemplar_update'),
]
