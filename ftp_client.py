import ftplib
import host

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
			self.ftp.cwd(cmd[1])
		
		elif cmd.startswith('SIZE'):
			cmd = cmd.split(' ')
			self.ftp.voidcmd('TYPE I')
			print('{} bytes'.format(self.ftp.size(cmd[1])))
		
		elif cmd == 'HELP':
			with open('help.txt', 'r') as help_file:
				line_index = 0
				for line in help_file:
					# This is for hiding the help header
					if line_index <= 3:
						line_index += 1
					else:
						print(line, end='')
		
		else:
			print('Command not found')