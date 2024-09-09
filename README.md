# MANUAL TECNICO

Aqui se explicara todo lo necesario para la creacion y instalacion del servicio

**Recomendacion**
Acceder en una terminal como modo superusuario

## Modulo de Kernel
Primero debemos ir a la ruta donde esta ubicado nuestro modulo y ejecutar
- make
- insmod sysinfo.ko

Aqui ya esta nuestro modulo ejecutado y la carpeta fue creada en /proc/sysinfo_202003220 
para visualizarla es con
- cat /proc/sysinfo_202003220 

## Creacion de Imagenes de Docker
Debemos de crear primero las imagenes que vamos a utilizar para eso primero accedemos a la carpeta contenedores y accedemos a cada una de las carpetas y con una terminal escribimos en cada una de ellas
- docker build -t (Nombre)
Los nombres utilizados son los siguientes
- alto_cpu_py
- alta_ram_py
- bajo_consumo_nodejs
- bajo_consumo_py

## Cronjob
Escribir en la terminal lo siguiente:
- crontab -e
- 1
- */30 * * * * /ruta completa del  GenerateContenedores.sh
ctrl+x

## Iniciar el servicio de rust
Primero instalamos dependencias
- cargo build
Luego ejecutamos
- cargo run



