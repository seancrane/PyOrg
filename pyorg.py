#!/bin/python
import logging
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from os import listdir
from os import chdir
from os import getcwd
from mutagen.mp3 import MP3

#audio = MP3("angel.mp3")
class System:
    _directories = ""
    logging.basicConfig(filename="pyorg.log", level=logging.DEBUG)

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

class PyOrgArguments:
    _parser = ""
    _subparser = ""
    _args = ""
    def __init__(self):
       self._parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
       self._add_args()
       self._handle_args()
    
    def _add_args(self):
        self._parser.add_argument("-v", "--version", help="display current PyOrg version.", action="store_true")
        self._parser.add_argument("-s", "--system",required=False, help='Traverse a directory structure. \nSYSTEM(s):\n   ipod - traverse ipod directory structure')
        self._args = self._parser.parse_args()

    def _handle_args(self):
        if self._args.system == "ipod":
            pyorg = Ipod()
        if self._args.version:
            print("PyOrg 0.0.1 (May 21 2014, 21:57:00)")

if __name__ == "__main__":
    _py_org_main = PyOrgArguments()
 
#audio = MP3("AFKF.mp3")
#test = audio.pprint()
#title = audio["TIT2"]
#print(test)
#print(title)
