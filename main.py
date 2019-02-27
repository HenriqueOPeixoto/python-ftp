import sys
import terminal
import ftp_server
import ftp_client

def main():
	
	# Instantiates the Terminal class which handles user interaction and does
	# initial setup
	display = terminal.Terminal()
	
	display.display_startup_sequence()
	is_server = display.ask_if_server()
	
	if is_server == True:
		
		user = display.display_server_config_sequence()
		
		# The server receives a user account in order to initialize
		server = ftp_server.FTPServer(user)
		
		print('\nThe server will start. In order to shut it down use Ctrl-C (NT) or Ctrl-D (POSIX)\n')
		
		server.start_server()
		
	else:
		
		print('This is still under implementations and may be broken\n')
		
		# Initializes the client config sequence and receives the host object
		host = display.display_client_config_sequence()
		
		# Instantiates a client object that automatically connects to a host
		client = ftp_client.FTPClient(host)
		
		while True:
			print(client.ftp.pwd())
			cmd = display.get_user_input()
			
			# Sometimes, a command might return a statement
			client.execute_cmd(cmd)
			listener = client.get_return_value()
			print('\n')
			if listener == 'exit':
				break
			elif listener == 'help':
				display.display_help_message()
				client.clear_return_value()
			listener = ''
			print('\n')

if __name__ == '__main__':
	main()