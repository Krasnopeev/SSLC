import numpy as np
import os


# get_data 
# {date} string in format '2023-07-15'

def get_data(date, count):
    data = date
    path_open = "static/data/"
    list_file = os.listdir(path_open)
    tabl = []
    for line in list_file[:]:
        line_new = line.replace('.','-')
        if line_new[:10] == data:
            #print("File exist. Success!")
            data_tabl = np.load(path_open+line)
            tabl = data_tabl['tabl']
            
        if line_new[15:-4] == data:
            #print("File exist. Success!")
            data_tabl = np.load(path_open+line)
            tabl = data_tabl['tabl']
        else:
            print("File not found or not exist")
    
    return(tabl[0:int(count)])

