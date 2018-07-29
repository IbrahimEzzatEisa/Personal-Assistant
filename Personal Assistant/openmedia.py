import subprocess
import webbrowser
import os
import sys
from filesearch import FileSearch

# ///////////////////////////////////////////////
# open media

class OpenMedia :
    def openFile(self,path):
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, path])
