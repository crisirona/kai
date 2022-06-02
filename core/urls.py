from django.urls import path
#se importa todo de views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('agregar_bowl/<int:producto_id>/', views.agregar_bowl, name="AddB"),
    #path('agregar_handclassic/<int:producto_id>/', views.agregar_handclassic, name="AddHC"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),  
    #se asigna ruta, se toma funcion de views y se le da nombre

    path('nuevoproducto/', views.NuevoProducto, name='newproduct'),
    path('listaproducto/', views.ListaProducto, name='listproduct'),
    path('modificarproducto/<int:id>', views.Update, name='updateproduct'),
    path('eliminarproducto/<int:id>', views.EliminarProducto, name='deleteproduct'),
    #path('carrito/', views.Carrito, name='carrito'),

    path('registros/',views.registros,name='registros'),
]