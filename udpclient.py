#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:55:57 2020

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
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.sendto(msg, (host, port))

socket.close()
