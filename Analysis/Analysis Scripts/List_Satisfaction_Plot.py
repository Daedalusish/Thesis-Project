import pandas as pd
import researchpy as rp
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.stats.multicomp as mc
import sys
from shutil import get_terminal_size
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

'''Script for generating list satisfaction comparison tables'''

localPath = "" #Data source
saveLocation = ''   #Where to write output files
raw = pd.read_csv(localPath)
rawAtt = raw[raw.v_attention2 != False]

#Configure pandas writing to display all rows
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', get_terminal_size()[0])
pd.set_option('display.expand_frame_repr', False)

#Settings
showPlot = True
savePlot = True
compPlot = True
singular = False
outputAll = {}
outputAtt = {}
conditionLabel = [1,2,3,4,5]
colorlistA = ['red','royalblue','limegreen','maroon','darkblue','darkgreen']
colorlistB = ['red','royalblue','limegreen','maroon','darkblue']
labelListA = ['No control random A1','No control fixed A2','No control weight A3', 'Control random B1','Control fixed B2','Control weight B3']
labelListB = ['Random sort 1','Fixed sort 2','Weighted sort 3','No controll total A','Control total B']

#For comparison between singular conditions
if singular:
    #Get means and standard error from set, for all and attention sets
    for x in range(1,7):
        outputAll[x] = {}
        temp = raw[raw['condition'] == x]
        for i in range(1,6):
            outputAll[x]['listM' + str(i)] = temp['q_outc_satisfactionScore' + str(i)].mean().round(2)
            outputAll[x]['listSE' + str(i)] = temp['q_outc_satisfactionScore' + str(i)].sem().round(2)

    rawAtt = raw[raw.v_attention2 != False]
    outputAtt = {}
    for x in range(1,7):
        outputAtt[x] = {}
        temp = rawAtt[rawAtt['condition'] == x]
        for i in range(1,6):
            outputAtt[x]['listM' + str(i)] = temp['q_outc_satisfactionScore' + str(i)].mean().round(2)
            outputAtt[x]['listSE' + str(i)] = temp['q_outc_satisfactionScore' + str(i)].sem().round(2)

    finalAll = pd.DataFrame.from_dict(outputAll).T
    finalAtt = pd.DataFrame.from_dict(outputAtt).T

    #Creates plot showing all conditions as lines
    if compPlot:
        plt.figure(figsize=[6, 5])
        ax = plt.axes()
        for x in range(1,7):
            temp = finalAtt.loc[x, :]
            meanList = [temp['listM1'], temp['listM2'], temp['listM3'], temp['listM4'], temp['listM5']]
            index = np.arange(len(meanList))
            plt.errorbar(index, meanList,
                                 fmt ='o-',
                                 color=colorlistA[x-1],
                                label = labelListA[x-1])
        ax.set_facecolor("gainsboro")
        plt.title('Conditional comparison',fontsize=14)
        plt.xticks(index,conditionLabel, fontsize=11)
        yIndex = [3.5,3.6,3.7,3.8,3.9,4.0,4.1,4.2]
        plt.yticks(yIndex)
        ax.grid(which='both', color="white")
        plt.tick_params(
                axis='x',  # changes apply to the x-axis
                    which='minor',  # both major and minor ticks are affected
                    bottom=False,  # ticks along the bottom edge are off
                    top=False,  # ticks along the top edge are off
                    labelbottom=False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.ylabel('List satisfaction',fontsize="12")
        plt.xlabel('Iteration', fontsize ="12")
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), framealpha=1)
        plt.tight_layout()

        if savePlot:
            saveFilename = 'singularCondComp' + '.png'
            saveLocation1 = saveLocation + saveFilename
            plt.savefig(saveLocation1)

        if showPlot:
            plt.show()

    #Creates individual plots
    if not compPlot:
        for x in range(1, 7):
            plt.figure(figsize=[3, 5])
            ax = plt.axes()
            temp = finalAtt.loc[x, :]
            errorList = [temp['listSE1'], temp['listSE2'], temp['listSE3'], temp['listSE4'], temp['listSE5']]
            meanList = [temp['listM1'], temp['listM2'], temp['listM3'], temp['listM4'], temp['listM5']]

            index = np.arange(len(meanList))
            plt.errorbar(index, meanList,
                        yerr=errorList,
                         fmt='o',
                         color='black')
            plt.title(labelListA[x-1])
            ax.set_facecolor("gainsboro")
            plt.xticks(index, conditionLabel, fontsize=11)
            yIndex = [3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4]
            plt.yticks(yIndex)
            ax.grid(which='both', color="white")
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            plt.ylabel('List satisfaction', fontsize="12")
            plt.xlabel('Iteration', fontsize='12')
            ax.set_xticklabels(conditionLabel, minor=True)
            plt.tight_layout()
            if savePlot:
                saveFilename = labelListA[x-1] + '.png'
                saveLocation1 = saveLocation + saveFilename
                plt.savefig(saveLocation1)

            if showPlot:
                plt.show()

if not singular:
    temp1 = raw[raw.condition.isin([1,4])]
    temp2 = raw[raw.condition.isin([2,5])]
    temp3 = raw[raw.condition.isin([3,6])]
    tempA = raw[raw.condition.isin([1,2,3])]
    tempB = raw[raw.condition.isin([4,5,6])]
    totalist = [temp1,temp2,temp3,tempA,tempB]
    counter = 0
    for x in totalist:
        outputAll[counter] = {}
        for i in range(1, 6):
            outputAll[counter]['listM' + str(i)] = x['q_outc_satisfactionScore' + str(i)].mean().round(2)
            outputAll[counter]['listSE' + str(i)] = x['q_outc_satisfactionScore' + str(i)].sem().round(2)
        counter += 1
    print(outputAll)
    
    temp1 = rawAtt[rawAtt.condition.isin([1,4])]
    temp2 = rawAtt[rawAtt.condition.isin([2,5])]
    temp3 = rawAtt[rawAtt.condition.isin([3,6])]
    tempA = rawAtt[rawAtt.condition.isin([1,2,3])]
    tempB = rawAtt[rawAtt.condition.isin([4,5,6])]
    totalist = [temp1,temp2,temp3,tempA,tempB]
    counter = 0
    for x in totalist:
        outputAtt[counter] = {}
        for i in range(1, 6):
            outputAtt[counter]['listM' + str(i)] = x['q_outc_satisfactionScore' + str(i)].mean().round(2)
            outputAtt[counter]['listSE' + str(i)] = x['q_outc_satisfactionScore' + str(i)].sem().round(2)
        counter += 1
    finalAll = pd.DataFrame.from_dict(outputAll).T
    finalAtt = pd.DataFrame.from_dict(outputAtt).T
    labelList = ['list 1','list2','list3','no control','Control']

    if compPlot:
        plt.figure(figsize=[6, 5])
        ax = plt.axes()
        for x in range(0, 5):
            temp = finalAtt.loc[x, :]
            meanList = [temp['listM1'], temp['listM2'], temp['listM3'], temp['listM4'], temp['listM5']]
            index = np.arange(len(meanList))
            plt.errorbar(index, meanList,
                         fmt='o-',
                         color=colorlistB[x],
                         label=labelListB[x])
        ax.set_facecolor("gainsboro")
        plt.title('Conditional comparison')
        plt.xticks(index, conditionLabel, fontsize=11)
        yIndex = [3.7, 3.8, 3.9, 4.0, 4.1]
        plt.yticks(yIndex)
        ax.grid(which='both', color="white")
        plt.tick_params(
            axis='x',  # changes apply to the x-axis
            which='minor',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.ylabel('List satisfaction', fontsize="12")
        plt.xlabel('Iteration', fontsize="12")
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), framealpha=1)
        plt.tight_layout()

    if savePlot:
        saveFilename = 'aggregatedCondComp' + '.png'
        saveLocation1 = saveLocation + saveFilename
        plt.savefig(saveLocation1)

    if showPlot:
        plt.show()

    # Creates individual plots
    if not compPlot:
        for x in range(0, 5):
            plt.figure(figsize=[3, 5])
            ax = plt.axes()
            temp = finalAtt.loc[x, :]
            errorList = [temp['listSE1'], temp['listSE2'], temp['listSE3'], temp['listSE4'], temp['listSE5']]
            meanList = [temp['listM1'], temp['listM2'], temp['listM3'], temp['listM4'], temp['listM5']]

            index = np.arange(len(meanList))
            plt.errorbar(index, meanList,
                         yerr=errorList,
                         fmt='o',
                         color='black')
            plt.title(labelListB[x])
            ax.set_facecolor("gainsboro")
            plt.xticks(index, conditionLabel, fontsize=11)
            yIndex = [3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2]
            plt.yticks(yIndex)
            ax.grid(which='both', color="white")
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            plt.ylabel('List satisfaction', fontsize="12")
            plt.xlabel('Iteration', fontsize='12')
            ax.set_xticklabels(conditionLabel, minor=True)
            plt.tight_layout()

            if savePlot:
                saveFilename = labelListB[x] + '.png'
                saveLocation1 = saveLocation + saveFilename
                plt.savefig(saveLocation1)

            if showPlot:
                plt.show()