import pandas as pd
import json
import copy
import random
import shutil
import os
'''README NOTE
This file contains the different scripts that manipulates the raw data into json objects to be used by the databases.
As such, it is a workspace that is streamlined with one input and one output, but rather several sections of code
that does different operations depending on what is tested and changes that needed to be made.

Since the database was "molded" rather than a simple streamline, this file does not support a simple "generate" option
as of now. The following code is thus for reference only
'''
#Appends meta-data from movielens to the corresponding ID.
def createsystem(list):
    temp = { }
    for x in list:
        temp[x] = { }
        data = movieData[movieData['id'] == x]
        data = data.reset_index(drop=True)
        temp[x]["Id"] = data.get_value(0,'id')
        temp[x]["Title"] = data.get_value(0,'title')
        temp[x]["Lang"] = data.get_value(0,'en_lang')
        temp[x]["Cover_Path"] =  data.get_value(0,'cover_path')
        temp[x]["Overview"] = data.get_value(0,'overview')
        temp[x]["Actors"] =  data.get_value(0,'actors')
        temp[x]["Genres"] = data.get_value(0,'genres')
        temp[x]["Release"] = data.get_value(0,'release_year')
        temp[x]["Runtime"] = data.get_value(0,'runtime')
        temp[x]["Directors"] =  data.get_value(0,'directors')
        temp[x]["MovieLensID"] =  data.get_value(0,'MovieLensID')
    return temp

#Creates a random set of ten numbers and picks ten "movies" to a list.
def getRandom():
    baseline = [ ]
    source = random.sample(range(0,len(baselineSource)),10)
    for x in source:
        baseline.append(baselineSource[x])
    return baseline


#Init movielens Data. Need transposing.
movieData = pd.read_json(r'')
movieData = movieData.T

#Init similarity data. Drops uneeded columns
r_filenameTSV = 'AllSim-2.csv'
csv_read = pd.read_csv(r_filenameTSV, sep='\t')
csv_read.drop(columns=['pred_all_all/max(pred_all_all)','User:Rating','All','Title:LEV','Title:JW','Title:LCS','Title:BI','Title:LDA','Image:EMB','Image:BR','Image:SH','Image:CO','Image:COL','Image:EN','Plot:LDA','Plot:cos','Genre:LDA','Genre:Jacc','Stars:Jacc','Directors:Jacc','Date:MD','Tag:Genome','SVD'], axis=1, inplace=True)

#Init Variables
output = { }
counter = 0
#Practically speaking, this list contains all the ID's of the json files, thus movies used
baselineSource = list(set(csv_read['validation$r1'].tolist()))

mainSub = csv_read[csv_read['validation$r1'] == '51255.json']
temp = mainSub.nlargest(10,'pred_all/max(pred_all)')
results = []
for x in baselineSource:
    print(str(counter) + "/" + str(len(baselineSource)))
    counter = counter + 1
    mainSub = csv_read[csv_read['validation$r1'] == x]

    if(len(mainSub) <= 10):
        results.append(x)
        print(x)
print(results)

'''
#sorting images function
destination_folder = 'C:\\Users\\John B\\Documents\\pictures\\'
source_folder = 'C:\\Users\\John B\\Documents\\source\\'
test = movieData[movieData['id'].isin(baselineSource)]
test = test['cover_path'].tolist()
for x in test:
    fixX = x[1:]
    source = source_folder + fixX
    shutil.copy2(source,destination_folder) '''
'''
#SCRIPT FIX. This takes the bloody json file for the movies and makes it into separate content since I suck at databases
counter = 1
writePath = 'C:\\Output-Movies\\'
for i in baselineSource:
    print(str(counter) + "/" + str(len(baselineSource)))
    counter += 1
    temp = [i]
    metaData = createsystem(temp)
    metaData = metaData[i]
    fileName = writePath + i
    with open(fileName, "w") as writer:
        json.dump(metaData, writer)
#SCRIPT FIX 2. This takes the output of the previous file, appends metadata of current movie and writes it into separate files.
'''
'''
#SCRIPT FIX 3: I am a god damned idiot. Fixes movie sim files so that the ID is actually called ID.
counter = 0
for i in baselineSource:
    print(str(counter)+"/"+str(len(baselineSource)))
    counter += 1
    path = "C:\\Output\\"
    filepath = path + i
    with open(filepath,"r") as read_file:
        data = json.load(read_file)
    newFormat = {}
    newFormat["ID"] = i
    newFormat["Metadata"] = data[i]["Metadata"]
    newFormat['Similarities'] = data[i]["Similarities"]
    with open(filepath,"w") as writer:
        json.dump(newFormat,writer)
 '''
#Start of loop
'''
#Main loop for creating the JSON datafile for output. BEWARE this needs modification. Currently writes to one file,
#Should really write to one file per movie and also adds the metadata of the current movie to it.
for index in range(0,176270):
    print(index)
    currentfile = str(index) +".json"
    mainSub = csv_read[csv_read['validation$r1'] == currentfile]
    
    if not mainSub.empty:
        buildingBlock = {}
        buildingBlock['ID'] = currentfile
        buildingBlock['Metadata'] = createsystem(currentfile)
        #It will now sort the list so that the top ten ranked movies are selected. Then it appends the metadata to it.
        output[currentfile] = {}
        #All Predict
        temp = mainSub.nlargest(10,'pred_all/max(pred_all)')
        predicts = temp['validation$r2'].to_list()
        output[currentfile]['All'] = createsystem(predicts)

        #Title
        temp = mainSub.nlargest(10,'pred_title/max(pred_title)')
        predicts = temp['validation$r2'].to_list()
        output[currentfile]['Title'] = createsystem(predicts)

        #Image
        temp = mainSub.nlargest(10,'pred_image/max(pred_image)')
        predicts = temp['validation$r2'].to_list()
        output[currentfile]['Image'] = createsystem(predicts)

        #Plot
        temp = mainSub.nlargest(10,'pred_plot/max(pred_plot)')
        predicts = temp['validation$r2'].to_list()
        output[currentfile]['Plot'] = createsystem(predicts)

        #Genre
        temp = mainSub.nlargest(10,'pred_genre/max(pred_genre)')
        predicts = temp['validation$r2'].to_list()
        output[currentfile]['Genre'] = createsystem(predicts)

        #Stars
        temp = mainSub.nlargest(10,'pred_stars/max(pred_stars)')
        predicts = temp['validation$r2'].to_list()
        output[currentfile]['Stars'] = createsystem(predicts)

        #Director
        temp = mainSub.nlargest(10,'pred_directors/max(pred_directors)')
        predicts = temp['validation$r2'].to_list()
        output[currentfile]['Director'] = createsystem(predicts)

        #Date
        temp = mainSub.nlargest(10,'pred_date/max(pred_date)')
        predicts = temp['validation$r2'].to_list()
        output[currentfile]['Date'] = createsystem(predicts)

        #Tag
        temp = mainSub.nlargest(10,'pred_tag/max(pred_tag)')
        predicts = temp['validation$r2'].to_list()
        output[currentfile]['Tag'] = createsystem(predicts)

        #SVD
        temp = mainSub.nlargest(10,'pred_svd/max(pred_svd)')
        predicts = temp['validation$r2'].to_list()
        output[currentfile]['SVD'] = createsystem(predicts)

        #Baseline
        output[currentfile]['Baseline'] = createsystem(getRandom())


#Writes it to a file.
with open('MovieSim.json', 'w') as json_file:
  json.dump(output, json_file)
'''''