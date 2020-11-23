import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from shutil import get_terminal_size

'''Generates conditional comparison plots'''

#Pandas display configuration
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', get_terminal_size()[0])
pd.set_option('display.expand_frame_repr', False)

#Data location
readPath = ''
saveLocation = ''

#Read all data for RQ1_1
inputFileAB = 'att_RQ1_1 C(A)-C(B).csv'
inputFileAB1 = 'att_RQ1_1 C(A-1)-C(B-1).csv'
inputFileAB2 = 'att_RQ1_1 C(A-2)-C(B-2).csv'
inputFileAB3 = 'att_RQ1_1 C(A-3)-C(B-3).csv'
readPathFullAB = readPath + inputFileAB
readPathFullAB1 = readPath + inputFileAB1
readPathFullAB2 = readPath + inputFileAB2
readPathFullAB3 = readPath + inputFileAB3


#List over normal attributes in the dataset
#c_sys_SUS
# q_sys_freqUse	q_sys_complex	q_sys_easeUse	q_sys_techNeed	q_sys_funcInteg	q_sys_inconsist	q_sys_learnUse	q_sys_cumbUse	q_sys_confUse	q_sys_learnToUse
# c_moveDistanceAavg	c_moveDistanceCavg	c_moveDistanceDavg	c_clickCountAvg	c_dragCountAvg	c_movieInListPosAvg	c_moviePosAvg
# c_outc_listSatAvg	q_outc_diversity	q_outc_novelty	q_outc_serendipity	q_outc_relevance
# q_proc_searchSim	q_proc_decidDiff	q_proc_recImprove	q_proc_control	q_proc_sorting
# q_dem_onlineUsage	q_dem_movieUsage	c_ageGroup	c_dem_genderCat

#Define what variables to plot and how to label them
inclusionList = ['c_outc_listSatAvg','q_outc_diversity','q_outc_novelty','q_outc_serendipity','q_outc_relevance']
labelList = ['List Satisfaction','Diversity', 'Novelty','Serendipity','Relevance']

#Read and extract all the data for RQ1_1
dataAB = pd.read_csv(readPathFullAB)
dataAB = dataAB[dataAB.Variable.isin(inclusionList)]
y_A_meanAB = dataAB['C(A) Mean'].to_numpy()
y_B_meanAB = dataAB['C(B) Mean'].to_numpy()
y_A_SEAB = dataAB['C(A) SE'].to_numpy()
y_B_SEAB = dataAB['C(B) SE'].to_numpy()

dataAB1 = pd.read_csv(readPathFullAB1)
dataAB1 = dataAB1[dataAB1.Variable.isin(inclusionList)]
y_A_meanAB1 = dataAB1['C(A-1) Mean'].to_numpy()
y_B_meanAB1 = dataAB1['C(B-1) Mean'].to_numpy()
y_A_SEAB1 = dataAB1['C(A-1) SE'].to_numpy()
y_B_SEAB1 = dataAB1['C(B-1) SE'].to_numpy()

dataAB2 = pd.read_csv(readPathFullAB2)
dataAB2 = dataAB2[dataAB2.Variable.isin(inclusionList)]
y_A_meanAB2 = dataAB2['C(A-2) Mean'].to_numpy()
y_B_meanAB2 = dataAB2['C(B-2) Mean'].to_numpy()
y_A_SEAB2 = dataAB2['C(A-2) SE'].to_numpy()
y_B_SEAB2 = dataAB2['C(B-2) SE'].to_numpy()

dataAB3 = pd.read_csv(readPathFullAB3)
dataAB3 = dataAB3[dataAB3.Variable.isin(inclusionList)]
y_A_meanAB3 = dataAB3['C(A-3) Mean'].to_numpy()
y_B_meanAB3 = dataAB3['C(B-3) Mean'].to_numpy()
y_A_SEAB3 = dataAB3['C(A-3) SE'].to_numpy()
y_B_SEAB3 = dataAB3['C(B-3) SE'].to_numpy()

#Settings for the plot

distance = 0.12     #Distance between each point
offset= 0.4         #Aligns output. Depedent on plot size and other properties
separation = 0.05   #Reduce distance between direct comparison (A versus B for example)
title = "A|B outcome mean comparison"
plt.rcParams["figure.figsize"] = [11,3.5]   #Plot size
plt.rcParams.update({'font.size': 12})      #Font size
showplot = True
savePlot = True
saveFilename = 'RQ1_1 Outcome'

#Generate index
x_axes = dataAB1['Variable'].to_numpy()
index = np.arange(len(x_axes))

#Create plots
counter = 0
fig, ax = plt.subplots()
conditionA = ax.errorbar(index-offset, y_A_meanAB,
                 yerr = y_A_SEAB,
                 fmt ='o',
                    label="A", color="darkgrey")
counter +=1
conditionB = ax.errorbar(index+((distance*counter-offset)-separation), y_B_meanAB,
                 yerr = y_B_SEAB,
                 fmt ='o',
                label = "B", color="black")
counter +=1
conditionA1 = ax.errorbar(index+((distance*counter-offset)), y_A_meanAB1,
                 yerr = y_A_SEAB1,
                 fmt ='o',
                    label="A-1", color="red")
counter +=1
conditionB1 = ax.errorbar(index+((distance*counter-offset)-separation), y_B_meanAB1,
                 yerr = y_B_SEAB1,
                 fmt ='o',
                label = "B-1", color="maroon")
counter +=1
conditionA2 = ax.errorbar(index+((distance*counter-offset)), y_A_meanAB2,
                 yerr = y_A_SEAB2,
                 fmt ='o',
                    label="A-2", color="royalblue")
counter +=1
conditionB2 = ax.errorbar(index+((distance*counter-offset)-separation), y_B_meanAB2,
                 yerr = y_B_SEAB2,
                 fmt ='o',
                label = "B-2",color="darkblue")
counter +=1
conditionA3 = ax.errorbar(index+((distance*counter-offset)), y_A_meanAB3,
                 yerr = y_A_SEAB3,
                 fmt ='o',
                    label="A-3", color="limegreen")
counter +=1
conditionB4 = ax.errorbar(index+((distance*counter-offset)-separation), y_B_meanAB3,
                 yerr = y_B_SEAB3,
                 fmt ='o',
                label = "B-3",color="darkgreen")

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

