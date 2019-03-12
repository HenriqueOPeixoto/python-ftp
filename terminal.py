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

    def display_startup_sequence(self):

        print('python-ftp')
        print('---------------------------------')
        print('Version 0.9.1, by CodeArch')
        print('\n')

    def ask_if_server(self):

        print('Choose an option from below: ')
        print('\n')
        print('[1]: Server')
        print('[2]: Client')
        print('\n')
        print('Insert option: ', end='')

        while True:

            user_option = input()

            if user_option == '1':
                self.user.is_server = True
                break
            elif user_option == '2':
                self.user.is_server = False
                break
            else:
                print('Use [1] for Server and [2] for Client: ')

        return self.user.is_server

    def display_server_config_sequence(self):

        self.user.username = input('Insert username: ')
        self.user.password = input('Insert password: ')

        while True:

            try:
                self.user.dir_ = input('Insert directory to share: ')

                if os.path.isdir(self.user.dir_) is False:
                    raise NotADirectoryError from OSError
                break
            except NotADirectoryError:
                print('Error: Not a directory or directory not found')

        while True:
            access_level = input('Insert level of access ' +
                                 '(R for read/RW for Read/Write): ').upper()

            # Each character from the permissions variable allows a different
            # command to be executed. Check the pyftpdlib docs, to
            # understand what they do.
            # https://pyftpdlib.readthedocs.io/en/latest/

            if access_level == 'R':

                self.user.permissions = 'elr'
                break

            elif access_level == 'RW':

                self.user.permissions = 'elradfmwMT'
                break

        return self.user

    def display_client_config_sequence(self):

        address = input('Insert address (default = 0.0.0.0): ')

        if address == '':
            address = '0.0.0.0'

        while True:
            try:

                port = input('Insert port (default = 2121): ')

                if port == '':
                    port = 2121
                    break

                elif port.isdecimal():
                    port = int(port)
                    break

                else:
                    raise ValueError('The port is an integer number')

            except ValueError as error:
                print(error)

        username = input('Insert username (default = None): ')
        password = input('Insert password (default = None): ')

        self.host.address = address
        self.host.port = port
        self.host.username = username
        self.host.password = password

        return self.host

    def display_help_message(self):
        with open('help.txt', 'r') as help_file:
            line_index = 0
            for line in help_file:
                # The if statement below is here to skip the "help.txt"
                # file header which is only supposed to be seen in a
                # normal text editor
                if line_index <= 3:
                    line_index += 1
                else:
                    print(line, end='')

        print('\n')

    def get_arguments_with_quotes(self, cmd):

        quote_index_list = []
        args_list = []

        args_list.append(cmd.split(' ')[0].upper())

        for c in range(len(cmd)):
            if cmd.startswith('"', c):
                quote_index_list.append(c)

        for i in range(1, cmd.count('"'), 2):
            args_list.append(
                cmd[quote_index_list[i - 1] + 1:quote_index_list[i]])

        return args_list

    def get_user_input(self):

        cmd = input('> ')

        if '"' in cmd:
            cmd = self.get_arguments_with_quotes(cmd)
        else:
            cmd = cmd.split(' ')
            cmd[0] = cmd[0].upper()

        return cmd
