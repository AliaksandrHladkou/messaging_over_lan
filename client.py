# Message Sender over UDP
# This is a client to send message to a server over the local network
import os
from socket import *

def printBorder():
    print("=================================================")

def setAddress():
    printBorder()
    host = input("Enter IP address of destunation machine: ")
    port = input("Enter the port number of destination machine: ")

def defaultAddress():
    host = "192.168.55.101"
    port = 11111
    return host, port

def engine(host, port):
    printBorder()
    print("Connecting to %s with port %s." % (host, port))
    printBorder()

    serverAddress = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    while True:
        printBorder()
        userInput = input("Enter message. Type 'exit' to exit the programs: ") #typing exit will stop both client and server
        convertToBytes = bytes(userInput, 'utf-8')
        UDPSock.sendto(convertToBytes, serverAddress)
        if userInput == "exit":
            break
    UDPSock.close()
    os._exit(0)

def main():
    host = ""
    port = 0
    attempts = 3

    while attempts > 0:
        defaults = input("Use default address? (yes/no): ")
        if defaults == "yes":
            host, port = defaultAddress()
            break
        elif defaults == "no":
            setAddress()
            break
        else: 
            print("Invalid input, use either \"yes\" or \"no\". ")
            attempts -= 1
    
    if attempts == 0:
        printBorder()
        print("You have reached max # of attempts!")
        os._exit(0)
    
    engine(host, port)

if __name__ == "__main__":
    main()
