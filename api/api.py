from itertools import product
from django.shortcuts import get_object_or_404
from ninja import Schema
from ninja import NinjaAPI,  File
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

############################################################################################################
#                                                                                                          #
#                                                                                                          #
############################################################################################################
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

############################################################################################################
#                                                                                                          #
#                                                                                                          #
############################################################################################################


#esquema para el producto salida del orm
class ProductIn(Schema):
    name: str
    description: str
    price: float
    image: str 
    stock: int
    category: str
#esquema para el  producto salida del orm
class ProductOut(Schema):
    name: str
    description: str
    price: float
    image: str 
    stock: int
    category: str
    created_at: date
    updated_at: date



############################################################################################################
#                                                                                                          #
#                                                                                                          #
############################################################################################################

#esquema para el supplier entrada del orm
class SupplierIn(Schema):
    name: str
    description: str
    mail: str
    phone: str
    address: str
    image: str

#esquema para el supplier salida del orm
class SupplierOut(Schema):
    name: str
    description: str
    mail: str
    phone: str
    address: str
    image: str
    created_at: date
    updated_at: date



#endpoint para crear un cliente
@api.post("/client", auth=django_auth, tags=["clients"])
def create_client(request, payload: ClientIn):
    client = Client.objects.create(**payload.dict())
    return {"id": client.id}

#endpoint para obtener un cliente por id
@api.get("/client/{client_id}", response=ClientOut,auth=django_auth, tags=["clients"])
def get_client(request, client_id: int):
    client = get_object_or_404(Client, id=client_id)
    return client

#endpoint para obtener todos los cliente
@api.get("/client", response=List[ClientOut],auth=django_auth, tags=["clients"])
def list_client(request):
    qs = Client.objects.all()
    return qs

#endpoint para actualizar un cliente
@api.put("/client/{client_id}", auth=django_auth, tags=["clients"])
def update_client(request, client_id: int, payload: ClientIn):
    client = get_object_or_404(Client, id=client_id)
    for attr, value in payload.dict().items():
        setattr(client, attr, value)
    client.save()
    return {"success": True}

#endpoint para eliminar un cliente
@api.delete("/client/{client_id}" ,auth=django_auth, tags=["clients"])
def delete_client(request, client_id: int):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return {"success": True}






############################################################################################################
#                                                                                                          #
#                                                                                                          #
############################################################################################################


#endpoint para crear un producto
@api.post("/product", auth=django_auth, tags=["product"])
def create_product(request, payload: ProductIn):
    product = Product.objects.create(**payload.dict())
    return {"id": product.id}

#endpoint para obtener un producto por id
@api.get("/product/{product_id}", response=ProductOut,auth=django_auth, tags=["product"])
def get_product(request,product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return product

#endpoint para obtener todos los producto
@api.get("/product", response=List[ProductOut],auth=django_auth, tags=["product"])
def list_product(request):
    products = Product.objects.all()
    return products

#endpoint para actualizar un producto
@api.put("/product/{product_id}", auth=django_auth, tags=["product"])
def update_client(request, product_id: int, payload: ProductIn):
    client = get_object_or_404(Product, id=product_id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}

#endpoint para eliminar un producto
@api.delete("/product/{product_id}", auth=django_auth, tags=["product"])
def delete_client(request, product_id: int):
    product = get_object_or_404(Product, id= product_id)
    product.delete()
    return {"success": True}


############################################################################################################
#                                                                                                          #
#                                                                                                          #
############################################################################################################


#endpoint para crear un producto
@api.post("/supplier", auth=django_auth, tags=["supplier"])
def create_supplier(request, payload: SupplierIn):
    supplier = Supplier.objects.create(**payload.dict())
    return {"id": supplier.id}

#endpoint para obtener un producto por id
@api.get("/supplier/{supplier_id}", response=SupplierOut,auth=django_auth, tags=["supplier"])
def get_product(request,supplier_id: int):
    supplier = get_object_or_404(Product, id=product_id)
    return supplier

#endpoint para obtener todos los producto
@api.get("/supplier", response=List[SupplierOut],auth=django_auth, tags=["supplier"])
def list_supplier(request):
    supplier = supplier.objects.all()
    return supplier

#endpoint para actualizar un producto
@api.put("/supplier/{supplier_id}", auth=django_auth, tags=["supplier"])
def update_supplier(request, supplier_id: int, payload: SupplierIn):
    Supplier = get_object_or_404(Supplier, id=supplier_id)
    for attr, value in payload.dict().items():
        setattr(Supplier, attr, value)
    Supplier.save()
    return {"success": True}

#endpoint para eliminar un producto
@api.delete("/supplier/{supplier_id}", auth=django_auth, tags=["supplier"])
def delete_supplier(request, supplier_id: int):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    supplier.delete()
    return {"success": True}

