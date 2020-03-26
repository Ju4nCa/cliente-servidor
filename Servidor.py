import socket
import os

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser.bind(('', 8000))

ser.listen(2)
get=""
msj = bytes(get, 'utf-8');
os.system('color 9')
os.system('cls')
print("Esperando clientes")
cli, addr = ser.accept()
print("Conexion aceptada")

while True:
    try:
        get = cli.recv(1024)
    except:
        print("***Servidor caido***")
        os.system('color')
        os.system('exit')
    print("recibido de la IP:  " + str(addr[0]) + " Puerto: " + str(addr[1]))
    print(get)
    cli.send(bytes("Recibido", 'utf8'))

cli.close()
ser.close()

print("Conexiones cerradas")
os.system('color')
