#!/usr/bin/env python3

import os
from datetime import datetime
from shutil import move
from git import Repo

os.chdir("bachelor_arbeit")

source_dir = os.getcwd()

file_names = os.listdir(".")

no_files_found = True

folder_name = datetime.today().strftime('%d.%m.%Y')
os.mkdir(folder_name)
target_dir = os.path.join(source_dir,folder_name)
for file_name in file_names:
	if os.path.isfile(file_name):
		move(os.path.join(source_dir,file_name),target_dir)
		no_files_found = False
if no_files_found:
	os.rmdir(folder_name)
else:
	repo = Repo(".git")
	repo.git.add('.')
	repo.index.commit(folder_name)
	origin = repo.remote(name="origin")
	origin.push()

