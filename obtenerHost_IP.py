
import socket


hostName = socket.gethostname()
ip = socket.gethostbyname(hostName)
    
print("Hostname: " + hostName)
print("IP: " + ip)
    
    