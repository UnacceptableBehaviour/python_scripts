#! /usr/bin/env python
# 3.7
# create MD for TOC


import os
import re
from pprint import pprint

def create_toc_link_text(title):
    
    # downcase, remove all non alphanumeric, replace spave with hyphen
    
    return title.lower()
    


def create_TOC_from_text(text):
    
    
    replacement = ''
    
    # how to enumerate - replacement with a tag? for later returning snippet?
    # remove code snippets
    text_lite = re.sub(r'^```.*?```', replacement, text, flags = re.MULTILINE | re.DOTALL)
    
    #    - match for one or more # and title
    collect_toc_lines = re.findall(r'^(#+)(.*?)$', text_lite, flags = re.MULTILINE | re.DOTALL)
    
    #text_lite = re.sub(r'^#.*?$', replacement, text, flags = re.MULTILINE | re.DOTALL)
    #text_lite = re.sub(r'#', '@', text, flags = re.MULTILINE | re.DOTALL)
    print('\n\n> found - - - - S')
    for m in collect_toc_lines:
        print(f"\n\n[{m[1].strip()}](#{create_toc_link_text(m[1])})")
        pprint(m)
    print('> found - - - - E')

    #print(text_lite)


def get_mark_down(filename='context.md'):
        
    with open(filename) as f:
        content = f.read()

    for line in iter(content.splitlines()):
        print(line)
    
    print("\n\n\n\n\n\n")
    
    return content        
    
    
if __name__ == '__main__':
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    
    print(f"PWD: {os.getcwd()}")

    text = get_mark_down()
    
    print(type(text))
    
    create_TOC_from_text(text)