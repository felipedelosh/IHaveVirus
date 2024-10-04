import requests

def verificar_directorio(base_url, rutas):
    """
    Verifica si las rutas especificadas existen en el servidor.

    :param base_url: URL base del servidor (por ejemplo, "http://89.208.107.49/")
    :param rutas: Lista de rutas para verificar.
    """
    for ruta in rutas:
        url = f"{base_url}{ruta}"
        try:
            respuesta = requests.head(url)  # Usar HEAD para verificar la existencia sin descargar el contenido
            if respuesta.status_code == 200:
                print(f"Directorio encontrado: {url}")
            else:
                print(f"Directorio no encontrado o inaccesible: {url} (Código de estado: {respuesta.status_code})")
        except requests.RequestException as e:
            print(f"Error al acceder a {url}: {e}")

# URL base del servidor
base_url = "http://185.155.184.32/"

# Lista de posibles rutas de directorios
rutas = [
    "media/",
    "util/",
    "util/utils.js",
    "ruta/con/subdirectorio/"
]

# Verificar existencia de directorios
verificar_directorio(base_url, rutas)