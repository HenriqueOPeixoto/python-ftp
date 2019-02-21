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
		cmd = cmd.upper()
		if cmd == 'LIST':
			self.ftp.dir()
		elif cmd == 'EXIT':
			self.return_value = 'exit'
		else:
			print('Command not found')