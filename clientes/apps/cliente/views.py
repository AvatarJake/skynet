from typing import Any
from django import http
from django.http import JsonResponse
from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from .models import Cliente
import json
import uuid

# Create your views here.
class ClienteView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=None):
        if id:
            try:
                uuid_obj = uuid.UUID(id)
                clientes = list(Cliente.objects.filter(id=str(uuid_obj)).values())
                if len(clientes) > 0:
                    cliente = clientes[0]
                    datos = cliente
                else:
                    datos = {'message': "Cliente not found..."}
            except ValueError:
                datos = {'message': "Invalid UUID format"}
        else:
            clientes = list(Cliente.objects.values())
            if len(clientes) > 0:
                datos = clientes
            else:
                datos = {'message': "No se encontró información"}
        
        return JsonResponse(datos, safe=False)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Cliente.objects.create(
            nombres=jd['nombres'], 
            apellidos=jd['apellidos'], 
            email=jd['email'],
            telefono=jd['telefono'],
            direccion=jd['direccion'],
            fecha_union=jd['fecha_union'],
            activo=jd['activo'], 
            notas=jd['notas'], 
            location=jd['location'])
        datos={'message':"Success"}

        return JsonResponse(datos)
    
    def put(self, request, id=None):
        jd = json.loads(request.body)
        if id:
            try:
                uuid_obj = uuid.UUID(id)
                cliente = Cliente.objects.filter(id=str(uuid_obj)).first()
                if cliente:
                    cliente.nombres = jd.get('nombres', cliente.nombres)
                    cliente.apellidos = jd.get('apellidos', cliente.apellidos)
                    cliente.email = jd.get('email', cliente.email)
                    cliente.telefono = jd.get('telefono', cliente.telefono)
                    cliente.direccion=jd.get('direccion',cliente.direccion)
                    cliente.fecha_union = jd.get('fecha_union', cliente.fecha_union)
                    cliente.activo = jd.get('activo', cliente.activo)
                    cliente.notas = jd.get('notas', cliente.notas)
                    cliente.location = jd.get('location', cliente.location)
                    cliente.save()
                    datos = {'message': "Cliente actualizado correctamente"}
                else:
                    datos = {'message': "Cliente no encontrado"}
            except ValueError:
                datos = {'message': "Formato de UUID no válido"}
        else:
            clientes = list(Cliente.objects.values())
            if len(clientes) > 0:
                datos = {'message': "Éxito", 'clientes': clientes}
            else:
                datos = {'message': "No se encontró información"}

        return JsonResponse(datos)

    
    def delete(self, request,id=None):
        if id:
            try:
                uuid_obj = uuid.UUID(id)
                clientes = list(Cliente.objects.filter(id=str(uuid_obj)).values())
                if len(clientes) > 0:
                    Cliente.objects.filter(id=id).delete()
                    datos = {'message': "Success"}
                else:
                    datos = {'message': "Cliente no encontrado..."}
            except ValueError:
                datos = {'message': "Invalid UUID format"}
        else:
            clientes = list(Cliente.objects.values())
            if len(clientes) > 0:
                datos = {'message': "Exitoso", 'clientes': clientes}
            else:
                datos = {'message': "No se encontró información"}
        
        return JsonResponse(datos)
 