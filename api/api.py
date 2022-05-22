from django.shortcuts import get_object_or_404
from ninja import Schema
from ninja import NinjaAPI, Form, File
from .models import *
from typing import List
from datetime import date
from ninja.files import UploadedFile
from ninja.security import django_auth


api = NinjaAPI( 
    csrf=True,
    title="Tiendita API",
    version="0.1.0",    
    description="Tiendita API",
)
#endpoin para subir archivos
@api.post("/upload-file")
def upload_file(request, files: List[UploadedFile] = File(...)):
    return [f.name for f in files]


#esquema para el cliente entrada al orm
class ClientIn(Schema):
    first_name: str
    last_name: str
    mail: str
    birthdate: date 
    address: str
    phone: str
    password: str
    image: str 

#esquema para el cliente salida del orm
class ClientOut(Schema):
    first_name: str
    last_name: str
    mail: str
    birthdate: date 
    address: str
    phone: str
    password: str
    image: str  

#endpoint para crear un empleado
@api.post("/client", auth=django_auth)
def create_client(request, payload: ClientIn):
    client = Client.objects.create(**payload.dict())
    return {"id": client.id}

#endpoint para obtener un empleado por id
@api.get("/client/{client_id}", response=ClientOut)
def get_client(request, client_id: int):
    client = get_object_or_404(Client, id=client_id)
    return employee

#endpoint para obtener todos los empleados
@api.get("/client", response=List[ClientOut])
def list_client(request):
    qs = Client.objects.all()
    return qs

#endpoint para actualizar un empleado
@api.put("/client/{client_id}")
def update_client(request, client_id: int, payload: ClientIn):
    client = get_object_or_404(Client, id=client_id)
    for attr, value in payload.dict().items():
        setattr(client, attr, value)
    client.save()
    return {"success": True}

#endpoint para eliminar un empleado
@api.delete("/client/{client_id}")
def delete_client(request, client_id: int):
    client = get_object_or_404(Client, id=cliente_id)
    client.delete()
    return {"success": True}