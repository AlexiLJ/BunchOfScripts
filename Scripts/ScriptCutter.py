import pandas as pd
import numpy as np

'''
This sript take an .csv file produced by imageJ
and filters out areas below pointed threshold
'''
try:
    name = input('Enter csv file name: ')
    if not name:
        raise ValueError

    df = pd.read_csv(name)

except FileNotFoundError:
    print ("No such file in directory!")
    exit()                                  #exit() is an alias for quit, raises the SystemExit excp.
except KeyboardInterrupt:
    print("\nUser interupted session!") 
    exit()
except ValueError:
    print("\nNo file name provided!") 
    exit()
  
# dropping unnamed columns
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True) 

while True:
    try:
        threshhold = int(input('Enter area threshhold (nm^2): '))
        break
    except ValueError:
        print("You need enter an integer")
        continue
    except KeyboardInterrupt:
        print("program has been interupted") 
        exit()

new_dataframe = df[df.Area>= threshhold] #filtering dataframe

# When we reset the index, the old index is added as a column,
# and a new sequential index is used
# We can use the drop parameter to avoid the old index being added as a column

new_dataframe = new_dataframe.reset_index(drop=True)

print(new_dataframe)
print('\n', new_dataframe.Area.describe(), sep="")
print(new_dataframe.Area.median())

while True:
   
    inq = input("Do you want to save file? (Y/N) ")
    try:
        if inq.casefold() == 'y': 
            name_csv = input('Enter name or press Enter for standart file name: ')
            if name_csv != "":
                try:
                    if name_csv[-4:] == ".csv":
                        print(name_csv)
                        new_dataframe.to_csv(name_csv)    
                        
                    elif name_csv[-4:] != ".csv":
                        print(name_csv)
                        name_csv = name_csv + '.csv'
                        new_dataframe.to_csv(name_csv)

                finally:
                    print(name_csv + ' is saved' )
                    break               
            else:
                file_name = name[:-4] + '_modified.csv'
                new_dataframe.to_csv(file_name)
                print(file_name + ' is saved')
                break         
        else:
            print("program is closed")
            break 
    except KeyboardInterrupt:
            print("Error occured, revise code!")    





