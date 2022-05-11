from typing import List, Optional
from ninja import NinjaAPI


api = NinjaAPI()

@api.get("/test")
def test(request):
    return {'message': 'success!'}

