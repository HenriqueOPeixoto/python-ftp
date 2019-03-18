# Changelog v1.0.0
* Many exceptions are now handled and the program should only shut down
when it's actually necessary
* The code is now even more readable and many unecessary comments were removed

# Changelog v0.9.1
* The program now supports spaced arguments on the client side. That means
you can now interact with files that have whitespace on their directories (
by using quotes)

# Changelog v0.8.3
* Added STOR, DELE, RENAME, RMD and MKD commands
* The client side is now fully usable (still has some bugs, though)
* The server now allows file renaming

# Changelog v0.8.2-alpha
* Giving no or too many arguments on a CWD command now no longer exits the aplication
* New methods added to make the code easier to understand
* Added RETR and PWD commands

# Changelog v0.8.1-alpha
* Added more client commands (those are decribed in the "help.txt" file)
* Added "help.txt" file

# Changelog v0.7.2-alpha
* The code is now more organized and cleaner

# Changelog v0.7.1-alpha
* Server is now fully customizable
* It is now possible to connect to an FTP server and display its files