#!/bin/python
import logging
import ConfigParser
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from sys import exit
from system import System

class Main:
    __parser = ""
    __args = ""
    __config = ConfigParser.ConfigParser()
    __logger = logging.getLogger("pyorg_logger") 
    __logger.propagate = False
    __file_handler = logging.FileHandler("pyorg.log", delay=False)

    def __init__(self):
       self.__logger.setLevel(logging.INFO)
       self.__file_handler.setLevel(logging.INFO)
       self.__logger.addHandler(self.__file_handler)
       self.__parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

       self.__logger.debug("Loading config file")
       # Read config file.
       try:
            self.__config.read('pyorg.cfg')
       except:
            print("Config file not found. Please place pyorg.cfg in correct location")
            self.__logger.critical("Config file not found.  Please place pyorg config in correct location")
            sys.exit(0)
               
       # Setup the logger level. 
       self.__logger.debug("Setting logger level")
       self.__set_logger()    

       # Handle command line arguments.
       self.__handle_args()
    
    def __evaluate_logger_level(self, __logger_level):
        if __logger_level < 0:
            __logger_level = 0
        elif __logger_level > 0 and __logger_level < 11:
            __logger_level = 10
        elif __logger_level > 10 and __logger_level < 21:
            __logger_level = 20
        elif __logger_level > 20 and __logger_level < 31:
            __logger_level = 30
        elif __logger_level > 30 and __logger_level < 41:
            __logger_level = 40
        elif __logger_level > 40 and __logger_level < 51:
            __logger_level = 50
        else:
            __logger_level = 50
    
        return __logger_level

    def __set_logger(self):
        #Get the logger level from pyorg.cfg. 
        try:
            __logger_level = self.__config.getint("Logger", "Level")
        except:
            self.__logger.critical("Invalid logger level provided in the config file. Setting default value to INFO (20).")
            __logger_level = logging.INFO            

        self.__logger.info("Setting the logger level")
        self.__logger.setLevel(self.__evaluate_logger_level(__logger_level))          

    def __add_args(self):
        self.__parser.add_argument("-v", "--version", help="display current PyOrg version.", action="store_true")
        self.__args = self.__parser.parse_args()

    def __start_system(self):
        try:
            __source_directory = self.__config.get("SourceFiles", "Files")
        except:
            self.__logger.critical("Invalid source file directory. Please set a correct directory in pyorg.cfg")
            print("Invalid source file directory. Please set a correct directory in pyorg.cfg")
            sys.exit(0)

        print("Setting source directory to: " + __source_directory)
        self.__logger.info("Setting source directory to: " + __source_directory)

        try:
            __destination_directory = self.__config.get("DestinationFiles", "Files")
        except:
            self.__logger.critical("Invalid destination file directory. Please set a correct directory in pyorg.cfg")
            print("Invalid destination file directory. Please set a correct directory in pyorg.cfg")
            sys.exit(0)

        print("Setting destination directory to: " + __destination_directory)
        self.__logger.info("Setting destination directory to: " + __source_directory)

    def __handle_args(self):
       self.__add_args()
       self.__start_system()
       if self.__args.version:
            print("PyOrg 0.0.1 (May 21 2014, 21:57:00)")
         
if __name__ == "__main__":
    py_org_main = Main()
