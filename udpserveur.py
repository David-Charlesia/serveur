#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:16:29 2020

@author: david
"""

host, port = ('',5678)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))

while True:
    socket.listen()
    conn, adress=socket.accept()
    print("Client connecté !")
    
    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)

conn.close()
socket.close()