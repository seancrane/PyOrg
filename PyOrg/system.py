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
    __logger = logging.getLogger("pyorg_logger")
    __source_directory = ""
    __destination_directory = ""

    def __init__(self, source_directory, destination_directory):
        self.__source_directory = source_directory
        self.__destination_directory = destination_directory
        self._files= listdir(getcwd())
        self.__traverse_files()
        #print(self._directories)

    def __traverse_files(self):
        count = 0
        for root,directories,files in walk(self.__source_directory):
            for filename in files:
                file_dir = join(root,filename)
                __strat = Strategy(file_dir, self.__destination_directory)
