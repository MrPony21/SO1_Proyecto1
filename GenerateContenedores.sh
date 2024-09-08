#!/bin/bash

#Mis imagenes
imagenes=("alto_cpu_py" "alta_ram_py" "bajo_consumo_nodejs" "bajo_consumo_py")

imagenes_seleccionadas=()
for i in {1..10}; do
    echo "${i}"
    imagenes_seleccionadas+=("${imagenes[RANDOM % ${#imagenes[@]}]}")
done


for imagen in "${imagenes_seleccionadas[@]}"; do
    docker run -d "$imagen"
done
