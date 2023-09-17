import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 
        
        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
        
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

csvFilePath = 'E:\\Web_learning\\wonder_site\\2023-07-25.txt'
jsonFilePath = 'E:\\Web_learning\\wonder_site\\2023-07-25.json'
csv_to_json(csvFilePath, jsonFilePath)




import pandas as pd
csv_file = pd.DataFrame(pd.read_csv("E:\\Web_learning\\wonder_site\\2023-07-25.txt", sep = "\t", header = 0, index_col = False))
csv_file.to_json("E:\\Web_learning\\wonder_site\\2023-07-25.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)


import csv, json
from geojson import Feature, FeatureCollection, Point

features = []
with open('E:\\Web_learning\\wonder_site\\2023-07-25.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for latitude, longitude, weather, temp in reader:
        latitude, longitude = map(float, (latitude, longitude))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'weather': weather,
                    'temp': temp
                }
            )
        )

collection = FeatureCollection(features)
with open("E:\\Web_learning\\wonder_site\\2023-07-25.json", "w") as f:
    f.write('%s' % collection)

