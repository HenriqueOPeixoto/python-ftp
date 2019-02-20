import os
import user
import host

class Terminal:
	
	_user = None
	_host = None
	_login_msg = None
	_logout_msg = None
	
	def __init__(self):
	    
		self._user = user.User()
		self._host = host.Host()
	
	# Shows welcome message
	def display_startup_sequence(self):
		
		print('Python FTP Manager')
		print('---------------------------------')
		print('Version 0.7.1, by CodeArch')
		print('\n')
		
	# Asks if the user wants to host a server or connect to an existing one
	def ask_if_server(self):
		
		print('Choose an option from below: ')
		print('\n')
		print('[1]: Server')
		print('[2]: Client')
		print('\n')
		print('Insert option: ', end='')
		
		_user_option = input()
		
		if _user_option == '1':
			self._user.is_server = True
		elif _user_option == '2':
			self._user.is_server = False
		
		return self._user.is_server
		
	def display_server_config_sequence(self):
		print('Insert username: ', end='')
		self._user.username = input()
		print('Insert password: ', end='')
		self._user.password = input()
		
		while True:
			
			try:
				print('Insert directory to share: ', end='')
				self._user.dir_ = input()
				
				# Checking if a directory exists. If false, raise NotADirectoryError
				# If it exists, break the loop and continue operations
				if os.path.isdir(self._user.dir_) == False:
					raise NotADirectoryError from OSError
				break
			except NotADirectoryError:
				print('Error: Not a directory or directory not found')
	
		
		print('Insert level of access (R for read/RW for Read/Write): ', end='')
		access_level = input().upper()
		while True:
		
			if access_level == 'R':
				
				# Sets Read Only permissions
				self._user.permissions = 'elr'
				break
			
			elif access_level == 'RW':
				
				# Sets Read/Write permissions
				self._user.permissions = 'elradfwMT'
				break
			
			else:
				
				# Checks if the user inserted something else and asks again
				print('Use R for read and RW for Read/Write: ', end='')
				access_level = input().upper()
		
		# Returns user account information to be used as hosting parameters
		return self._user
	
	def display_client_config_sequence(self):
		
		print('Insert address (default = 0.0.0.0): ', end='')
		address = input()
		print('Insert port (default = 2121): ', end='')
		port = input()
		
		if address == '':
			address = '0.0.0.0'
		
		if port == '':
			port = 2121
		
		else:
			port = int(port)
		
		print('Insert username (default = None): ', end='')
		username = input()
		
		print('Insert password (default = None): ', end='')
		password = input()
		
		# Sets all the information necessary in the Host class and returns these values
		self._host.address = address
		self._host.port = port
		self._host.username = username
		self._host.password = password
		
		return self._host
		
	def get_user_input(self):
			
			command = input('> ')
			
			return command