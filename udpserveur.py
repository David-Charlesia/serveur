#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:16:29 2020

@author: david
"""
import socket
import sys

#définition des paramètres d'entrées
port = int(sys.argv[1])

host, port = ("",port)

#créeation du socket tcp
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((host,port))

print("serveur demarrer")

while True:
    data, addr = socket.recvfrom(1024)

    ip_client=addr[0]
    port_client=addr[1]
    aff='client d\'adresse ' + str(ip_client) + ' depuis port ' + str(port_client)
    print(aff)

    data = data.decode("utf8") #décodage du msg
    data = "ok : " + data #syntaxe respectée
    print(data)

    data=data.encode("utf8")
    socket.sendto(data,addr)

socket.close()
