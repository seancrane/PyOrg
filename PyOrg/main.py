#!/bin/python
import logging
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from system import System

class Main:
    __parser = ""
    __args = ""
    __logger_choices = ['CRITICAL','ERROR','WARNING','INFO','DEBUG','NOTSET']
    __system_choices = ['ipod']
    __logger = logging.getLogger("pyorg_logger") 
    _file_handler = logging.FileHandler("pyorg.log", delay=False)

    def __init__(self):
       self.__logger.setLevel(logging.INFO)
       self.__logger.addHandler(self._file_handler)
       self.__parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
       self.__add_args()
       self.__handle_args()
    
    def __add_args(self):
        self.__parser.add_argument("-l", help="turn on logger and set logging level", choices=self.__logger_choices) 
        self.__parser.add_argument("-v", "--version", help="display current PyOrg version.", action="store_true")
        self.__parser.add_argument("-s", "--system", help='Traverse a directory structure.', required=False, choices=self.__system_choices)
        self.__args = self.__parser.parse_args()

    def __handle_args(self):
       if self.__args.version:
            print("PyOrg 0.0.1 (May 21 2014, 21:57:00)")
       self.__handle_logger_args() 
       self.__handle_system_args()

    def __handle_logger_args(self):    
        if self.__args.l == "CRITICAL":
            self.__logger.setLevel(logging.CRITICAL)
        if self.__args.l == "ERROR":
            self.__logger.setLevel(logging.ERROR)
        if self.__args.l == "WARNING":
            self.__logger.setLevel(logging.WARNING)
        if self.__args.l == "INFO":
            self.__logger.setLevel(logging.INFO)
        if self.__args.l == "DEBUG":
            self.__logger.setLevel(logging.DEBUG)
        if self.__args.l == "NOTSET":
            self.__logger.setLevel(logging.NOTSET)
       
    def __handle_system_args(self):
        if self.__args.system == "ipod":
            pyorg = System()
        
if __name__ == "__main__":
    py_org_main = Main()
