#####2017 January---this script is for remaning files by creating two column
#####CSV file with the current(old) filenames in the 1st column and the desired
#####name as the second column.

#######To create the CSV:#######

####---Save a List of Files from Finder:
####-------Open the folder you want to get a content listing of and
####-------Hit Command+A (Select All) followed by Command+C (Copy)
####---Pasting straight into first column in excel --> Command+V.
####---Populate second column with corresponding new name desired.
####---Save as a csv file called 'file_names_dict_prep.csv'. 

import csv
import os
import shutil

####Create dictionary (keys from first column, values from second column).
with open ('file_names_dict_prep.csv') as f:
    d = dict(filter(None, csv.reader(f)))    

####Make folder 'renamed_files' in current directory.
os.mkdir('renamed_files') 

####Copy files from current directory to 'renamed_files'; copied file's name
####is the new name (values) from the dictionary created using CSV file.
for old_file_name in d: #for each key in dictionary d
    if os.path.isfile(old_file_name):
        shutil.copyfile(old_file_name, ('renamed_files' + '/' +
                                        d.get(old_file_name))
                                       )
                                                                      

