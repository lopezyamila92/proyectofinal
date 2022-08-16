from django.urls import path
from .views import List_articles
from proyecto.views import categorias
from proyecto.views import inicio
from autos.views import create_autos , list_autos , servicio , inicio , primer_formulario, search_products, delete_product , update_product, List_articles
    
 



urlpatterns = [
    path("", inicio),
    path('categorias/', categorias, name="categorias"),
    path('create_autos/', create_autos, name = "create_autos"),
    path('list_autos/', list_autos, name = "list_autos"),
    path('servicio/', servicio, name="servicio"),
    path('primer-formulario/', primer_formulario, name="primer-formulario"),
    path('search-products/', search_products, name="search_products"),
    path("delete-product/<int:pk>/", delete_product, name="delete_product"),
    path("update-product/<int:pk>/", update_product, name="update_product"),
    path("list-articles/", List_articles.as_view(), name="List_articles"),
]



