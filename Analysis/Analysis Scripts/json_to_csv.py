import pandas as pd
import json
import copy
import random
import shutil
import os
import json_flatten
import csv

'''
This documents works like a pipeline for flattening the survey result nested JSON objects into more manageable
CSV documents. It can take as many json objects as desired (minor code edits required in the fluid section)
and combines them into one csv document. Other operation performed in no particular order:
Dropping incomplete entries
repairing missing entries if appropriate metadata is available
calculating several other variables, denoted as 'c_' values
'''

#Generates the SUS score according to the standard formula.
def susCalc(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10):
    odd = ((q1 + q3 + q5 + q7 + q9) - 5)
    even = 25 - (q2 + q4 + q6 + q8 + q10)
    score = ((odd + even)*2.5)
    return score

#Returns average of inputs
def avgCalc(q1,q2,q3,q4,q5):
    return((q1+q2+q3+q4+q5)/5)

#Defines age categories as integers
def ageGroup(age):
    if 17 < age < 25:
        return 1
    elif 24 < age < 35:
        return 2
    elif 34 < age < 45:
        return 3
    elif 44 < age < 55:
        return 4
    elif 54 < age < 110:
        return 5
    else:
        return 0

#Gender as integer
def genderCat(string):
    if string == "Female":
        return 1
    elif string == "Male":
        return 2
    else:
        return 3

#Fixes error where movie position was not properly stored in one condition. Can be deduced by other stored variables.
def movieSelectError(selected,list):
    splitList = list.split('-')
    counter = 0
    for x in splitList:
        if x == selected:
            return counter
        else:
            counter +=1

#Determines the position of a movie in a given list based on meta information and selected list
def movieInListPosition(selMovie,selList,list):
    for x in list:
        if(x[0] == selList):
            inlistCounter = 0
            for y in range(0,5):
                if(selMovie == (str(x[1][str(y)]["MovieLensID"]) + ".json")):
                    return inlistCounter
                inlistCounter += 1

#Categorizes what interaction method participants preferred. 0 = equal, 1 = DragDrop, 2 = click
def interactionCategory(dragDrop,click):
    if dragDrop == click:
        return 0
    elif(dragDrop > click):
        return 1
    elif dragDrop < click:
        return 2

#Finds the sum index of a list in a participants study run
def averageIndex(term, totalList):
    temp = 0
    for x in totalList:
        reclist = x.split('-')
        temp += reclist.index(term)
    return temp

#Number of times a list is picked
def pickedTimes(term, totalList):
    temp = 0
    for x in totalList:
        if term == x:
            temp +=1
    return temp

#Input raw data
movieData1 = pd.read_json(r'')
movieData2 = pd.read_json(r'')
movieData3 = pd.read_json(r'')
movieData4 = pd.read_json(r'')
movieData5 = pd.read_json(r'')
movieData6 = pd.read_json(r'')
li = [movieData1,movieData2,movieData3, movieData4, movieData5, movieData6]
movieData = pd.concat(li, axis=0, ignore_index=True)

#What to name the output file
filename = "allConditions"
output= {}

#Removes incomplete entries. These incomplete entries may have occured due to participant exiting the study or
#connection error when inserting data.
movieData = movieData[movieData['surveyResults'].notna()]
movieData = movieData[movieData['browseResult5'].notna()]
movieData = movieData[movieData['browseResult4'].notna()]
movieData = movieData[movieData['browseResult3'].notna()]
movieData = movieData[movieData['browseResult2'].notna()]
movieData = movieData[movieData['browseResult1'].notna()]
movieData = movieData[movieData['v_refMovie_1'].notna()]
movieData = movieData[movieData['v_refMovie_2'].notna()]
movieData = movieData[movieData['v_refMovie_3'].notna()]
movieData = movieData[movieData['v_refMovie_4'].notna()]
movieData = movieData[movieData['v_refMovie_5'].notna()]
movieData = movieData.reset_index(drop=True)

#Prints dataset if desired
'''
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
    print(movieData)
'''


#Main loop for flattening the JSON into CSV files
for x in movieData.index:
    print(str(x+1)+"/"+str(len(movieData.index)))

    #basic session info
    output[x] = {}
    output[x]['sessionName'] = movieData.iloc[x]['sessionName']
    output[x]['time'] = movieData.iloc[x]['time']['$date']
    output[x]['condition'] = movieData.iloc[x]['condition']
    output[x]['v_attention1'] = movieData.iloc[x]['v_attetion1']

    #Loops through all itterations and stores each itteration dependent variable as variableName + Itteration.
    for i in range(1,6):
        output[x]['v_refMovie_'+str(i)] = movieData.iloc[x]['v_refMovie_'+str(i)]
        preListOrder = ""
        postListOrder= ""

        #Information on list order both before and after interactions are stored with corresponding movie and complete
        #meta information. Since these are not used in this thesis and would bloat the csv when flatten, only thesis
        #dependent information are stored. Change this segment if you wish to encode more meta information.
        for y in range (0,11):
            if y != 0:
                preListOrder += "-"
                postListOrder += "-"
            preListOrder += movieData.iloc[x]['browseResult'+str(i)]['v_initialListMeta'][y][0]
            postListOrder += movieData.iloc[x]['browseResult'+str(i)]['v_finalOrderF'][y][0]
        output[x]['v_preListOrder_'+str(i)] = preListOrder
        output[x]['v_postListOrder_' + str(i)] = postListOrder

        output[x]['v_listSelectedFrom' + str(i)] = movieData.iloc[x]['browseResult'+str(i)]['v_listSelectedFrom']
        output[x]['v_movieSelected' + str(i)] = movieData.iloc[x]['browseResult' + str(i)]['v_movieSelected']
        if output[x]['condition'] == 3 or output[x]['condition'] == 6: #Position not stored due to bug in condition 3. Fix applied from meta-information stored
            output[x]['v_moviePosition' + str(i)] = movieSelectError(output[x]['v_listSelectedFrom' + str(i)],output[x]['v_postListOrder_' + str(i)]  )
        else:
            output[x]['v_moviePosition' + str(i)] = movieData.iloc[x]['browseResult' + str(i)]['v_moviePosition']

        output[x]['v_clickCount' + str(i)] = movieData.iloc[x]['browseResult' + str(i)]['v_clickCount']
        output[x]['v_dragCount' + str(i)] = movieData.iloc[x]['browseResult' + str(i)]['v_dragCount']
        output[x]['v_moveDistanceA' + str(i)] = movieData.iloc[x]['browseResult' + str(i)]['v_moveDistanceA']
        output[x]['v_moveDistanceC' + str(i)] = movieData.iloc[x]['browseResult' + str(i)]['v_moveDistanceC']
        output[x]['v_moveDistanceD' + str(i)] = movieData.iloc[x]['browseResult' + str(i)]['v_moveDistanceD']
        output[x]['v_browsingTime' + str(i)] = movieData.iloc[x]['browseResult' + str(i)]['v_browsingTime']
        output[x]['v_zoomPressed' + str(i)] = movieData.iloc[x]['browseResult' + str(i)]['v_zoomPressed']
        output[x]['q_outc_satisfactionScore' + str(i)] = movieData.iloc[x]['browseResult' + str(i)]['q_outc_satisfactionScore']
        output[x]['c_movieInListPos' + str(i)] = movieInListPosition(output[x]['v_movieSelected' + str(i)],output[x]['v_listSelectedFrom' + str(i)],movieData.iloc[x]['browseResult'+str(i)]['v_finalOrderF'] )

    #This segment creates average values per participant based on itteration data
    output[x]['c_moveDistanceAavg'] = avgCalc( output[x]['v_moveDistanceA1'], output[x]['v_moveDistanceA2'], output[x]['v_moveDistanceA3'], output[x]['v_moveDistanceA4'], output[x]['v_moveDistanceA5'])
    output[x]['c_moveDistanceCavg'] = avgCalc(output[x]['v_moveDistanceC1'], output[x]['v_moveDistanceC2'],
                                               output[x]['v_moveDistanceC3'], output[x]['v_moveDistanceC4'],
                                               output[x]['v_moveDistanceC5'])
    output[x]['c_moveDistanceDavg'] = avgCalc(output[x]['v_moveDistanceD1'], output[x]['v_moveDistanceD2'],
                                               output[x]['v_moveDistanceD3'], output[x]['v_moveDistanceD4'],
                                               output[x]['v_moveDistanceD5'])
    output[x]['c_clickCountAvg'] = avgCalc(output[x]['v_clickCount1'], output[x]['v_clickCount2'],
                                               output[x]['v_clickCount3'], output[x]['v_clickCount4'],
                                               output[x]['v_clickCount5'])
    output[x]['c_dragCountAvg'] = avgCalc(output[x]['v_dragCount1'], output[x]['v_dragCount2'],
                                           output[x]['v_dragCount3'], output[x]['v_dragCount4'],
                                           output[x]['v_dragCount5'])
    output[x]['c_movieInListPosAvg'] = avgCalc(output[x]['c_movieInListPos1'], output[x]['c_movieInListPos2'],
                                           output[x]['c_movieInListPos3'], output[x]['c_movieInListPos4'],
                                           output[x]['c_movieInListPos5'])
    output[x]['c_preferecControl'] = interactionCategory(output[x]['c_moveDistanceDavg'] ,output[x]['c_moveDistanceCavg'])
    output[x]['c_moviePosAvg'] = avgCalc(output[x]['v_moviePosition1'], output[x]['v_moviePosition2'],
                                         output[x]['v_moviePosition3'], output[x]['v_moviePosition4'],
                                         output[x]['v_moviePosition5'])
    output[x]['c_movieInListPosAvg'] = avgCalc(output[x]['c_movieInListPos1'],output[x]['c_movieInListPos2'],output[x]['c_movieInListPos3'],output[x]['c_movieInListPos4'],output[x]['c_movieInListPos5'])

    #Study end variables
    output[x]['v_surveyTime'] = movieData.iloc[x]['surveyResults']['v_surveyTime']
    output[x]['v_totalTime'] = movieData.iloc[x]['surveyResults']['v_totalTime']
    output[x]['v_attention2'] = movieData.iloc[x]['surveyResults']['v_attention2']

    #Demographic questions
    output[x]['q_dem_onlineUsage'] = movieData.iloc[x]['surveyResults']['q_dem_onlineUsage']
    output[x]['q_dem_movieUsage'] = movieData.iloc[x]['surveyResults']['q_dem_movieUsage']
    output[x]['q_dem_age'] = movieData.iloc[x]['surveyResults']['q_dem_age']
    output[x]['c_ageGroup'] = ageGroup(output[x]['q_dem_age'])
    output[x]['q_dem_gender'] = movieData.iloc[x]['surveyResults']['q_dem_gender']
    output[x]['c_dem_genderCat'] = genderCat(movieData.iloc[x]['surveyResults']['q_dem_gender'])

    #System usability questions
    output[x]['q_sys_freqUse'] = movieData.iloc[x]['surveyResults']['questions']['q_sys_freqUse']
    output[x]['q_sys_complex'] = movieData.iloc[x]['surveyResults']['questions']['q_sys_complex']
    output[x]['q_sys_easeUse'] = movieData.iloc[x]['surveyResults']['questions']['q_sys_easeUse']
    output[x]['q_sys_techNeed'] = movieData.iloc[x]['surveyResults']['questions']['q_sys_techNeed']
    output[x]['q_sys_funcInteg'] = movieData.iloc[x]['surveyResults']['questions']['q_sys_funcInteg']
    output[x]['q_sys_inconsist'] = movieData.iloc[x]['surveyResults']['questions']['q_sys_inconsist']
    output[x]['q_sys_learnUse'] = movieData.iloc[x]['surveyResults']['questions']['q_sys_learnUse']
    output[x]['q_sys_cumbUse'] = movieData.iloc[x]['surveyResults']['questions']['q_sys_cumbUse']
    output[x]['q_sys_confUse'] = movieData.iloc[x]['surveyResults']['questions']['q_sys_confUse']
    output[x]['q_sys_learnToUse'] = movieData.iloc[x]['surveyResults']['questions']['q_sys_learnToUse']
    output[x]['c_sys_SUS'] = susCalc(output[x]['q_sys_freqUse'], output[x]['q_sys_complex'], output[x]['q_sys_easeUse'], output[x]['q_sys_techNeed'], output[x]['q_sys_funcInteg'],output[x]['q_sys_inconsist'], output[x]['q_sys_learnUse'], output[x]['q_sys_cumbUse'],output[x]['q_sys_confUse'],output[x]['q_sys_learnToUse'])

    #Process variables
    output[x]['q_proc_searchSim'] = movieData.iloc[x]['surveyResults']['questions']['q_proc_searchSim']
    output[x]['q_proc_decidDiff'] = movieData.iloc[x]['surveyResults']['questions']['q_proc_decidDiff']
    output[x]['q_proc_recImprove'] = movieData.iloc[x]['surveyResults']['questions']['q_proc_recImprove']
    output[x]['q_proc_control'] = movieData.iloc[x]['surveyResults']['questions']['q_proc_control']
    output[x]['q_proc_sorting'] = movieData.iloc[x]['surveyResults']['questions']['q_proc_sorting']

    #Outcome variables
    output[x]['c_outc_listSatAvg'] = avgCalc(output[x]['q_outc_satisfactionScore1'],output[x]['q_outc_satisfactionScore2'],output[x]['q_outc_satisfactionScore3'],output[x]['q_outc_satisfactionScore4'],output[x]['q_outc_satisfactionScore5'])
    output[x]['q_outc_diversity'] = movieData.iloc[x]['surveyResults']['questions']['q_outc_diversity']
    output[x]['q_outc_novelty'] = movieData.iloc[x]['surveyResults']['questions']['q_outc_novelty']
    output[x]['q_outc_serendipity'] = movieData.iloc[x]['surveyResults']['questions']['q_outc_serendipity']
    output[x]['q_outc_relevance'] = movieData.iloc[x]['surveyResults']['questions']['q_outc_relevance']

    #Comments storage
    comment = ""
    comment = movieData.iloc[x]['surveyResults'].get('comment')
    if comment:
        output[x]['q_comment'] = movieData.iloc[x]['surveyResults']['comment']
    else:
        output[x]['q_comment'] = ""

    #List Analysis fun fun
    output[x]['c_All_IndexAvg']         = averageIndex("All",       [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_Title_IndexAvg']       = averageIndex("Title",     [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_Image_IndexAvg']       = averageIndex("Image",     [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_Plot_IndexAvg']        = averageIndex("Plot",      [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_Genre_IndexAvg']       = averageIndex("Genre",     [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_Stars_IndexAvg']       = averageIndex("Stars",     [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_Director_IndexAvg']    = averageIndex("Director",  [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_Date_IndexAvg']        = averageIndex("Date",      [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_Tag_IndexAvg']         = averageIndex("Tag",       [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_SVD_IndexAvg']         = averageIndex("SVD",       [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_Baseline_IndexAvg']    = averageIndex('Baseline',  [output[x]['v_postListOrder_1'],output[x]['v_postListOrder_2'],output[x]['v_postListOrder_3'],output[x]['v_postListOrder_4'],output[x]['v_postListOrder_5']])
    output[x]['c_All_Picked']           = pickedTimes('All',        [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])
    output[x]['c_Title_Picked']         = pickedTimes('Title',      [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])
    output[x]['c_Image_Picked']         = pickedTimes('Image',      [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])
    output[x]['c_Plot_Picked']          = pickedTimes('Plot',       [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])
    output[x]['c_Genre_Picked']         = pickedTimes('Genre',      [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])
    output[x]['c_Stars_Picked']         = pickedTimes('Stars',      [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])
    output[x]['c_Director_Picked']      = pickedTimes('Director',   [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])
    output[x]['c_Date_Picked']          = pickedTimes('Date',       [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])
    output[x]['c_Tag_Picked']           = pickedTimes('Tag',        [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])
    output[x]['c_SVD_Picked']           = pickedTimes('SVD',        [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])
    output[x]['c_Baseline_Picked']      = pickedTimes('Baseline',   [output[x]['v_listSelectedFrom1'],output[x]['v_listSelectedFrom2'],output[x]['v_listSelectedFrom3'],output[x]['v_listSelectedFrom4'],output[x]['v_listSelectedFrom5']])

#Write to file
finalVersion = pd.DataFrame.from_dict(output).T
finalVersion = finalVersion.to_csv(index=False)
outputPath = filename + ".csv"
f = open(outputPath, "a")
f.write(finalVersion)
f.close


