import socket
import os

HOST= 'localhost'
PORT= 8000

con = socket.socket()
data=""
msj = bytes(data, 'utf-8')

try:
    con.connect((HOST, PORT))
except:
    print("***Servidor caido***")

print("***Conectado***")

while True:
    os.system('color e')
    try:
        get = input("Mensaje Cliente a Servidor >> ")
        if get=='exit':
            os.system('color')
            break
        con.send(bytes(get, 'utf8'))
        data = con.recv(1024)
        print(data)
    except:
        print("***Servidor caido***")
        os.system('color')
        os.system('exit')
        
con.close()
print("Conexion cerrada")
os.system('color')
