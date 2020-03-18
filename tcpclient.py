#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:16:29 2020

@author: david
"""
import socket
import sys

host = str(sys.argv[1])
port = int(sys.argv[2])
msg = str(sys.argv[3])

host, port = (host, port)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port))
    print("Connecte au serveur")

    #envoie du message
    data = msg.encode("utf8")
    socket.send(data)

    #reception de la reponse
    data = socket.recv(1024)
    data = data.decode("utf8")
    data = "recu "+data
    print(data)

except Exception as e:
    print(e)

finally :
    socket.close()
