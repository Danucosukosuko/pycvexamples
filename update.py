import os
import requests
import zipfile
import shutil

GITHUB_API_URL = "https://api.github.com/repos/Danucosukosuko/pycvexamples/releases/latest"

def descargar_release(branch):
    response = requests.get(GITHUB_API_URL)
    
    if response.status_code == 200:
        release_info = response.json()
        assets = release_info['assets']
        
        for asset in assets:
            if branch in asset['name']:
                asset_url = asset['browser_download_url']
                filename = asset_url.split("/")[-1]
                
                print(f"Descargando {filename}...")
                
                # Descarga el archivo
                response = requests.get(asset_url)
                
                if response.status_code == 200:
                    print("Descarga completada.")
                    return response.content
    
    print(f"No se encontró la actualización de la rama {branch}.")
    return None

def descomprimir_release(archivo_zip):
    # Descomprime el archivo ZIP en la carpeta actual
    with zipfile.ZipFile(archivo_zip) as zip_ref:
        zip_ref.extractall()
    
    print("Instalando actualización...")
    
def actualizar_archivos():
    # Copia los archivos .py de la carpeta de descarga a la carpeta original
    source_folder = "pycvexamples"  # Carpeta original
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".py"):
                source_file = os.path.join(root, file)
                shutil.copy2(source_file, file)
                print(f"Archivo {file} Actualización instalada")
    
def menu():
    while True:
        print("PyCVExamples Updater")
        print("1. Descargar Stable")
        print("2. Descargar beta")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            archivo_zip = descargar_release("Stable")
            if archivo_zip:
                descomprimir_release(archivo_zip)
                actualizar_archivos()
        elif opcion == "2":
            archivo_zip = descargar_release("Beta")
            if archivo_zip:
                descomprimir_release(archivo_zip)
                actualizar_archivos()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
