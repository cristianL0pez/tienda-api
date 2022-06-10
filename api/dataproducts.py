import requests


url = 'https://fakestoreapi.com/products?limit=20' #url de la api
data =  requests.get(url)                                     #request generica 
productjson = data.json()                               #tranformo data en json
####################################################################
#creo la lista products y vacia
products = []                                                
for pro in productjson:
    name = pro['title']
    description = pro['description']
    price = pro['price']
    image = pro['image']
    products.append({'name':name, 'description':description, 'price':price, 'image':image})
    


