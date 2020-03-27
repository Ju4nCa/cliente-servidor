import socket
import os
import threading

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser.bind(('', 8000))

ser.listen(2)
get="" 
client = []

os.system('color 9')
os.system('cls')

for i in range (0, 2):
    print("Esperando clientes")
    cli, addr = ser.accept()
    client.append(cli)
    print("Conexion aceptada")
    print("recibido de la IP:  " + str(addr[0]) + " Puerto: " + str(addr[1]))
i=0
while True:
    if i==2:
        i=0
    try:
        get = client[i].recv(1024)
        print(get)
        client[i].send(bytes("Recibido", 'utf8'))
    except:
        print("***Cliente caido***")
        print("Esperando clientes")
        cli, addr = ser.accept()
        client[i]=cli
        print("Conexion aceptada")
        print("recibido de la IP:  " + str(addr[0]) + " Puerto: " + str(addr[1]))            
    i+=1
cli.close()
ser.close()
print("Conexiones cerradas")



hilo1.start()
hilo2.start()


