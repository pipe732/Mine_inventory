from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Fixed .py to .urls
    path('mine/', include('mine_inventory.urls')),
    path('prestamo/', include('prestamo.urls')),
    path('inventario/', include('inventario.urls')),
]