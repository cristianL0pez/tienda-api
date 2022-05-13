from typing import List, Optional
from ninja import NinjaAPI


api = NinjaAPI(
    title="Tiendita API",
    version="0.1.0",
    description="Tiendita API",
)

@api.get("/clients")
def test(request):
    return {'message': 'success!'}

