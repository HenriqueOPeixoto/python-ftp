import os
import ip_retriever
import terminal

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer


class FTPServer:

    server = None

    def __init__(self, user):

        authorizer = DummyAuthorizer()
        
        authorizer.add_user(
            user.username,
            user.password,
            user.dir_,
            perm=user.permissions)
        
        handler = FTPHandler
        handler.authorizer = authorizer
        
        handler.banner = 'Welcome to a Python FTP Server!'

        address = (str(ip_retriever.get_ip_address()), 2121)
        self.server = ThreadedFTPServer(address, handler)

        self.server.max_cons = 10
        self.server.max_cons_per_ip = 5

        print('\nServer Address: ftp://{}:{}\n'.format(address[0], address[1]))

    def start_server(self):

        self.server.serve_forever()
