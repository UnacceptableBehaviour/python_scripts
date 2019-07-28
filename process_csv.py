#! /usr/bin/env python

# process csv data display in chart?

# import os                   # chdir(dir), getcwd
# import subprocess           # subprocess.run(command, arg)
# import re                   # regular expresions
# import json                 # json parsing
# 
# import glob                 
# from pprint import pprint   # giza a look
# 
from pathlib import Path    # working with paths - # https://docs.python.org/3/library/pathlib.html
import logging              # include various levels of debugging - https://docs.python.org/3/howto/logging.html


# csv data
csv_data_file = Path("./scratch/__2019.csv")

# create directory (and subdirectory if NO exist)    
local_scratch_dir = Path("./scratch/")
local_scratch_dir.mkdir(parents=True, exist_ok=True)

# = = LOGGING COOKBOOK: https://docs.python.org/3/howto/logging-cookbook.html
# configure basic logging - create new file each time
#logging.basicConfig(filename='scratch/process_csv.log', filemode='w', level=logging.INFO, format='%(asctime)s %(message)s')

# levels lowest to highest: DEBUG, INFO, WARNING, ERROR, CRITICAL
# logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')   # add time & date info

logging.basicConfig(level=logging.DEBUG)   # set level
#logging.basicConfig(level=logging.INFO)   # set level
#logging.basicConfig(level=logging.WARNING)   # set level
#logging.basicConfig(level=logging.ERROR)   # set level
#logging.basicConfig(level=logging.CRITICAL)   # set level

logging.info("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
logging.info(f"Logging to: {local_scratch_dir}")
logging.info("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
logging.debug("- - - - - - - - - - DEBUG <")
logging.info("- - - - - - - - - - -INFO <")
#logging.warning("- - - - - - - - - WARNING <")
#logging.error("- - - - - - - - - - ERROR <")
#logging.critical("- - - - - - - - -CRITICAL <")





def display_csv_data_to_console(csv):
    logging.debug("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    logging.debug("CSV data raw:")
    logging.debug("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")


    
    logging.debug("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")



    
if __name__ == '__main__':
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    display_csv_data_to_console()
