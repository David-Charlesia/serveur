#!/usr/bin/env python3
import socket
import sys
import threading

'''********************************************Thread*********************************************************'''
class ThreadForClient(threading.Thread):
    """docstring for TreadForClient."""

    def __init__(self, conn):
        super(ThreadForClient, self).__init__()
        self.conn = conn

    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        data = "ok : " + data
        print(data)

        #renvoie d'une réponse
        data = "recu \"" + data + "\""
        data = data.encode("utf8")
        conn.send(data)

'''********************************************Thread*********************************************************'''

#initialisation de l'adresse IP et du port
host = str(sys.argv[1])
port = int(sys.argv[2])

#initialisation du socket cote serveur
host, port =('', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Le serveur a demarré...")

#mise en route du serveur
while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("client d'adresse " + str(address[0]) + " depuis port " + str(address[1]))

    #sans Thread
    '''#reception du message
    data = conn.recv(1024)
    data = data.decode("utf8")
    data = "ok : " + data
    print(data)

    #renvoie d'une réponse
    data = "recu \"" + data + "\""
    data = data.encode("utf8")
    conn.send(data)
    data = conn.recv(1024)
    data = data.decode("utf8")'''

    #activation du Thread
    my_thread = ThreadForClient(conn)
    my_thread.start()




#fermerture de la connexion puis du socket
conn.close()
socket.close()
