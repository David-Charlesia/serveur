#!/usr/bin/env python3
import socket
import sys

host = str(sys.argv[1])
port = int(sys.argv[2])

#initialisation du socket cote client
host, port =(host, port)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connexion au serveur
try:
    socket.connect((host, port))
    print("Client connecté..")


    #envoie du message
    data = input()
    data = data.encode("utf8")
    socket.send(data)

    #reception de la reponse
    data = socket.recv(1024)
    data = data.decode("utf8")


except Exception as e:
    print(e)
