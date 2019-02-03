from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Categoria,Producto

# Create your views here.

def about_page(request):
    name = "Tienda virtual"
    context= {"name": name }
    return render(request,'productos/about.html',context)

def productos_page(request,categoria_slug=None):
    categoria= None
    categorias = Categoria.objects.all()
    productos= Producto.objects.filter(disponibilidad=True)
    if categoria_slug :
        categoria = get_object_or_404(categorias,slug=categoria_slug)
        productos = productos.filter(categoria=categoria)
    
    paginator= Paginator(productos,6)
    page= request.GET.get('page')

    try: 
        items= paginator.page(page)
    except PageNotAnInteger: 
           items = paginator.page(1) 
    except EmptyPage:
            items = paginator.page(paginator.num_pages)
        

    context = {"categoria": categoria ,"categorias": categorias,"items": items }
    return render(request,"productos/posts/list.html",context)


def producto_detalles(request,id,producto_slug):

    productos = Producto.objects.all()
    producto = get_object_or_404(productos,id=id,slug=producto_slug) 
   
    context = { "producto": producto}
    return render(request,"productos/posts/detalles.html",context)