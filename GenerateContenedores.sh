#!/bin/bash

#Script donde generamos 10 contenedores con nombre aleatorio

#creamos un nombre aleatorio de 10 caracteres con el modulo especial /dev/random
ContainerNameAleatorio(){
    nombre=$(head -c 100 /dev/random | tr -dc 'a-zA-Z0-9' | head -c ${1:-10})
    echo "${nombre}"
}


#Mis imagenes
imagenes=("alto_cpu_py" "alta_ram_py" "bajo_consumo_nodejs" "bajo_consumo_py")

imagenes_seleccionadas=()
for i in {1..10}; do
    imagenes_seleccionadas+=("${imagenes[RANDOM % ${#imagenes[@]}]}")
done

for imagen in "${imagenes_seleccionadas[@]}"; do
    nombre=$(ContainerNameAleatorio)
    docker run -d --name "${nombre}" "$imagen"
done
