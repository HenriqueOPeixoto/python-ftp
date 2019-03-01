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

        # Creates a bin folder to store downloaded files
        if os.path.isdir('{0}{1}bin{1}'.format(os.getcwd(), os.sep)) is False:
            os.mkdir('{0}{1}bin{1}'.format(os.getcwd(), os.sep))

        # Instantiates a blank FTP Server connection
        self.ftp = ftplib.FTP()

        # Receives host data (address, username and password) that's passed as
        # an argument
        self.host = host

        # Connects to the host
        self.ftp.connect(host.address, host.port)

        # Logs into the server
        self.ftp.login(host.username, host.password)

    # Allows main.py to receive relevant information about the program
    # executions
    def get_return_value(self):
        return self.return_value

    # Checks if there aren't any errors in the command and executes them
    def execute_cmd(self, cmd):

        print('\n')

        # This is for separating the command from it's arguments
        # cmd[0] is the command and cmd[> 0] are it's arguments
        cmd = cmd.split(' ')
        cmd[0] = cmd[0].upper()

        if cmd[0] == 'LIST':
            self.ftp.dir()

        elif cmd[0] == 'EXIT' or cmd[0] == 'QUIT':
            self.ftp.quit()
            self.return_value = 'exit'

        elif cmd[0] == 'CWD':

            try:
                if len(cmd) == 2:
                    self.ftp.cwd(cmd[1])
                else:
                    raise IndexError
            except IndexError:
                print(
                    'Error: CWD takes 1 argument only. {} were given'.format(
                        len(cmd) - 1))

        elif cmd[0] == ('SIZE'):
            print('{} bytes'.format(self.get_size(cmd[1])))

        elif cmd[0] == 'HELP':
            self.return_value = 'help'

        elif cmd[0] == 'PWD':
            print(self.ftp.pwd())

        elif cmd[0] == 'RETR':
            with open('{0}{1}bin{1}{2}'.format(os.getcwd(), os.sep, cmd[1]),
                      'wb') as file:
                self.ftp.retrbinary('RETR {}'.format(cmd[1]), file.write)

        elif cmd[0] == 'MKD':
            self.ftp.mkd(cmd[1])

        elif cmd[0] == 'RMD':
            self.ftp.rmd(cmd[1])

        elif cmd[0] == 'RENAME':
            self.ftp.rename(cmd[1], cmd[2])

        elif cmd[0] == 'DELE':
            self.ftp.delete(cmd[1])

        elif cmd[0] == 'STOR':
            with open(cmd[1], 'rb') as file:
                self.ftp.storbinary('STOR {}'.format(cmd[2]), file)

        else:
            print('Command not found')

    def get_size(self, filename):
        # The command below is here to ensure binary mode is used in order to
        # get size
        self.ftp.voidcmd('TYPE I')
        return self.ftp.size(filename)

    def clear_return_value(self):
        self.return_value = None
