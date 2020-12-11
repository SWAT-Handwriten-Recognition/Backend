Handwritten API REST
=============


docker-compose -f local.yml build

docker-compose -f local.yml up

docker-compose -f local.yml up --build

Comandos de Administración

1. docker-compose -f local.yml run --rm django python manage.py createsuperuser
2. docker-compose -f local.yml run --rm django python manage.py makemigrations
3. docker-compose -f local.yml run --rm django python manage.py migrate


Habilitar debugger

Pasos:

1. Ejecutar docker-compose -f local.yml up --build 
2. Ejecutar docker-compose -f local.yml ps
3. Matar el contenedor de django con: docker rm -f (ID)
4. Correr docker-compose -f local.yml run --rm --service-ports django
5. Agregar al codigo import ipdb;ipdb.set_trace()
