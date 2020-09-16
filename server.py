# Message Receiver over UDP
# This program receives messages from client over local network
import os
from socket import *

def engine():
    host = ""
    port = 11111
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    print("Waiting for new messages...")

    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        decoded = str(data, 'utf-8')
        if decoded == "exit":
            print("==========================================================")
            print("You received \"exit\" command. \nThis program will be closed now by th client. Goodbuy!")
            print("==========================================================")
            break
        print("Received message: " + decoded)

    UDPSock.close()
    os._exit(0)

def main():
    engine()

if __name__ == "__main__":
    main()
