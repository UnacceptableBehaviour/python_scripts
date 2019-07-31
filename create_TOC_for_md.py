#! /usr/bin/env python
# 3.7
# create MD for TOC


import os
import re
from pprint import pprint
import sys                          # argv
#from pprint import  pprint

def create_toc_link_text(title):
    
    # downcase, remove all non alphanumeric, replace space with hyphen
    toc_link_text = title.strip().strip("\\").lower()
    toc_link_text = re.sub(r'[^a-z 0-9]', '', toc_link_text)
    toc_link_text = re.sub(r' ', '-', toc_link_text)
    
    return toc_link_text


MAX_NO_CONTENT_ITEMS_PER_INDENT = 100   
MAX_INDENT_DEPTH = 12
FRONT_OF_QUEUE = 0
INDENT_DEPTH = 0
LINK_LINE = 1

def create_indented_md_link_lines(link_tuples, indent=1):    
    if indent > MAX_INDENT_DEPTH: return
    
    toc_lines = []    
    bullet = 1

    while(len(link_tuples) > 0):
        #print(f"INDENT:{indent} - len(link_tuples):{len(link_tuples)}")
        
        if( link_tuples[FRONT_OF_QUEUE][INDENT_DEPTH] == indent ):
            # pop it
            line = link_tuples.pop(FRONT_OF_QUEUE)
            
            # create toc line            
            tabs ="\t" * (indent - 1)
            print(f"{tabs}{bullet}. {line[LINK_LINE]}")
            toc_lines.append(f"{tabs}{bullet}. {line[LINK_LINE]}")            
            
            bullet += 1
            
            
        elif( link_tuples[FRONT_OF_QUEUE][INDENT_DEPTH] > indent ):
            # call this function to go to next level
            toc_lines.append( create_indented_md_link_lines(link_tuples, indent+1) )
        else:
            # return to go to down a level
            return toc_lines

        
    return toc_lines
    


def create_TOC_from_text(text):

    replacement = ''
    links_with_no_of_indents = []
    
    # how to enumerate - replacement with a tag? for later returning snippet?
    # remove code snippets
    text_lite = re.sub(r'^```.*?```', replacement, text, flags = re.MULTILINE | re.DOTALL)
    
                                    # match for one or more # and title
    collect_toc_lines = re.findall(r'^(#+)(.*?)$', text_lite, flags = re.MULTILINE | re.DOTALL)
    
    #print('\n\n> found - - - - S\n')
    for m in collect_toc_lines:
        #print(f"[{m[1].strip()}](#{create_toc_link_text(m[1])})\\")
        #print(m)
        
        md_href = f"[{m[1].strip()}](#{create_toc_link_text(m[1])})"
        
        links_with_no_of_indents.append( (len(m[0]) - 1,md_href) )
    
    links_with_no_of_indents.pop(0) # remove headline    
    
    indented_md_hrefs = create_indented_md_link_lines(links_with_no_of_indents)
       
    return indented_md_hrefs 
    



DEFAULT_FILE = 'context.md'

def get_mark_down(filename=DEFAULT_FILE):
        
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

    report = f"PWD: {os.getcwd()}"
    
    # sys.argv[0] is name of this file
    # prefer
    # import pathlib; Path(sys.argv[1]).exists()   # but since we've already imported os
    

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):  
        report += f"\nCreating TOC for {sys.argv[1]}"
        text = get_mark_down(sys.argv[1])
            
    else: 
        report += f"\n* * USING DEFAULT FILE * * - Creating TOC for {DEFAULT_FILE}"
        text = get_mark_down()
    
    print("- - - - - - - - - -")
    create_TOC_from_text(text)
    
    print(f"\n\n{report}")