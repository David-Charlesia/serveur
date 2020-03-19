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

host, port = (host,port)

#créeation du socket tcp
socket = socket.socket()
socket.bind((host,port))

print("serveur demarrer")
