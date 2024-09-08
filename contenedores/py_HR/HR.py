import os
import time
import sys

#proceso de alto consumo de RAM Calculamos el 2% de la memoria y lo llenamos
def main():
    
    total_memory = 16 * 1024 * 1024 * 1024  
    target_memory = total_memory * 0.02  
    print(f"Consumiendo aproximadamente {target_memory / (1024 * 1024)} MB de RAM")

    
    block_size = 1024 * 1024  
    num_blocks = int(target_memory // block_size)
    large_list = []

    for _ in range(num_blocks):
        large_list.append(bytearray(block_size))  

    # Esto es para mantener el proceso activo
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Memoria liberada")

if __name__ == "__main__":
    main()
