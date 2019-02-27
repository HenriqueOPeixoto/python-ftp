import ftplib
import host
import os

class FTPClient:
	
	username = None
	password = None
	host = None
	ftp = None
	return_value = None
	commands = ('CWD', 'CDUP', 'LIST', 'NLST', 'STAT', 'MLSD', 'MLST', 
				 'SIZE', 'RETR', 'APPE', 'DELE', 'RMD', 'RNFR', 'RNTO', 
				 'MKD', 'STOR', 'STOU', 'SITE CHMOD', 'SITE MFMT')
	
	def __init__(self, host):
		
		# Instantiates a blank FTP Server connection
		self.ftp = ftplib.FTP()
		
		# Receives host data (address, username and password) that's passed as an argument
		self.host = host
		
		# Connects to the host
		self.ftp.connect(host.address, host.port)
		
		# Logs into the server
		self.ftp.login(host.username, host.password)
		
		# Lists files in a directory
		self.ftp.dir()
		
	def get_return_value(self):
		return self.return_value
		
	def execute_cmd(self, cmd):
		print('\n')
		
		cmd = cmd.upper()
		
		if cmd == 'LIST':
			self.ftp.dir()
		
		elif cmd == 'EXIT' or cmd == 'QUIT':
			self.ftp.quit()
			self.return_value = 'exit'
		
		elif cmd.startswith('CWD'):
			# Transforms the command in an array, in which the index one contains args
			cmd = cmd.split(' ')
			# Takes the argument of the command and changes the directory
			# The try is here to ensure that only one argument is given
			try:
				if len(cmd) == 2:
					self.ftp.cwd(cmd[1])
				else:
					raise IndexError
			except IndexError:
				print('Error: CWD takes 1 argument only. {} were given'.format(len(cmd) - 1))
				
		elif cmd.startswith('SIZE'):
			cmd = cmd.split(' ')
			print('{} bytes'.format(self.get_size(cmd[1])))
		
		elif cmd == 'HELP':
			self.return_value = 'help'
		
		elif cmd == 'PWD':
			print(self.ftp.pwd())
			
		elif cmd.startswith('RETR'):
			cmd = cmd.split(' ')
			with open('{0}{1}bin{1}{2}'.format(os.getcwd(), os.sep, cmd[1]), 'wb') as file:
				self.ftp.retrbinary('RETR {}'.format(cmd[1]), file.write)
		
		else:
			print('Command not found')
	
	def get_size(self, filename):
		self.ftp.voidcmd('TYPE I')
		return self.ftp.size(filename)
			
	def clear_return_value(self):
		self.return_value = None