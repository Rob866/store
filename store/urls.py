from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',lambda r : HttpResponseRedirect('store')),
    path('store/', include("productos.urls",namespace="store"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
