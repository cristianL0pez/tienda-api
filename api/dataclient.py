import requests


url = 'https://randomuser.me/api/?results=20&inc=name,picture,dob,email,id,location,login,phone,registered' #url de la api
data =  requests.get(url)                                     #request generica 
users = data.json()['results']                                #tranformo data en json
####################################################################
#creo la lista usuarios y vacia
clients = []                                                
for user in users:
    first_name =user['name']['first']
    last_name = user['name']['last']
    mail = user['email']
    birthdate = user['dob']['date']
    address = user['location']['street']
    phone = user['phone']
    password = user['login']['password']
    image = user['picture']['large']
    clients.append({'first_name':first_name, 'last_name':last_name, 'mail':mail, 'birthdate':birthdate, 'address':address, 'phone':phone, 'password':password, 'image':image})

