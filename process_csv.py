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
import csv
import itertools


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


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# load a csv file into a list of dictionaries
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def get_csv_as_dictionary(csv_data_file):

    dict_of_days = {}
    # { 'weekday': { 'FAT delta': [1,2,3,-1,etc],
    #                'H2O delta': [[1,2,3,-1,etc]] }
    # }
    
    weekdays = [ 'Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']    

    for day in weekdays:
        dict_of_days[day] = {'FAT delta':[],
                             'H2O delta':[]}
        

    with open(csv_data_file) as csv_to_dict_file:    
        csv_reader = csv.DictReader(csv_to_dict_file, delimiter=',')        
        logging.debug(f"TYPE: csv_reader {type(csv_reader)}")    
                
        for row in csv_reader:
            
            logging.debug(f"\n\nTYPE: row {type(row)}")    
            logging.debug(row)
            
            #[('Day', 'Saturday') ('FAT delta', '0.6'), ('H2O delta', '-0.7')]
            logging.debug(row['Day'])
            logging.debug(row['FAT delta'])
            logging.debug(row['H2O delta'])
            
            dict_of_days[row['Day']]['FAT delta'].append(row['FAT delta'])            
            dict_of_days[row['Day']]['H2O delta'].append(row['H2O delta'])
            
            #for col_key in csv_reader.fieldnames:                
            #    entry[col_key] = row[col_key]   # create and info dictionary    
    
            #sql_dict[entries] = entry
            
            #entries +=1

        
    logging.debug("----- reponse ------------------------------------------------------------")
    
    for day in dict_of_days:
        #low_val = min()
        print(f">> {day} >")
        dict_of_days[day]['FAT delta'] = list(filter(None, dict_of_days[day]['FAT delta']))  # strip out blanks
        dict_of_days[day]['H2O delta'] = list(filter(None, dict_of_days[day]['H2O delta']))
        
        dict_of_days[day]['FAT delta'] = [float(x) for x in dict_of_days[day]['FAT delta']] # convert to ints
        dict_of_days[day]['H2O delta'] = [float(x) for x in dict_of_days[day]['H2O delta']]
        
        fd = dict_of_days[day]['FAT delta']
        hd = dict_of_days[day]['H2O delta']

        low_val_F = min(fd)
        hi_val_F = max(fd)
        av_val_F = sum(fd) / len(fd)
        low_val_H = min(hd)
        hi_val_H = max(hd)
        av_val_H = sum(hd) / len(hd)

        print(f"FAT delta {low_val_F}".ljust(20) + f"< {av_val_F} >".ljust(10) + f"{hi_val_F}")
        print(f"H2O delta {low_val_F}".ljust(20) + f"< {av_val_F} >".ljust(10) + f"{hi_val_F}")
                    

    logging.debug(f">---------------------------------------- DICTIONARY LOADED >------------")

    return dict_of_days



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
    #display_csv_data_to_console()
    
    get_csv_as_dictionary(csv_data_file)
