# documentación levantamiento de proyecto tiendita api

proyecto de api con datos de clientes productos y proveedores creado con las siguientes tecnologías

1. Django
2. Django-ninja
3. docker-compose 
4. postgres
5. nginx

para poder levantar este proyecto en tu maquina debes tener instalado docker compose 

[https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-es](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-es)

luego seguir los siguientes pasos

1. clonar el siguiente repositorio  https://github.com/cristianL0pez/tienda-api.git

       

```bash
git clone https://github.com/cristianL0pez/tienda-api.git
```

1. luego Tambien debes cambiarle los nombres a los archivos [docker-compose copy.yml](https://github.com/cristianL0pez/tienda-api/blob/main/docker-compose%20copy.yml) y [.env copy](https://github.com/cristianL0pez/tienda-api/blob/main/.env%20copy)

```
docker-compose copy.yml por docker-compose.yml
.env copy por .env
```

1.luego tendrás que  crear una secret key al proyecto ya que por seguridad no posee una secret te dejo una pagina para crear una secret  y deberás ponerla en el  .env  

```
## en este archivo estaran todas las variables de entorno cambiarlas del archivo
## do not put this file under version control!
##antes de correr el docker generar una secret key desde esta pagina https://miniwebtool.com/es/django-secret-key-generator/
SECRET_KEY='tu secret key'
## el debug en desarrollo deve estar en True para pasar a produccion  queda en false
DEBUG=True
```

1. luego deberás levantar el proyecto con docker-compose

```bash
sudo docker-compose up --build
```

1. en este paso deberás hacer la migración de la base de datos

```bash
sudo docker-compose run web python manage.py migrate
```

1. luego podrás  crear el super usuario para poder realizar cambios en el proyecto

```bash
sudo docker-compose run web python manage.py createsuperuser
```

Con esto ya tendrías levantado el proyecto tiendita api
