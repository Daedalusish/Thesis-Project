import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from shutil import get_terminal_size
from matplotlib import rcParams
from matplotlib.ticker import FormatStrFormatter

def getMeans(data,variable,condition):
    temp = []
    for x in condition:
        temp.append(data[data.condition == x][variable].mean())
    return temp

def getSE(data,variable,condition):
    temp = []
    for x in condition:
        temp.append(data[data.condition == x][variable].sem())
    return temp

rcParams.update({'figure.autolayout': True})

#Pandas display configuration
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', get_terminal_size()[0])
pd.set_option('display.expand_frame_repr', False)

#Data location
readPath = ''
saveLocation = ''

#Filtering
raw = pd.read_csv(readPath + "All Conditions.csv")
raw['condition'] = raw['condition'].replace([4], 1)
raw['condition'] = raw['condition'].replace([5], 2)
raw['condition'] = raw['condition'].replace([6], 3)
raw = raw[raw.v_attention2 != False]

#Read all data for RQ1_1
'''
inputFileAB = 'att_RQ1_1 C(A)-C(B).csv'
inputFileAB1 = 'att_RQ1_1 C(A-1)-C(B-1).csv'
inputFileAB2 = 'att_RQ1_1 C(A-2)-C(B-2).csv'
inputFileAB3 = 'att_RQ1_1 C(A-3)-C(B-3).csv'
readPathFullAB = readPath + inputFileAB
readPathFullAB1 = readPath + inputFileAB1
readPathFullAB2 = readPath + inputFileAB2
readPathFullAB3 = readPath + inputFileAB3
dataAB = pd.read_csv(readPathFullAB)
dataAB1 = pd.read_csv(readPathFullAB1)
dataAB2 = pd.read_csv(readPathFullAB2)
dataAB3 = pd.read_csv(readPathFullAB3)
datalist = [dataAB,dataAB1,dataAB2,dataAB3]
'''

#Data for RQ1_2
'''
inputFileAB = 'att_RQ1_2 C(C)-C(DD).csv'
readPathFullAB = readPath + inputFileAB
dataAB = pd.read_csv(readPathFullAB)
datalist = [dataAB]
'''


#List over normal attributes in the dataset
#c_sys_SUS
# q_sys_freqUse	q_sys_complex	q_sys_easeUse	q_sys_techNeed	q_sys_funcInteg	q_sys_inconsist	q_sys_learnUse	q_sys_cumbUse	q_sys_confUse	q_sys_learnToUse
# c_moveDistanceAavg	c_moveDistanceCavg	c_moveDistanceDavg	c_clickCountAvg	c_dragCountAvg	c_movieInListPosAvg	c_moviePosAvg
# c_outc_listSatAvg	q_outc_diversity	q_outc_novelty	q_outc_serendipity	q_outc_relevance
# q_proc_searchSim	q_proc_decidDiff	q_proc_recImprove	q_proc_control	q_proc_sorting
# q_dem_onlineUsage	q_dem_movieUsage	c_ageGroup	c_dem_genderCat
#Define what variables to plot and how to label them
inclusionList = ['c_sys_SUS',
                 'q_sys_freqUse','q_sys_complex','q_sys_easeUse','q_sys_techNeed','q_sys_funcInteg',
                 'q_sys_inconsist','q_sys_learnUse','q_sys_cumbUse','q_sys_confUse','q_sys_learnToUse',
                 'c_moveDistanceAavg','c_moveDistanceCavg','c_moveDistanceDavg','c_clickCountAvg','c_dragCountAvg',
                 'c_movieInListPosAvg','c_moviePosAvg''',
                 'c_outc_listSatAvg','q_outc_diversity','q_outc_novelty','q_outc_serendipity','q_outc_relevance',
                 'q_proc_searchSim','q_proc_decidDiff','q_proc_recImprove','q_proc_control','q_proc_sorting',
                 'q_dem_onlineUsage','q_dem_movieUsage','c_ageGroup']
labelList =     ['System usability score','Desire to use system','Complexity','Easy to use',"Assistance need",'Functions integrated',
                 'Inconsistency in system','Easy to learn','Cumbersome','Confident using system','A lot to learn',
                 'Total distance','Click distance','Drag and drop distance',"Times clicked",'Times dragged',
                 "Index of movie in list",'Index of list selected',
                 'List satisfaction','Diversity', 'Novelty','Serendipity','Relevance',
                 'Recommendation similarity','Difficulty of picking movie','Recommendations improved','Recommendation Control','Sorting Function Useful',
                 'Streaming service usage','Movie consumption','Age group']

#Conditional Labeling and organizing
#conditionLabel = ['No control (A)','Control (B)','No control random sort (A-1)','Control random sort (B-1)','No Control constant sort (A-2)',
 #                'Control constant sort (B-2)','No control weight sort (A-3)','Control weight sort (B-3)']
#cList = [['A','B'],['A-1','B-1'],['A-2','B-2'],['A-3','B-3']]
#conditionLabel = ['Click User', "Drag & Drop user"]
conditionLabel = ["Random sort","Persistant sort","Weighted Sort"]
#cList = [['C','DD']]
selectionCounter = 0

plt.rcParams.update({'font.size': 12})
savePlot = False
showPlot = True
plotStuff = False
alternativePlot = True
if alternativePlot:
    for x in inclusionList:
        selectedData = inclusionList[selectionCounter]
        selectedLabel = labelList[selectionCounter]
        selectionCounter += 1
        errorList = getSE(raw,selectedData,[1,2,3])
        meanList = getMeans(raw,selectedData,[1,2,3])

        plt.figure(figsize=[4, 5])
        ax = plt.axes()

        index = np.arange(len(conditionLabel))
        #index = [0, 1]
        plt.errorbar(index, meanList,
                     yerr=errorList,
                     fmt='o',
                     color="black")
        ax.set_facecolor("gainsboro")
        plt.xticks(index, conditionLabel, rotation='vertical', fontsize=11)
        #plt.locator_params(axis='x', nbins=2)
        ax.grid(which='both', color="white")
        plt.tick_params(
            axis='x',  # changes apply to the x-axis
            which='minor',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=False)
        # ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.ylabel(selectedLabel, fontsize="12")
        plt.tight_layout()
        if savePlot:
            saveFilename = selectedLabel + '.png'
            saveLocation1 = saveLocation + saveFilename
            plt.savefig(saveLocation1)

        if showPlot:
            plt.show()

if plotStuff:
    for x in inclusionList:
        selectedData = inclusionList[selectionCounter]
        selectedLabel = labelList[selectionCounter]
        selectionCounter +=1
        errorList =[]
        meanList = []
        counter = 0
        for x in datalist:
            temp = x[x.Variable == selectedData]
            meanList.append(float(temp["C(" +cList[counter][0] + ") Mean"]))
            meanList.append(float(temp["C(" + cList[counter][1] + ") Mean"]))
            errorList.append(float(temp["C(" +cList[counter][0] + ") SE"]))
            errorList.append(float(temp["C(" + cList[counter][1] + ") SE"]))

            counter += 1

        plt.figure(figsize=[4,5])
        ax = plt.axes()

        #index = np.arange(len(conditionLabel))
        index = [0,1]
        plt.errorbar(index, meanList,
                         yerr = errorList,
                         fmt ='o',
                         color="black")
        ax.set_facecolor("gainsboro")
        plt.xticks(index,conditionLabel,rotation='vertical', fontsize=11)
        plt.locator_params(axis='x', nbins=2)
        ax.grid(which='both', color="white")
        plt.tick_params(
            axis='x',  # changes apply to the x-axis
            which='minor',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=False)
        #ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.ylabel(selectedLabel,fontsize="12")
        plt.tight_layout()
        if savePlot:
            saveFilename = selectedLabel + '.png'
            saveLocation1 = saveLocation + saveFilename
            plt.savefig(saveLocation1)

        if showPlot:
            plt.show()


#Settings saved for pairwise comparison
'''
#Creates the grid
test = [0.5,1.5,2.5,3.5]
yticksMti = [2.75,3.25,3.75,4.25,4.75]
yticksMi = [3,3.5,4,4.5]
ax.set_yticks(yticksMi, minor=False)
ax.set_yticks(yticksMti, minor=True)
ax.set_xticks(test, minor=True)
ax.grid(which='both')
ax.xaxis.grid(False, which='major')
ax.xaxis.grid(True, which='minor', color="black")
ax.yaxis.grid(True, which='minor', color="gainsboro")
ax.yaxis.grid(True, which='major', color="lightgrey")

#Defines range, labels and other properties
ax.set_ylim([2.75, 4.75])
ax.set_ylabel('Average Likert Score')
ax.set_title(title)
ax.set_xticks((index + distance / 2)-0.06)
ax.set_xticklabels(labelList)
ax.legend(loc='center left', bbox_to_anchor=(0.96, 0.5), framealpha=1)

if savePlot:
    saveFilename = saveFilename + '.png'
    saveLocation = saveLocation + saveFilename
    plt.savefig(saveLocation)

if showplot:
    plt.show()

'''