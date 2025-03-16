""" 
Question :- Write a python program to print the contents of the directory using the os module.
Search online for the function which does that.

""" 

import os
directory_path ='/'
entries = os.listdir(directory_path)
for entry in entries :
    print(entry)     