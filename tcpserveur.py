#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:16:50 2020

@author: david
"""
import socket
import sys

#définition des paramètres d'entrées
port = int(sys.argv[1])

host, port = ('',port)

#créeation du socket tcp
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))
#socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) pour le broadcast, ne fonctionne pas
#socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) pour le broadcast, ne fonctionne pas

print("serveur demarrer")

while True:
    socket.listen(5)
    conn, adress=socket.accept() #connexion acceptée
    ip_client=adress[0]
    port_client=adress[1]
    aff='client d\'adresse ' + str(ip_client) + ' depuis port ' + str(port_client)
    print(aff)

    data = conn.recv(1024) #réception du msg
    data = data.decode("utf8") #décodage du msg
    data = "ok : " + data #syntaxe respectée
    print(data)

    data=data.encode("utf8")
    conn.send(data) #envoie de la confirmation serveur au Client

conn.close() #fermeture de la connexion
socket.close() #fermeture du socket
