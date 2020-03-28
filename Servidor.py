import socket
import os
import threading
import time

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.bind(('', 8000))


ser.listen(2) 
client = []

os.system('color 9')
os.system('cls')

def agregar(espacio):
    while 0<espacio:
        print("***Esperando clientes || Espacio para: "+ str(espacio) +"***")
        espacio-=1
        cli, addr = ser.accept()
        client.append(cli)
        print("***Conexion aceptada***")
        print("recibido de la IP:  " + str(addr[0]) + " Puerto: " + str(addr[1]))
    print("***Server Closed***")
    ser.close()
    
hilo_agregar=threading.Thread(target=agregar, args=(2,))
hilo_agregar.start()

def aceptar(i):
    while True:
        try:
            get = client[i].recv(1024)
            print(get)
            client[i].send(bytes("Recibido", 'utf8'))
        except:
            print("***Cliente caido***")
            break
    client[i].close()

a=0
while True:
    if a<len(client):
        hilo=threading.Thread(target=aceptar, args=(a,))
        hilo.start()
        a+=1

