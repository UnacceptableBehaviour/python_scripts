#!/usr/bin/env python3

import subprocess
from pprint import pprint
import os
import sys


print('finding repos . . .')
repos_root = '../..'
os.chdir(repos_root)
command = "find . -type d -path '*/.git' -prune"
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
paths, error = process.communicate()
paths = paths.decode('utf-8')

repo_merged_summary = True

if '-p' in sys.argv:
    paths = sys.argv[sys.argv.index('-p') + 1]
    print(f"Using paths: {paths}")
    repo_merged_summary = False


def get_commit_count(repo_path, year, start_month, num_months):
    start_year = end_year = year
    #print(f"get_commit_count: {repo_path}, {start_month}, {num_months}")

    end_month = start_month + num_months
    if end_month > 12:
        end_year += 1
        end_month -= 12

    command = f"git log --since {start_year}-{start_month}-1 --until {end_year}-{end_month}-1 --pretty=oneline | wc -l"    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, cwd=repo_path)
    no_of_commits, error = process.communicate()
    no_of_commits = int(no_of_commits.decode('utf-8').strip())
    #print(f"Com#:{no_of_commits} - C: {command}")

    return no_of_commits

def get_commit_date_comment_and_files(repo_path, year, start_month, num_months):
    start_year = end_year = year
    #print(f"get_commit_count: {repo_path}, {start_month}, {num_months}")

    end_month = start_month + num_months
    if end_month > 12:
        end_year += 1
        end_month -= 12

    command = f"git log --since {start_year}-{start_month}-1 --until {end_year}-{end_month}-1 --pretty=format:'%cd - %h  > %s' --date=short --name-only"    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, cwd=repo_path)
    info_txt, error = process.communicate()
    info_txt = info_txt.decode('utf-8')
    #print(f"Com#:{info_txt} - C: {command}")

    return info_txt

active_repos = {}

# show number of commits by repo
for repo_path in paths.split('\n'):
    # cd into repo_path    
    repo_path = repo_path.strip().replace('/.git', '')
    if not repo_path:  # skip empty lines
        continue

    no_of_commits = get_commit_count(repo_path, 2023, 1, 12)    # TODO pass year in as option -y 2025
        
    if no_of_commits > 0:
        print(f"{no_of_commits:<4} commits {repo_path}")
        active_repos[repo_path] = { 'total_commits': no_of_commits } 

# remove mysql_python_flask_1_deprecated key active_repos - noise
                                # None - stops it raising Error if ke not found
active_repos.pop('./python/mysql_python_flask_1_deprecated', None) 

if '-sp' in sys.argv:   # show paths
    #print(paths)
    sys.exit(0)

longest_repo_name = 0
for repo_path in active_repos.keys():
    if len(repo_path) > longest_repo_name:
        longest_repo_name = len(repo_path)    

# show number of commits each month by repo
def print_repo_12_month_summary_bars(repo_path):
    print(f">-: {repo_path} - - - -")
    for i, c in enumerate(active_repos[repo_path]['commits']):
        print(f"{i+1:02}: {c:<4} {'#' * c}")
    print(f"> - - - - - - - - - - - -\n")


def build_repo_data(get_commit_count, get_commit_date_comment_and_files, active_repos, year=2023):

    for repo_path in active_repos.keys():
        commits = []
        commit_detail = []

        for start_month in range(1, 13):
            no_of_commits = get_commit_count(repo_path, year, start_month, 1)
            commits.append(no_of_commits)
        
            if no_of_commits > 0:
                commit_txt = get_commit_date_comment_and_files(repo_path, year, start_month, 1)
                commit_detail.append(commit_txt)
            else:
                commit_detail.append('')
    
        active_repos[repo_path]['commits'] = commits
        active_repos[repo_path]['commit_detail'] = commit_detail


def print_repo_summary_and_detail(repo_path):
    
    print('\n\n')
    print('- ' * 40)
    print(f" > > > {repo_path} < < <")
    print('- ' * 40)

    print_repo_12_month_summary_bars(repo_path)

    print(f"\n\n= = = {repo_path} = = =")
    for month in range(1, 13):
        no_of_commits = active_repos[repo_path]['commits'][month-1]
        if no_of_commits > 0:            
            #print('- ' * 40 + f"Month: {month:02}")    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            print((f"{month:02}: {repo_path:<{longest_repo_name+1}} ").ljust(80, '-') + f" Month: {month:02}")

            print(f"{month:02}: {no_of_commits:<4} {'#' * no_of_commits}")
            commit_txt = active_repos[repo_path]['commit_detail'][month-1]
            print(commit_txt)
            #git log --since '2023-11-01' --until '2024-01-01' --pretty=format:'%cd - %h  > %s' --date=short --name-only
            # git log --since '11/01/2023' --until '01/01/2024' --oneline --name-only


def print_all_repo_summaries():
    for repo_path in active_repos.keys():
        print_repo_summary_and_detail(repo_path)
        




print('- ' * 60)
print('- ' * 60)

# enumerate list w/ index and value
def print_merged_summary_all_repos_over_12_months()  :
    # longest_repo_name = 0
    # for repo_path in active_repos.keys():
    #     if len(repo_path) > longest_repo_name:
    #         longest_repo_name = len(repo_path)    

    for m in range(1, 13):
        print('- ' * 40 + f"Month: {m:02}")
        for repo_path in active_repos.keys():
            c = active_repos[repo_path]['commits'][m-1]
            print(f"{m:02}: {repo_path:<{longest_repo_name+1}} {'#' * c}")


build_repo_data(get_commit_count, get_commit_date_comment_and_files, active_repos)
    
print_all_repo_summaries()

if repo_merged_summary:
    print_merged_summary_all_repos_over_12_months()

    
# colorizing the report:
#    
# pip install colorama
    
# from colorama import Fore, Style

# text = "2023-03-01 - 12792c0  > Add JS conversion code & SW for intallability"

# # Split the text into parts
# date, _, hash, *message = text.split(' ', 3)

# # Print each part in the desired color
# print(Fore.GREEN + date, Fore.BLACK + hash, Fore.BLUE + ' '.join(message))

# # Reset the color to default
# print(Style.RESET_ALL)

# 70a41ee minimise output	2023-02-16	wtdl.py
# AFAD24	0200FF			B600FF		FF3D00
# y.green   d.blue          purple      or.red

# not working posible incorrect escape sequences for zsh ?  ??
def rgb(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

# Convert your hex color to RGB
hex_color = "0200FF"        # comes out "000000"
r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
print(rgb(r, g, b, "Supposed to be deep blue"))

# Convert your hex color to RGB
hex_color = "AFAD24"        # comes out "ABDFE4"
r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
print(rgb(r, g, b, "Supposed to be yellow green"))

# Convert your hex color to RGB
hex_color = "B600FF"        # comes out "000000"
r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
print(rgb(r, g, b, "Supposed to be purple"))

# Convert your hex color to RGB
hex_color = "FF3D00"        # comes out "000000"
r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
print(rgb(r, g, b, "Supposed to be orange red"))







