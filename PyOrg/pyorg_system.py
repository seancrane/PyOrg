from os import listdir
from os import chdir
from os import getcwd
from mutagen.mp3 import MP3
import logging

class System:
    _logger = logging.getLogger("pyorg_logger")
    _directories = ""

class Ipod(System):
    def __init__(self):
        self._directories = listdir(getcwd())
        print(self._directories)

    def traverse_directories(self):
        for i in self._directories:
            try:
                chdir(i)
            except:
                files = listdir(getcwd())

#audio = MP3("angel.mp3")
#audio = MP3("AFKF.mp3")
#test = audio.pprint()
#title = audio["TIT2"]
#print(test)
#print(title)
