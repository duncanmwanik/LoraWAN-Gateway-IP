import socket
import os
 
def get_ip_address():
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ip_address = s.getsockname()[0]
    gateway = gw[2]
    host = socket.gethostname()
    print ("IP:", ip_address, " GW:", gateway, " Host:", host)

    return ip_address