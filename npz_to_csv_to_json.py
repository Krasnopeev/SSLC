import numpy as np
import os
import csv 
import json

path_csv = "data/csv/"
path_json = "data/json/"
path_npz = "data/npz/"

list_file = os.listdir(path_npz)

for line in list_file[:]:
    data_tabl = np.load(path_npz+line, allow_pickle=True)
    data = data_tabl['tabl']
    #print(data)
    np.savetxt((path_csv+str(line[:-4])+".csv"), data, delimiter="\t", fmt='%s', comments='', header="id_num\tdate_light\tlat\tlon\tAmp\tNote")
    



def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf, delimiter="\t") 
        
        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
    
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)



list_file = os.listdir(path_csv)

for line in list_file[:]:
    csv_to_json(path_csv+line, str(path_json+line[:-4]+".json"))

