#!/usr/bin/env python3

import socket

HEADER_LEN = 64
MSG_FORMAT = "utf-8"
DISCONN_MSG = "q"
SERVER_PORT = 6969
SERVER_IP_ADDR = socket.gethostbyname(socket.gethostname())
SERVER_SOCK_ADDR = (SERVER_IP_ADDR, SERVER_PORT)

def send(msg):
    msg = msg.encode(MSG_FORMAT)
    msg_len = len(msg)
    msg_len = str(msg_len).ljust(64," ").encode(MSG_FORMAT)
    client_socket.send(msg_len)
    client_socket.send(msg)



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_SOCK_ADDR)
while True:
    inp = input()
    send(inp)
    if inp == DISCONN_MSG:
        break
client_socket.close()
