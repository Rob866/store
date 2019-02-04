from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.about_page,name="about_page"),
    path('productos/',views.productos_page,name="productos_page"),
    path('productos/busqueda/',views.producto_busqueda,name="producto_busqueda"),
    path('productos/<slug:categoria_slug>/',views.productos_page, name='productos_por_categoria'),
    path('productos/detalles/<int:id>/<slug:producto_slug>/',views.producto_detalles, name='producto_detalles'),
]
