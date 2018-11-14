import socket
import threading
import random



def hilo(address):
    cliente, direccion = address
    random_names = ["proplayer", "weeaboo", "normie", "pepe", "pleb", "topkek", "fritanga", "chileno promedio", "equisde"]
    with cliente:
        name= random.choice(random_names)
        print("Ha ingresado", name)
        while True:
            mensaje, addr = cliente.recvfrom(1024)
            if not mensaje:
                break
            msj = str(direccion[0]) + ":" + str(direccion[1])+ " --> " +mensaje.decode("utf-8")
            print(name, "dijo: ", mensaje.decode())
            cliente.sendall(msj.encode())

HOST = ''
PORT = 15000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    print("Esperando una conexion...")
    server.listen(1)
    while True:
        threading.Thread(target=hilo, args=(server.accept(),)).start()
