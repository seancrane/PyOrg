from os import listdir
from os import chdir
from os import getcwd
from os import walk
from os.path import isdir
from os.path import join
from mutagen.mp3 import MP3
from strategy import Strategy
import logging

class System:
    _logger = logging.getLogger("pyorg_logger")
    _directories = ""

    def __init__(self):
        self._files= listdir(getcwd())
        self.__traverse_files()
        #print(self._directories)

    def __traverse_files(self):
        count = 0
        for root,directories,files in walk('set directory'):
            for filename in files:
                file_dir = join(root,filename)
                __strat = Strategy(file_dir)
