import pandas as pd
import numpy as np

def from_dat_to_csv(name):
    '''
    Converts PPMS .dat file into .csv file
    '''
    df = pd.read_csv(name)
    name_csv = name[:-4] + '.csv'
  
    return df.to_csv(name_csv), name_csv,

    
if __name__ == "__main__":
    try:
        name = input('Enter .dat file name: ')
        if not name:
            raise ValueError
    except FileNotFoundError:
        print ("No such file in directory!")
        exit()                  
    except KeyboardInterrupt:
        print("\nUser interupted session!") 
        exit()
    except ValueError:
        print("\nNo file name provided!") 
        exit()
    from_dat_to_csv(name)
    
    print(from_dat_to_csv(name)[1]+ ' is saved' )


                