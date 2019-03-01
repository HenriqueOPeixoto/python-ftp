import os
import socket


def get_ip_address():
    # Checks if the machine is using Windows
    if (os.name == 'nt'):

        # On Windows the command below works perfectly fine and returns the
        # IPv4. Unix-based systems tend to return 127.0.0.1 which doesn't work
        return socket.gethostbyname(socket.gethostname())

    else:

        # Creates a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connects to the Google Public DNS Server
        s.connect(('8.8.8.8', 80))

        # Retrieves IPv4 and port information. The IP is on the index 0
        ip_addr = s.getsockname()[0]

        # Closes the socket
        s.close()

        return ip_addr
