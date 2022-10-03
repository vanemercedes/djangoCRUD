from django.urls import path
from .views import crear_producto, listar_productos, borrar_producto


urlpatterns = [
    path('',listar_productos),
    path('new/',crear_producto,name='crear_producto'),
    path('borrar/<int:producto_id>/',borrar_producto,name='borrar_producto'),
]