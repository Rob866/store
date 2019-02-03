from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nombre =  models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)


    class Meta:
        ordering=('nombre',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('store:productos_por_categoria',args=[self.slug])    


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,related_name="categoria",on_delete= models.CASCADE)
    nombre =   models.CharField(max_length=200,db_index=True)
    slug= models.SlugField(max_length=200,db_index=True)
    imagen =models.ImageField(upload_to="productos/%Y/%m/%d",blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    almacen = models.PositiveIntegerField()
    disponibilidad = models.BooleanField(default=False)
    creado =  models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ('nombre',)
        index_together= (('id','slug'))

    def __str__(self):
        return self.nombre 

    def get_absolute_url(self):
        return reverse("store:producto_detalles",args=[self.id,self.slug])
        

