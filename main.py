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
			cmd = display.get_user_input()
			listener = client.execute_cmd(cmd)
			print('\n')
			if listener == 'exit':
				break

if __name__ == '__main__':
	main()