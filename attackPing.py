import socket


def verificar_puerto(ip, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Establecer un tiempo de espera para la conexión
    s.settimeout(1)  # Tiempo en segundos
    
    try:
        # Intentar conectar al puerto especificado
        s.connect((ip, puerto))
    except (socket.timeout, socket.error):
        # Si ocurre una excepción, el puerto está cerrado o inalcanzable
        return False
    finally:
        # Cerrar el socket
        s.close()
    
    # Si la conexión fue exitosa, el puerto está abierto
    return True

ip = "89.208.107.49"

for i in range(8000, 9000):
    print(f"PORT: {i} : {verificar_puerto(ip, i)}")
