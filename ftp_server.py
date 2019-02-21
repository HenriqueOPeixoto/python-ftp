import os
import ip_retriever
import terminal

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer

class FTPServer:

	server = None


	def __init__(self, user):

		# Instantiates a 'virtual' users manager
		authorizer = DummyAuthorizer()

		# Adds a new user according to the following parameters:
		# username, password, homedir, perm="", msg_login="", msg_quit=""
		authorizer.add_user(user.username, user.password, user.dir_, perm=user.permissions)

		# Instantiates the FTPHandler class
		handler = FTPHandler
		handler.authorizer = authorizer

		# Defines a banner (string) that shows when user connects
		handler.banner = 'Welcome to a Python FTP Server!'

		# Instantiates the server class and listen on address [Machine IPv4]:2121
		address = (str(ip_retriever.get_ip_address()), 2121)
		self.server = ThreadedFTPServer(address, handler)

		# Limits the amount of possible connections
		self.server.max_cons = 10
		self.server.max_cons_per_ip = 5
		
		print('\nServer Address: ftp://{}:{}\n'.format(address[0], address[1]))
		
	def start_server(self):
		
		# Launch FTP Server
		self.server.serve_forever()
