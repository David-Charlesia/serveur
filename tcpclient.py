#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:16:29 2020

@author: david
"""
import socket
import sys

#définition des paramètres d'entrées
host = str(sys.argv[1])
port = int(sys.argv[2])
msg = str(sys.argv[3])

host, port = (host, port)

#création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port)) #connexion au serveur
    print("Connecte au serveur")

    #envoie du message
    data = msg.encode("utf8") #encodage du msg
    socket.send(data) #envoie du msg

    data = socket.recv(1024) #reception de la reponse du serveur
    data = data.decode("utf8") #décodage de la réponse
    data = "recu "+data #syntaxe respectée
    print(data)

except Exception as e: #si erreur de connexion ou erreur d'envoie du msg
    print(e)

finally :
    socket.close() #fermeture du socket
