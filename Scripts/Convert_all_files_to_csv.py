import os 
import pandas as pd
from From_dat_to_csv import from_dat_to_csv
'''
Converts all files in directory from .dat to .csv
and removes LCR head

'''
path = os.getcwd()

with os.scandir(path) as scan:
    for file in scan:
        fname=file.name
        if file.name.endswith(".dat") and file.is_file():
            with open(file, encoding="utf-8") as ifile:
                lines = ifile.readlines()
                if '[Data]\n' in lines:
                    lines = lines[lines.index('[Data]\n')+1:]
                else: pass
               
                with open('dummy.dat', 'w', encoding="utf-8") as dummy:
                    for line in lines:
                        dummy.write(line)
                from_dat_to_csv('dummy.dat')
                os.rename('dummy.csv', f'{fname[:-4]}.csv')
    
    os.remove('dummy.dat')
                

