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

# output variable contains the response from the command
print(paths)  # decode from bytes to string

if '-p' in sys.argv:
    paths = sys.argv[sys.argv.index('-p') + 1]
    print(f"Using paths: {paths}")


def get_commit_count(repo_path, start_month, num_months):
    start_year = end_year = 2023
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

def get_commit_date_comment_and_files(repo_path, start_month, num_months):
    start_year = end_year = 2023
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

    no_of_commits = get_commit_count(repo_path, 1, 12)
        
    if no_of_commits > 0:
        print(f"{no_of_commits:<4} commits {repo_path}")
        active_repos[repo_path] = no_of_commits 


# show number of commits each month by repo
for repo_path in active_repos.keys():
    # if 'mysql_python' not in repo_path:
    #     continue

    if 'mysql_python_flask_1_deprecated' in repo_path:
        continue    

    year = 2023
    print(f"\n= = = {repo_path} = = =")
    commits = []
    for start_month in range(1, 13):

        no_of_commits = get_commit_count(repo_path, start_month, 1)
        commits.append(no_of_commits)
        
        if no_of_commits > 0:
            print('- ' * 40 + f"Month: {start_month:02}")    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            print(f"{start_month:02}: {no_of_commits:<4} {'#' * no_of_commits}")
            active_repos[repo_path] = no_of_commits
        
            print(get_commit_date_comment_and_files(repo_path, start_month, 1))
            #git log --since '2023-11-01' --until '2024-01-01' --pretty=format:'%cd - %h  > %s' --date=short --name-only

    print(f">-: {repo_path} - - - -")
    for i, c in enumerate(commits):
        print(f"{i+1:02}: {c:<4} {'#' * c}")
    print(f"> - - - - - - - - - - - -\n")

# git log --since '11/01/2023' --until '01/01/2024' --oneline --name-only
#pprint(active_repos)

# enumerate list w/ index and value


for repo_path, no_of_commits in active_repos.items():
    print(f"{no_of_commits:<4} commits {repo_path}")