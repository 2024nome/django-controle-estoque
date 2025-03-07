
from django.contrib import admin
from django.urls import path
from apps.produtos.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
    
]
