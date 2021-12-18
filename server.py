from os import system
import socket

HOST = '127.0.0.1'
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def Main():
    print('Start the server? [Y/N]')
    ans = input()

    if ans == 'Y':
        print("Starting Server...")
        system("cls")
        StartServer()

def StartServer():
    s.bind((HOST, PORT))
    print("Server Is Listening...")
    s.listen(5)
    EstablishConnection()

def EstablishConnection():
    c, addr = s.accept()
    print("Established Connection With", addr)

