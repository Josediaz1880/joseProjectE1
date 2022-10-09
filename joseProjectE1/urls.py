from django.contrib import admin
from django.urls import path
from firstAppE1.views import index, renderproyecto1, renderproyecto2, renderproyecto3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('proyectos/', renderproyecto1),
    path('proyectos2/', renderproyecto2),
    path('proyectos3/', renderproyecto3) 
]
