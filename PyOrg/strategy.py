from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.flac import FLAC
from os.path import splitext
import logging
import eyed3


class Strategy():
    __path = ""
    __file_name = ""
    __extension = ""
    __destination_directory = ""  

    def __init__(self, file_path, destination_directory):
        self.__path = file_path
        self.__extract_filename(file_path)
        self.__destination_directory = destination_directory

        if self.__extension == ".mp3":
            __strategy = Mp3(self.__path)
        if self.__extension == ".m4a" or self.__extension == ".m4p":
            __strategy = Mp4(self.__path)
        #if self.__extension == ".flac":
        #    __strategy = Flac(__file_name)

    def __extract_filename(self, file_path):
        self.__file_name, self.__extension = splitext(file_path)
    
class Format():
    __logger = logging.getLogger("pyorg_logger")
    __title = ""
    __artist = ""
    __track = ""
    __album = ""
    __audio = ""
    

class Mp3(Format):
    __logger = logging.getLogger("pyorg_logger")

    __test_path = ""
    def __init__(self,__path):
        self.__test_path = __path
        self.__audio = MP3(__path)
        self.__getInfo()
    
    def __getInfo(self):
        #try:
            self.__artist = self.__audio["TPE1"]
            self.__title = self.__audio["TIT2"]
            self.__album = self.__audio["TALB"]
            self.__track = self.__audio["TRCK"]
        #except:

class Mp4(Format):
    def __init__(self,__path):
        self.__test_path = __path
        self.__audio = MP4(__path)
        self.__getInfo()
    
    def __getInfo(self):
        #try:
            self.__artist = self.__audio["\xa9ART"]
            self.__title = self.__audio["\xa9nam"]
            self.__album = self.__audio["\xa9alb"]
            self.__track = self.__audio["trkn"]
            print(self.__artist)
        #except:
