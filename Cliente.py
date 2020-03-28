import socket
import os
import threading


HOST= '192.168.1.52'
PORT= 8000
con = socket.socket()

try:
    con.connect((HOST, PORT))
    os.system('color e')
    os.system('cls')
    print("***Conectado***")    
except:
    print("***Servidor caido***")


while True:
    os.system('cls')
    try:
        get = input("Mensaje Cliente a Servidor >> ")
        if get=='exit':
            os.system('color 7')
            break
        con.send(bytes(get, 'utf8'))
        data = con.recv(1024)
        print(data)
    except:
        print("***Cliente caido***")
        os.system('color 7')
        os.system('exit')
            
con.close()
print("Conexion cerrada")
os.system('color')

