# MANUAL TECNICO

Aqui se explicara todo lo necesario para la creacion y instalacion del servicio

## Modulo de Kernel
Primero debemos ir a la ruta donde esta ubicado nuestro modulo y ejecutar
- make
- sudo insmod sysinfo.ko

Aqui ya esta nuestro modulo ejecutado y la carpeta fue creada en /proc/sysinfo_202003220 
para visualizarla es con
- cat /proc/sysinfo_202003220 
