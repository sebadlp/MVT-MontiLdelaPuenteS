from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Fliares

# Create your views here.

def principal(request):
    return HttpResponse('<h1>Mi pagina Principal</h1>')

def datos_personas(request):
    
    template = loader.get_template('index.html')
    
    persona1 = Fliares(nombre='Pepe Argento', edad=85, fecha_creacion='2022-06-01')
    persona2 = Fliares(nombre='Dexter', edad=120, fecha_creacion='2022-06-01')   
    persona3 = Fliares(nombre='Cristobalito', edad=450, fecha_creacion='2022-06-01')
    
    persona1.save()
    persona2.save()
    persona3.save()
    
    render = template.render({'lista_objetos':[persona1, persona2, persona3]})
    
    return HttpResponse(render)