
#importar módulo socket
import socket



#ip de loopback para el ejemplo
ip = '127.0.0.1' #puedo solicitar la ip con input o utilizar un scrip que me devuelva ip para determinado host

for port in range(1,1000): #puedo definir el rango que necesite entre (1, 65535)
    #inicio el socket para IPV4 y protocolo TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #defino el tiempo de espera
    socket.setdefaulttimeout(1)
    #conecto cliente con IP del servidor (el método connect_ex además devuelve error si no puede conectarse)
    result = s.connect_ex((ip, port))
    #imprimo puertos abiertos
    if result==0:
        print("Puerto {} abierto".format(port))
    s.close()
