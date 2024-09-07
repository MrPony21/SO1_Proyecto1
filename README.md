# SO1_Proyecto1
Este repositorio contendra el proyecto 1 de sistemas operativos 1


# Aqui pondre comandos de Docker para ayudarme
Para crear una imagen seria
- docker build -t {nombre de la imagen} .
Para ver las imagenes creadas
- docker images
Para crear nuestro contenedor
- docker run -d <id_image|repository>
Eliminar un contenedor
- docker rm <container_id>
Eliminar image
- docker rmi <image_id>
**Docker compose nos ayuda a visualizar lo que esta pasando dentro de los directorios de mi contenedor**
Comando para ejecutar el docker compose en segundo plano (Lo corremos como servicio)
- sudo docker compose up -d
Comando para eliminar el docker compose
- sudo docker compose down


# Comandos para ver los procesos
Para ver los procesos
- sudo ps aux