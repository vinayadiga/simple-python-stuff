#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:55:13 2016

@author: Vinay
"""
# Importing libraries
import socket

#create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local host name
host = socket.gethostname()

port = 9998

#bind to port
server_socket.bind((host,port))

#init queue
server_socket.listen(5)

while True:
    #establihing the connection
    client_socket,addr = server_socket.accept()
    print("Connection from %s" %str(addr))
    data = client_socket.recv(1024)
    print(data)
    client_socket.close()
