# python-ftp v1.0.0
This project allows users to host or access an FTP server. 

# How to use
Setting up a server is pretty straight forward. Just follow the on-screen prompts and the server should be up and running. The client part, however, is a little bit more complicated. See "help.txt" or type "help" on the command line for more information.

# Setting up virtual environment
Use the command: 

	virtualenv -p python[version] venv
The version used in this project is 3.6.5.
To activate it, use:

	source venv/Scripts/activate

# Setting up library dependencies
Use the command (with your virtual environment activated):
	
	pip install -r requirements.txt
	
# How to build
If you wish to build an executable for yourself, set up your virtual environment and activate it, then download PyInstaller from pip (if you downloaded from "requirements.txt" you can skip this step)
	
	pip install pyinstaller
All that's left to do is the build itself. For this, use the command (Windows):

	pyinstaller --clean -n python-ftp --add-data "help.txt;." --add-data "LICENSE;." __main__.py
On most Unix systems, the command below should work:
	
	pyinstaller --clean -n python-ftp --add-data "help.txt:." --add-data "LICENSE:." __main__.py

# Warning:
This program doesn't use any encryption methods for storing passwords or
transfering files safely yet. Use it on safe and private environments only.
