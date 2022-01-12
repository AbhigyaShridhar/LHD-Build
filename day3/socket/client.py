import socket
import time

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!exit"

def connect():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(ADDR)
  return client

def send(client, msg):
  message = msg.encode(FORMAT)
  client.send(message)

def start():
    connection = connect()

    while True:
        msg = input("Message (q for quit): ")

        if msg == 'q':
            break

        send(connection, msg)
    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)

start()
