import socket
ip = '127.0.0.1'
puerto = 15000
BUFSIZ = 1024


#client_socket = socket(AF_INET, SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((ip, puerto))
    while True:
        mensaje = input("Escriba su mensaje y presione enter ->  ")
        cliente.send(mensaje.encode())
        if mensaje is "quit":
            break

def recibir():

    while True:
        try:
            msj = cliente.recv(BUFSIZ).decode("utf-8")
            print(msj)
        except OSError:
            break