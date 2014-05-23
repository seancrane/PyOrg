#!/bin/python
import logging
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
import pyorg_system


class PyOrgArguments:

    _parser = ""
    _subparser = ""
    _args = ""
    _logger_choices = ['CRITICAL','ERROR','WARNING','INFO','DEBUG','NOTSET']
    _system_choices = ['ipod']
    _logger = logging.getLogger("pyorg_logger") 
    _file_handler = logging.FileHandler("pyorg.log", delay=False)

    def __init__(self):
       self._logger.setLevel(logging.INFO)
       self._logger.addHandler(self._file_handler)
       self._parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
       self._add_args()
       self._handle_args()
    
    def _add_args(self):
        self._parser.add_argument("-l", help="turn on logger and set logging level", choices=self._logger_choices) 
        self._parser.add_argument("-v", "--version", help="display current PyOrg version.", action="store_true")
        self._parser.add_argument("-s", "--system", help='Traverse a directory structure.', required=False, choices=self._system_choices)
        self._args = self._parser.parse_args()

    def _handle_args(self):
       if self._args.version:
            print("PyOrg 0.0.1 (May 21 2014, 21:57:00)")
       self._handle_logger_args() 
       self._handle_system_args()

    def _handle_logger_args(self):    
        if self._args.l == "CRITICAL":
            self._logger.setLevel(logging.CRITICAL)
        if self._args.l == "ERROR":
            self._logger.setLevel(logging.ERROR)
        if self._args.l == "WARNING":
            self._logger.setLevel(logging.WARNING)
        if self._args.l == "INFO":
            self._logger.setLevel(logging.INFO)
        if self._args.l == "DEBUG":
            self._logger.setLevel(logging.DEBUG)
        if self._args.l == "NOTSET":
            self._logger.setLevel(logging.NOTSET)
       
    def _handle_system_args(self):
        if self._args.system == "ipod":
            pyorg = pyorg_system.Ipod()
        

if __name__ == "__main__":
    _py_org_main = PyOrgArguments()
 

