#! /usr/bin/env python
# 3.7
# create MD for TOC


import os
import re
from pprint import pprint

def create_toc_link_text(title):
    
    # downcase, remove all non alphanumeric, replace space with hyphen
    toc_link_text = title.strip().strip("\\").lower()
    toc_link_text = re.sub(r'[^a-z 0-9]', '', toc_link_text)
    toc_link_text = re.sub(r' ', '-', toc_link_text)
    
    return toc_link_text

   
MAX_INDENT_DEPTH = 12
FRONT_OF_QUEUE = 0
INDENT_DEPTH = 0
LINK_LINE = 1

def create_indented_md_link_lines(link_tuples, indent=1):    
    if indent > MAX_INDENT_DEPTH: return
    
    toc_lines = []
    
    # create bullet numbering
    bullet = 1 
    
    while(len(link_tuples) > 0):
        print(f"INDENT:{indent} - len(link_tuples):{len(link_tuples)}")
        
        if( link_tuples[FRONT_OF_QUEUE][INDENT_DEPTH] == indent ):
            # pop it
            line = link_tuples.pop(FRONT_OF_QUEUE)
            
            # create toc line
            test ="*" * indent
            print(f"{indent} - {test} - {bullet}. {line}")
            toc_lines.append(f"{indent} - {test} - {bullet}. {line}")
            
            bullet += 1     # increment bullet number
            
        elif( link_tuples[FRONT_OF_QUEUE][INDENT_DEPTH] > indent ):
            # call this function to go to next level
            toc_lines.append( create_indented_md_link_lines(link_tuples, indent+1) )
        else:    
            # call this function to go to down a level
            toc_lines.append( create_indented_md_link_lines(link_tuples, indent-1) )

        
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
        
        md_href = f"[{m[1].strip()}](#{create_toc_link_text(m[1])})\\"
        
        links_with_no_of_indents.append( (len(m[0]),md_href) )
    
    pprint(links_with_no_of_indents)
    
    indented_md_hrefs = create_indented_md_link_lines(links_with_no_of_indents)
       
    return indented_md_hrefs 
    




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
    
    
    print("- - - - - - - - - -")
    create_TOC_from_text(text)