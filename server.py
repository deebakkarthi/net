#!/usr/bin/env python3

import socket
import threading

HEADER_LEN = 64
MSG_FORMAT = "utf-8"
DISCONN_MSG = "q"
PORT = 6969
IP_ADDR = socket.gethostbyname(socket.gethostname())
SOCK_ADDR = (IP_ADDR, PORT)

def client_handle(client_socket, addr):
    print(f"New connection from {addr}")
    while True:
        msg_len = client_socket.recv(HEADER_LEN).decode(MSG_FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = client_socket.recv(msg_len).decode(MSG_FORMAT)
            if msg == DISCONN_MSG:
                print(f"Connection closed to {addr}")
                break
            print(f"[{addr}] {msg}")
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SOCK_ADDR)

server_socket.listen()
while True:
    client_socket, addr = server_socket.accept()
    thread = threading.Thread(target=client_handle, args=(client_socket, addr))
    thread.start()
    print(f"Active connections = {threading.active_count() - 1}")
