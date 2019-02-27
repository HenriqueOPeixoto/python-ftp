import os
import user
import host

class Terminal:
	
	user = None
	host = None
	login_msg = None
	logout_msg = None
	
	def __init__(self):
	    
		self.user = user.User()
		self.host = host.Host()
	
	# Shows welcome message
	def display_startup_sequence(self):
		
		print('Python FTP Manager')
		print('---------------------------------')
		print('Version 0.8.2-alpha, by CodeArch')
		print('\n')
		
	# Asks if the user wants to host a server or connect to an existing one
	def ask_if_server(self):
		
		print('Choose an option from below: ')
		print('\n')
		print('[1]: Server')
		print('[2]: Client')
		print('\n')
		print('Insert option: ', end='')
		
		user_option = input()
		
		if user_option == '1':
			self.user.is_server = True
		elif user_option == '2':
			self.user.is_server = False
		
		return self.user.is_server
		
	def display_server_config_sequence(self):
		
		print('Insert username: ', end='')
		self.user.username = input()
		
		print('Insert password: ', end='')
		self.user.password = input()
		
		while True:
			
			try:
				print('Insert directory to share: ', end='')
				self.user.dir_ = input()
				
				# Checking if a directory exists. If false, raise NotADirectoryError
				# If it exists, break the loop and continue operations
				if os.path.isdir(self.user.dir_) == False:
					raise NotADirectoryError from OSError
				break
			except NotADirectoryError:
				print('Error: Not a directory or directory not found')
	
		
		print('Insert level of access (R for read/RW for Read/Write): ', end='')
		access_level = input().upper()
		while True:
		
			if access_level == 'R':
				
				# Sets Read Only permissions
				self.user.permissions = 'elr'
				break
			
			elif access_level == 'RW':
				
				# Sets Read/Write permissions
				self.user.permissions = 'elradfwMT'
				break
			
			else:
				
				# Checks if the user inserted something else and asks again
				print('Use R for read and RW for Read/Write: ', end='')
				access_level = input().upper()
		
		# Returns user account information to be used as hosting parameters
		return self.user
	
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
			# The statement below will malfunction if the user types a string.
			# An exception needs to be added here
			port = int(port)
		
		print('Insert username (default = None): ', end='')
		username = input()
		
		print('Insert password (default = None): ', end='')
		password = input()
		
		# Sets all the information necessary in the Host class and returns these values
		self.host.address = address
		self.host.port = port
		self.host.username = username
		self.host.password = password
		
		return self.host
		
	def display_help_message(self):
		with open('help.txt', 'r') as help_file:
			line_index = 0
			for line in help_file:
				if line_index <= 3:
					line_index += 1
				else:
					print(line, end='')
		
	def get_user_input(self):
			
			command = input('> ')
			
			return command