from django.urls import path
from .views import principal, datos_personas

urlpatterns = [
    path('', principal),
    path('personas', datos_personas),

]