import sys
import terminal
import ftp_server
import ftp_client


def main():

    display = terminal.Terminal()

    display.display_startup_sequence()
    is_server = display.ask_if_server()

    if is_server:

        user = display.display_server_config_sequence()

        server = ftp_server.FTPServer(user)

        print('\nThe server will start. In order to shut it down use Ctrl - C',
              '(NT) or Ctrl - D(POSIX)\n')

        server.start_server()

    else:

        host = display.display_client_config_sequence()
        client = ftp_client.FTPClient(host)

        while True:

            print(client.ftp.pwd())
            cmd = display.get_user_input()
            print('\n')
            client.execute_cmd(cmd)
            listener = client.get_return_value()

            if listener == 'exit':
                break
            elif listener == 'help':
                display.display_help_message()
                client.clear_return_value()
            listener = ''

            print('\n')


if __name__ == '__main__':
    main()
