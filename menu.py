# --------------------------------------------------
# menu.py
# Version: 1.0.0
# Last Updated: Sep 4th, 2022
# --------------------------------------------------

import nuke
import platform

# Define where .nuke directory is on each OS's network
Win_Dir = 'C:\Users\rtm\.nuke'
MacOSX_Dir = '/Users/Daria/.nuke'
Linux_Dir = '/home/dalexander/.nuke'

# Set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None

