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
    path('autores/new/', views.autor_new, name='autor_new'),
    path('autores/update/<pk>', views.autor_update, name='autor_update'),

    path('idiomas/', views.IdiomasListView.as_view(), name='idiomas'),

    path('ejemplares/', views.EjemplarListView.as_view(), name='ejemplares'),
]
