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

host, port = (host,port)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))

print("serveur demarrer")

while True:
    socket.listen(5)
    conn, adress=socket.accept()
    print("Client connecte")

    data = conn.recv(1024)
    data = data.decode("utf8")
    data = "ok : " + data
    print(data)

    data_to_send="recu \"" + data + "\""
    data=data.encode("utf8")
    conn.send(data)

conn.close()
socket.close()
