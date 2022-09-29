
from http.client import HTTPResponse

from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template


def hola(request):
   return HttpResponse('<h1>Buenos dias, clase 41765<h1/>')

def fecha(request):
   fecha_y_hora = datetime.now()
   return HttpResponse(f'La fecha y hora actual es: {fecha_y_hora}')

def calcular_fecha_nacimiento(request,edad):
   fecha = datetime.now().year - edad
   return HttpResponse(f'Tu fecha de nacimiento para tus {edad} años  es: {fecha}')

def mi_template(request):

   cargar_archivo = open(r'C:\Users\Usuario\Desktop\41765\prueba_mvt\templates\template.html', 'r')

   template = Template(cargar_archivo.read())

   cargar_archivo.close()

   contexto = Context()

   template_renderizado = template.render(contexto)

   return HttpResponse(template_renderizado)





