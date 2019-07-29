#! /usr/bin/env python
# 3.7
# process csv data display in chart?


from pathlib import Path    # working with paths - # https://docs.python.org/3/library/pathlib.html
import logging              # include various levels of debugging - https://docs.python.org/3/howto/logging.html
import csv
import itertools


# csv data
csv_data_file = Path("./scratch/__2019.csv")    # large
#csv_data_file = Path("./data/__2019.csv")      # test data

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
# load csv file extract fat and water delta information
#   list by day Sun-Sat Min, average, max for each
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def get_max_av_min_for_fat_and_water_delts_by_day(csv_data_file):

    dict_of_days = {}
    # { 'weekday': { 'FAT delta': [1,2,3,-1,etc],
    #                'H2O delta': [[1,2,3,-1,etc]] }
    # }
    
    weekdays = [ 'Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']    

    for day in weekdays:
        dict_of_days[day] = {'FAT delta':[],        # store fat delta data as list for each day
                             'H2O delta':[]}        # same for water
        

    with open(csv_data_file) as csv_to_dict_file:    
        csv_reader = csv.DictReader(csv_to_dict_file, delimiter=',')        # import csv 
        logging.debug(f"TYPE: csv_reader {type(csv_reader)}")    
                
        for row in csv_reader:
            
            logging.debug(f"\n\nTYPE: row {type(row)}")     # row <class 'collections.OrderedDict'>
            logging.debug(row)  #[('Day', 'Saturday') ('FAT delta', '0.6'), ('H2O delta', '-0.7')]
                        
            logging.debug(row['Day'])                       # DEBUG:root:Wednesday
            logging.debug(row['FAT delta'])                 # DEBUG:root:-0.4
            logging.debug(row['H2O delta'])                 # DEBUG:root:-0.1

            dict_of_days[row['Day']]['FAT delta'].append(row['FAT delta'])      # build lists
            dict_of_days[row['Day']]['H2O delta'].append(row['H2O delta'])
            
        
    logging.info("----- reponse ------------------------------------------------------------")
    
    for day in dict_of_days:
        print(f">> {day} >")
        
        fd = dict_of_days[day]['FAT delta']     # for readability
        hd = dict_of_days[day]['H2O delta']

        fd = list(filter(None, fd))             # strip out blanks
        hd = list(filter(None, hd))
        
        fd = [float(x) for x in fd]             # convert to floats
        hd = [float(x) for x in hd]
        

        low_val_F = min(fd)
        hi_val_F = max(fd)
        av_val_F = round(sum(fd) / len(fd),2)
        low_val_H = min(hd)
        hi_val_H = max(hd)
        av_val_H = round(sum(hd) / len(hd),2)

        print(f"FAT delta {low_val_F}".ljust(20) + f"< {av_val_F} >".ljust(10) + f"{hi_val_F}".rjust(10))
        print(f"H2O delta {low_val_H}".ljust(20) + f"< {av_val_H} >".ljust(10) + f"{hi_val_H}".rjust(10))
        print("\n")
                    

    logging.info(f">---------------------------------------- DICTIONARY LOADED >------------")

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
    
    dod = get_max_av_min_for_fat_and_water_delts_by_day(csv_data_file)
