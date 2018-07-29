import subprocess
import webbrowser
import os
import sys
from filesearch import FileSearch

# ///////////////////////////////////////////////
# open media

file=FileSearch().search('workout')
# path = r'/home/abdo/Downloads/Edward Bullen - Building a ChatBot with Python, NLTK and scikit.mp4'

opener = "open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, file[0]])
print('inaodsndioasn')


# ////////////////////////////////////
# how to open website by python
address='http://google.com/#q='
requiredAddress=address+raw_input()
webbrowser.open(requiredAddress)
print("done")


# /////////////////////////////////////////////////
#how to run program in terminal

proc = subprocess.Popen('google-chrome', stdout=subprocess.PIPE)

proc.stdout.read()

# //////////////////////////////////////////////////
# list all file in the system
type(os.system('ls /usr/share/applications'))