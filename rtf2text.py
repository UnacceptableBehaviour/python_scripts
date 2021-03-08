#! /usr/bin/env python

# YOMU is uber slow & requires JDK
#
# build gem port of striprtf
#
# in the mean time hack a quick script together to convert rtf to text

from pathlib import Path
import sys
from pprint import pprint

# RTF conversion to text
from striprtf.striprtf import rtf_to_text

def get_text_content_of_file(rtf_filepath):
    
    with open(rtf_filepath,'r') as f:
        rtf = f.read()
    # print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - S')
    # print(rtf)
    # print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - E')        
    return rtf_to_text(rtf)             # convert to text and return


def main():
    pass

if __name__ == '__main__':
    
    file_to_read = sys.argv[1]
    # pprint(sys.argv)
    # pprint(file_to_read)
    # print(f"FILE EXISTS? [{Path(file_to_read).exists()}]")
    if Path(file_to_read).exists():        
        text = get_text_content_of_file(file_to_read)
        print(text)
    