import os

def save_file_paths(directory, output_file):
    # Listar todos los archivos en el directorio dado
    file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    
    # Escribir las rutas de los archivos en el archivo de salida
    with open(output_file, 'w') as f:
        f.write('{\n  "images": [\n')
        for path in file_paths[:-1]:
            f.write(f'    "{path}",\n')
        # Añadir el último archivo sin coma al final
        f.write(f'    "{file_paths[-1]}"\n')
        f.write('  ]\n}\n')

# Usar la función con la carpeta deseada y el nombre del archivo de salida
save_file_paths('icons', 'imageList.json')
