from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return "Hello world"

@api.get("/clientes")
def clientes(request):
    return "Clientes"