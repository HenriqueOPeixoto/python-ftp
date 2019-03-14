import os
import socket


def get_ip_address():

    if (os.name == 'nt'):

        # On Windows the command below works. However, Unix based systems
        # return 127.0.0.1
        return socket.gethostbyname(socket.gethostname())

    else:

        # A workaround to the issue above was to connect to Google Public
        # DNS Server and return the address used in the connection
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip_addr = s.getsockname()[0]
        s.close()

        return ip_addr
