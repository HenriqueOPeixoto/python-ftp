import ftplib
import host
import os


class FTPClient:

    username = None
    password = None
    host = None
    ftp = None
    return_value = None

    def __init__(self, host):

        if os.path.isdir('{0}{1}bin{1}'.format(os.getcwd(), os.sep)) is False:
            os.mkdir('{0}{1}bin{1}'.format(os.getcwd(), os.sep))

        self.ftp = ftplib.FTP()
        self.host = host

        self.ftp.connect(host.address, host.port)
        self.ftp.login(host.username, host.password)

    def get_return_value(self):
        return self.return_value

    def clear_return_value(self):
        self.return_value = None

    def get_size(self, cmd):
        try:
            # The command below ensures binary mode is used in order to
            # get size. It cannot be used in folders.
            self.ftp.voidcmd('TYPE I')
            size = self.ftp.size(cmd[1])
            print('{} bytes'.format(size))
        except ftplib.error_perm as e:
            print(e)
        except IndexError:
            print('SIZE command takes 1 argument. {} were given'.format(
                  (len(cmd) - 1)))
                  
    def change_directory(self, cmd):
        try:
            self.ftp.cwd(cmd[1])
        except IndexError:
            print(
                'Error: CWD takes 1 argument only. {} were given'.format(
                    len(cmd) - 1))
        except ftplib.error_perm as e:
            print(e)

    def retrieve_file(self, cmd):
        try:
            with open('{0}{1}bin{1}{2}'.format(os.getcwd(), os.sep, cmd[1]),
                      'wb') as file:
                self.ftp.retrbinary('RETR {}'.format(cmd[1]), file.write)
        except ftplib.error_perm as e:
            os.remove('{0}{1}bin{1}{2}'.format(os.getcwd(), os.sep, cmd[1]))
            print(e)
        except IndexError:
            print('RETR command takes 1 argument. {} were given.'.format(
                  (len(cmd) - 1)))
        
    def store_file_on_server(self, cmd):
        try:
            with open(cmd[1], 'rb') as file:
                self.ftp.storbinary('STOR {}'.format(cmd[2]), file)
        except (ftplib.error_perm, FileNotFoundError) as e:
            print(e)
        except IndexError:
            print('STOR command takes 2 arguments. {} were given'.format(
                  (len(cmd) - 1)))
                  
    def delete_file(self, cmd):
        try:
            self.ftp.delete(cmd[1])
        except ftplib.error_perm as e:
            print(e)
        except IndexError:
            print('DELE takes 1 argument. {} were given.'.format(
                  (len(cmd) - 1)))
                  
    def create_directory(self, cmd):
        try:
            self.ftp.mkd(cmd[1])
        except ftplib.error_perm as e:
            print(e)
        except IndexError:
            print('MKD takes 1 argument. {} were given'.format(
                  (len(cmd) - 1)))

    def remove_directory(self, cmd):
        try:
            self.ftp.rmd(cmd[1])
        except ftplib.error_perm as e:
            print(e)
        except IndexError:
            print('RMD takes 1 argument. {} were given'.format(
                  (len(cmd) - 1)))
    
    def rename_file_or_directory(self, cmd):
        try:
            self.ftp.rename(cmd[1], cmd[2])
        except ftplib.error_perm as e:
            print(e)
        except IndexError:
            print('RENAME takes 2 arguments. {} were given'.format(
                  (len(cmd) - 1)))
                  
    def execute_cmd(self, cmd):

        if cmd[0] == 'LIST':
            self.ftp.dir()

        elif cmd[0] == 'EXIT' or cmd[0] == 'QUIT':
            self.ftp.quit()
            self.return_value = 'exit'

        elif cmd[0] == 'CWD':
            self.change_directory(cmd)

        elif cmd[0] == 'SIZE':
            self.get_size(cmd)

        elif cmd[0] == 'HELP':
            self.return_value = 'help'

        elif cmd[0] == 'PWD':
            print(self.ftp.pwd())

        elif cmd[0] == 'RETR':
            self.retrieve_file(cmd)

        elif cmd[0] == 'MKD':
            self.create_directory(cmd)

        elif cmd[0] == 'RMD':
            self.remove_directory(cmd)

        elif cmd[0] == 'RENAME':
            self.rename_file_or_directory(cmd)

        elif cmd[0] == 'DELE':
            self.delete_file(cmd)

        elif cmd[0] == 'STOR':
            self.store_file_on_server(cmd)

        else:
            print('Command not found')
