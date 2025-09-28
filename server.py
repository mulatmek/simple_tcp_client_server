import socket
import threading
from config import *

#binding
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[SERVER] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            print(msg_length)
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False

            print(F"[SERVER] {addr} {msg}")

    conn.close()




def start():
    server.listen()
    print(f"[SERVER] server start listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()
        print(f"[SERVER] Active connections {threading.activeCount() -1}")


print("[SERVER] server is starting")
start()

