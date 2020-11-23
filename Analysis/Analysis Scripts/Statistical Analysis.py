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


'''
This file is the main file for analyzing the data and writing ANVOA, Tukey and T-test tables based on variable configuration.
It does require some manual edits
'''
#https://www.pythonfordatascience.org/anova-python/ source for function. Provides Statistics
def anova_table(aov):
    aov['mean_sq'] = aov[:]['sum_sq']/aov[:]['df']

    aov['eta_sq'] = aov[:-1]['sum_sq']/sum(aov['sum_sq'])

    aov['omega_sq'] = (aov[:-1]['sum_sq']-(aov[:-1]['df']*aov['mean_sq'][-1]))/(sum(aov['sum_sq'])+aov['mean_sq'][-1])

    cols = ['sum_sq', 'df', 'mean_sq', 'F', 'PR(>F)', 'eta_sq', 'omega_sq']
    aov = aov[cols]
    return aov

#Function for running One Way Anova
def runOneAnova(data,outcomeVar, independent):
    modelInput = outcomeVar + ' ~ C(' + independent + ')'
    model = ols(modelInput, data=data).fit()
    shapiro = stats.shapiro(model.resid)
    visNormality = False

    if visNormality:
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111)
        normality_plot, stat = stats.probplot(model.resid, plot=plt, rvalue=True)
        ax.set_title("Probability plot of model residual's", fontsize=20)
        ax.set
        plt.show()

    return sm.stats.anova_lm(model, typ=2), shapiro

#Function for running Two Way Anova
def runTwoAnova(data,outcomeVar, independent1,independent2):
    modelInput = outcomeVar + ' ~ ' + independent1 + ' + ' + independent2 + ' + ' + independent1 + ' : ' + independent2
    model = ols(modelInput, data=data).fit()
    return sm.stats.anova_lm(model, typ=2)

#Provides general statistical information
def contentAnalysis(data,outcomeVar,independent):
    return rp.summary_cont(data[outcomeVar].groupby(data[independent]))

#Tukey Honest Significant Distance code
def runTukey(data, outcomeVar,independent):
    comp = mc.MultiComparison(data[outcomeVar], data[independent])
    calctukey = comp.tukeyhsd()
    return pd.DataFrame(data=calctukey._results_table.data[1:], columns=calctukey._results_table.data[0])

#Function for running the T-test and formatting output
def tTest(data,checking,group,group1,group2,nameGroup1,nameGroup2,x,output):
    output[x]['Variable'] = checking
    leveneResult = stats.levene(data[checking][data[group] == group1], data[checking][data[group] == group2], center='mean')

    summary, results = rp.ttest(group1=data[checking][data[group] == group1], group1_name=nameGroup1,
                                group2=data[checking][data[group] == group2], group2_name=nameGroup2)

    output[x][nameGroup1 + ' N'] = round(summary.iloc[0]['N'],2)
    output[x][nameGroup2 + ' N'] = round(summary.iloc[1]['N'],2)
    output[x][nameGroup1 + ' Mean'] = round(summary.iloc[0]['Mean'],2)
    output[x][nameGroup2 + ' Mean'] = round(summary.iloc[1]['Mean'],2)
    output[x][nameGroup1 + ' SD'] = round(summary.iloc[0]['SD'],2)
    output[x][nameGroup2 + ' SD'] = round(summary.iloc[1]['SD'],2)
    output[x][nameGroup1 + ' SE'] = round(summary.iloc[0]['SE'],2)
    output[x][nameGroup2 + ' SE'] = round(summary.iloc[1]['SE'],2)


    if leveneResult.pvalue < 0.05:
        output[x]['Leneve Value'] = str(round(leveneResult.pvalue,2)) + "****"
    else:
        output[x]['Leneve Value'] = str(round(leveneResult.pvalue,2))

    values = results.results
    output[x]["T-Test P Value"] = signifiant(float(values.loc[[3]]))
    output[x]["Cohen Effect Size"] = effectSize(float(values.loc[[6]]))

#translates Cohen's effect size
def effectSize(number):
    if abs(number) < 0.01:
        return "None (" + str(round(number,2)) + ")"
    if  0.20 > abs(number) >= 0.01:
        return "Very Small (" + str(round(number,2)) + ")"
    elif 0.5 > abs(number) >= 0.20:
        return "Small (" + str(round(number,2)) + ")"
    elif 0.8 > abs(number) >= 0.5:
        return "Medium (" + str(round(number,2)) + ")"
    elif 1.20 > abs(number) >= 0.8:
        return "Large (" + str(round(number,2)) + ")"
    elif 1.40 > abs(number) >= 1.20:
        return "Very Large (" + str(round(number,2)) + ")"
    else:
        return "Huge (" + str(round(number,2)) + ")"

#Annotates P values
def signifiant(value):
    if value <= 0.001:
        return str(round(value,3))+"***"
    if value <= 0.01:
        return str(round(value,3))+"**"
    if value <= 0.05:
        return str(round(value,3))+"*"
    else:
        return str(round(value,3))

def leveneTest(data,checking,group,groupvalues):
    return stats.levene(data[checking][data[group] == groupvalues[0]],
                 data[checking][data[group] == groupvalues[1]],
                 data[checking][data[group] == groupvalues[2]],
                 center='mean')
def omegaEffect(value):
    if value < 0.01:
        return "None (" + str(round(value,3)) + ")"
    elif  0.06 > value >= 0.01:
        return "Small (" + str(round(value,3)) + ")"
    elif 0.14 > value >= 0.06:
        return "Medium (" + str(round(value, 3)) + ")"
    else:
        return "Large (" + str(round(value, 3)) + ")"

def writeToFile(path,filename,prefix,content):
    content = content.to_csv(index=False)
    fullOutputPath = path + prefix + filename + ".csv"
    f = open(fullOutputPath, "a")
    f.write(content)
    f.close

'''******************************************************************************************************************'''
'''GLOBAL SETTINGS
Settings for tests are located in test code block
'''

# Settings
localPath = "" #Data source
outputPath = ""   #Where to write output files
raw = pd.read_csv(localPath)   #input data

#Which tests to run
runT_Test = False
runOneWay = False
runTwoWay = True
saveLog = False #Save command output to text file.

#Configure pandas writing to display all rows
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', get_terminal_size()[0])
pd.set_option('display.expand_frame_repr', False)

#Variable list
systemUS    = ['c_sys_SUS']
susExtended  = ['q_sys_freqUse','q_sys_complex','q_sys_easeUse','q_sys_techNeed','q_sys_funcInteg','q_sys_inconsist','q_sys_learnUse','q_sys_cumbUse','q_sys_confUse','q_sys_learnToUse']
process     = ['q_proc_searchSim','q_proc_decidDiff','q_proc_recImprove','q_proc_control','q_proc_sorting']
listSat = ['q_outc_satisfactionScore1','q_outc_satisfactionScore2','q_outc_satisfactionScore3','q_outc_satisfactionScore4','q_outc_satisfactionScore5']
outcome     = ['c_outc_listSatAvg','q_outc_diversity','q_outc_novelty','q_outc_serendipity','q_outc_relevance']
activity    = ['c_moveDistanceAavg','c_moveDistanceCavg','c_moveDistanceDavg','c_clickCountAvg','c_dragCountAvg',
               'c_movieInListPosAvg','c_moviePosAvg','c_preferecControl']
#demographic = ['q_dem_onlineUsage','q_dem_movieUsage','c_ageGroup','c_dem_genderCat']
demographic = ['c_ageGroup','c_dem_genderCat']
indexes     = ['c_All_IndexAvg','c_Title_IndexAvg','c_Image_IndexAvg','c_Plot_IndexAvg','c_Genre_IndexAvg',
              'c_Stars_IndexAvg','c_Director_IndexAvg','c_Date_IndexAvg','c_Tag_IndexAvg','c_SVD_IndexAvg',
              'c_Baseline_IndexAvg','c_All_Picked','c_Title_Picked','c_Image_Picked','c_Plot_Picked','c_Genre_Picked',
              'c_Stars_Picked','c_Director_Picked','c_Date_Picked','c_Tag_Picked','c_SVD_Picked','c_Baseline_Picked']
combination = []
combination.extend(systemUS)
combination.extend(susExtended)
combination.extend(activity)
combination.extend(listSat)
combination.extend(outcome)
combination.extend(process)
combination.extend(demographic)
combination.extend(indexes)
# print(raw)
if saveLog:
    sys.stdout = open('consoleOutput.txt', 'w')

'''******************************************************************************************************************'''
if runT_Test:
    saveTtest = True  # Stores the T test
    testList = combination # Asign set of questions to test
    filterBy = 'condition'  # Which variable to group by
    group1Name = 'Passive'  # Name first test group
    group1Value = 1  # No script is set up for this to have effect. Manually edit data processing
    group2Name = 'Active'  # Name second test group
    group2Value = 4  # No script is set up for this to have effect. Manually edit data processing
    prefixName = "RQ1_1"
    suffix = "AB"
    filename = prefixName + "_"+ suffix
    resultAtt = {}  # Stores results
    resultAll = {}

    #Filter Data

    #A versus B

    '''Declare conditions to include and other filters here'''
    #raw['condition'] = raw['condition'].replace([3,4], 2)
    #raw['condition'] = raw['condition'].replace([3], 1)
    raw['condition'] = raw['condition'].replace([3,2], 1)
    raw['condition'] = raw['condition'].replace([6,5], 4)


    ''''''
    #Sub condition versus sub condition
    raw = raw[raw[filterBy].isin([1,4])]
    #raw['c_preferecControl'] = raw['c_preferecControl'].replace([2],1)
    #raw = raw[raw.c_preferecControl.isin([group1Value,group2Value])]
    ''''''
    rawAttention = raw[raw.v_attention2 != False]
    counter = 0
    steps = 1
    for x in testList:
        print(str(steps) +"/"+str(len(testList)*2))
        resultAll[counter] = {}
        tTest(raw, x, filterBy, group1Value, group2Value, group1Name, group2Name, counter,resultAll)
        counter +=1
        steps += 1
    counter = 0
    for x in testList:
        print(str(steps) + "/" + str(len(testList) * 2))
        resultAtt[counter] = {}
        tTest(rawAttention, x, filterBy, group1Value, group2Value, group1Name, group2Name, counter,resultAtt)
        counter += 1
        steps += 1

    resultAll = pd.DataFrame.from_dict(resultAll).T
    resultAtt = pd.DataFrame.from_dict(resultAtt).T
    print("All results")
    print(resultAll)
    print()
    print("***************************")
    print()
    print("Attention Results")
    print(resultAtt)

    if saveTtest:
        writeToFile(outputPath, filename, 'all_', resultAll)
        writeToFile(outputPath, filename, 'att_', resultAtt)
'''******************************************************************************************************************'''
if runOneWay:
    saveOWA = True          # Stores the Anova Results
    testList = combination     # Asign set of questions to test
    filterBy = 'q_dem_movieUsage'  # Which variable to group by
    filename = "RQ3-Moviewatcg"       #Filename to write

    #Initiate storing variables
    resultAll = pd.DataFrame(columns=['','sum_sq','df','mean_sq','F','PR(>F)','eta_sq','omega_sq','Normality','Homogeneity'])  # Stores results
    tukeyAll = pd.DataFrame(columns=['group1','group2','meandiff','p-adj','lower','upper','reject',"Cohen's d","Mean","SD","SE"])
    resultAtt = pd.DataFrame(columns=['','sum_sq','df','mean_sq','F','PR(>F)','eta_sq','omega_sq','Normality','Homogeneity'])  # Stores results
    tukeyAtt = pd.DataFrame(columns=['group1','group2','meandiff','p-adj','lower','upper','reject',"Cohen's d","Mean","SD","SE"])

    #Defines Variable to use

    raw['q_dem_movieUsage'] = raw['q_dem_movieUsage'].replace([1], 0)
    raw['q_dem_movieUsage'] = raw['q_dem_movieUsage'].replace([3], 2)
    raw['q_dem_movieUsage'] = raw['q_dem_movieUsage'].replace([5], 4)
    raw['q_dem_movieUsage'] = raw['q_dem_movieUsage'].replace([6], 4)
    raw['q_dem_movieUsage'] = raw['q_dem_movieUsage'].replace([7], 4)
    #raw[filterBy] = raw[filterBy].replace([1], 2)
    #raw[filterBy] = raw[filterBy].replace([5], 4)
    #raw = raw[raw.condition.isin([4,5,6])]
    #variableSet = [0,2,4]
    #raw = raw[raw.c_dem_genderCat.isin(variableSet)]
    #rawAttention = raw[raw.v_attention2 != False]


    #Other
    counter = 1
    variableSet = [0, 2, 4] #Declare the value for the ANOVA groups.

    for x in testList:
        print(str(counter) + "/" + str(len(testList) * 2))
        counter +=1
        selectedD = raw[[filterBy, x]]

        #Performs Anova test and Normality test
        anova, normality = runOneAnova(selectedD, x, filterBy)
        anova = anova_table(anova)

        #Testing and adding normality and homogeneity test values to anova table
        homogeneity = leveneTest(raw,x,filterBy,variableSet)
        if homogeneity.pvalue < 0.05:
            homogeneity = str(round(homogeneity.pvalue,2)) + "****"
        else:
            homogeneity = str(round(homogeneity.pvalue,2))

        if normality.pvalue < 0.05:
            normality = str(round(normality.pvalue,2)) + "****"
        else:
            normality = str(round(normality.pvalue,2))

        #Inserting data and storing this round of Anova
        anova.insert(7,'Normality',normality)
        anova.insert(8, 'Homogeneity', homogeneity)

        tempAnova = pd.Series([x, "-", "-", "-", "-", "-", "-", "-", "-", "-"], index=(
        '', 'sum_sq', 'df', 'mean_sq', 'F', 'PR(>F)', 'eta_sq', 'omega_sq', 'Normality', 'Homogeneity'))
        resultAll = resultAll.append(tempAnova, ignore_index=True, sort=False)
        resultAll = resultAll.append(anova, ignore_index=True, sort=False)

        #Perform post-hoc test with Tukey-HSD
        contentAn = contentAnalysis(raw,x,filterBy) #Provides a list of useful goodies like mean and SD
        tukey = runTukey(selectedD, x, filterBy)

        #Manually calculating cohen's d since it is apperantly not implemented in any library
        sdpool = sqrt((((contentAn.iloc[0]['SD']) ** 2) + ((contentAn.iloc[1]['SD']) ** 2)) / 2)
        cohens1 = effectSize((contentAn.iloc[1]['Mean'] - contentAn.iloc[0]['Mean']) / sdpool)
        sdpool = sqrt((((contentAn.iloc[0]['SD']) ** 2) + ((contentAn.iloc[2]['SD']) ** 2)) / 2)
        cohens2 = effectSize((contentAn.iloc[2]['Mean'] - contentAn.iloc[0]['Mean']) / sdpool)
        sdpool = sqrt((((contentAn.iloc[1]['SD']) ** 2) + ((contentAn.iloc[2]['SD']) ** 2)) / 2)
        cohens3 = effectSize((contentAn.iloc[2]['Mean'] - contentAn.iloc[1]['Mean']) / sdpool)
    
        # Inserting data and storing this round of tukey.
        temp = pd.Series([x, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                         index=(
                             'group1', 'group2', 'meandiff', 'p-adj', 'lower', 'upper', 'reject', "Cohen's d", "Mean",
                             "SD",
                             "SE"))
        
        tukey.insert(7, "Cohen's d", [cohens1,cohens2,cohens3])
        tukey.insert(8, 'Mean', [contentAn.iloc[0]['Mean'],contentAn.iloc[1]['Mean'],contentAn.iloc[2]['Mean']])
        tukey.insert(9, 'SD', [contentAn.iloc[0]['SD'],contentAn.iloc[1]['SD'],contentAn.iloc[2]['SD']])
        tukey.insert(10, 'SE', [contentAn.iloc[0]['SE'],contentAn.iloc[1]['SE'],contentAn.iloc[2]['SE']])

        tukeyAll = tukeyAll.append(temp, ignore_index=True, sort=False)
        tukeyAll = tukeyAll.append(tukey, ignore_index=True, sort=False)

    #Attention, copy pasted with variable changes since I'm to tired to make code generic
    for x in testList:
        print(str(counter) + "/" + str(len(testList) * 2))
        counter +=1
        selectedD = rawAttention[[filterBy, x]]

        # Performs Anova test and Normality test
        anova, normality = runOneAnova(selectedD, x, filterBy)
        anova = anova_table(anova)

        # Testing and adding normality and homogeneity test values to anova table
        homogeneity = leveneTest(rawAttention, x, filterBy,variableSet)
        if homogeneity.pvalue < 0.05:
            homogeneity = str(round(homogeneity.pvalue, 2)) + "****"
        else:
            homogeneity = str(round(homogeneity.pvalue, 2))

        if normality.pvalue < 0.05:
            normality = str(round(normality.pvalue, 2)) + "****"
        else:
            normality = str(round(normality.pvalue, 2))

        # Inserting data and storing this round of Anova
        anova.insert(7, 'Normality', normality)
        anova.insert(8, 'Homogeneity', homogeneity)

        tempAnova = pd.Series([x, "-", "-", "-", "-", "-", "-", "-", "-", "-"], index=(
            '', 'sum_sq', 'df', 'mean_sq', 'F', 'PR(>F)', 'eta_sq', 'omega_sq', 'Normality', 'Homogeneity'))
        resultAtt = resultAtt.append(tempAnova, ignore_index=True, sort=False)
        resultAtt = resultAtt.append(anova, ignore_index=True, sort=False)

        # Perform post-hoc test with Tukey-HSD
        contentAn = contentAnalysis(rawAttention,x,filterBy)  # Provides a list of useful goodies like mean and SD
        tukey = runTukey(selectedD, x, filterBy)

        # Manually calculating cohen's d since it is apperantly not implemented in any library
        '''Formula = Cohen's d = (M2 - M1) ⁄ SDpooled         SDpooled = √((SD1^2 + SD2^2) ⁄ 2) '''
        sdpool = sqrt((((contentAn.iloc[0]['SD']) ** 2) + ((contentAn.iloc[1]['SD']) ** 2)) / 2)
        cohens1 = effectSize((contentAn.iloc[1]['Mean'] - contentAn.iloc[0]['Mean']) / sdpool)

        sdpool = sqrt((((contentAn.iloc[0]['SD']) ** 2) + ((contentAn.iloc[2]['SD']) ** 2)) / 2)
        cohens2 = effectSize((contentAn.iloc[2]['Mean'] - contentAn.iloc[0]['Mean']) / sdpool)

        sdpool = sqrt((((contentAn.iloc[1]['SD']) ** 2) + ((contentAn.iloc[2]['SD']) ** 2)) / 2)
        cohens3 = effectSize((contentAn.iloc[2]['Mean'] - contentAn.iloc[1]['Mean']) / sdpool)

        # Inserting data and storing this round of tukey.'
        temp = pd.Series([x, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                         index=(
                             'group1', 'group2', 'meandiff', 'p-adj', 'lower', 'upper', 'reject', "Cohen's d", "Mean",
                             "SD",
                             "SE"))
 
        tukey.insert(7, "Cohen's d", [cohens1,cohens2,cohens3])
        tukey.insert(8, 'Mean', [contentAn.iloc[0]['Mean'],contentAn.iloc[1]['Mean'],contentAn.iloc[2]['Mean']])
        tukey.insert(9, 'SD', [contentAn.iloc[0]['SD'],contentAn.iloc[1]['SD'],contentAn.iloc[2]['SD']])
        tukey.insert(10, 'SE', [contentAn.iloc[0]['SE'],contentAn.iloc[1]['SE'],contentAn.iloc[2]['SE']])

        tukeyAtt = tukeyAtt.append(temp, ignore_index=True, sort=False)
        tukeyAtt = tukeyAtt.append(tukey, ignore_index=True, sort=False)

    print()
    print()
    print("Result All")
    print("**************************")
    print(resultAll)
    print()
    print()
    print("Tukey All")
    print("**************************")
    print(tukeyAll)
    print()
    print()
    print("Result Attention")
    print("**************************")
    print(resultAtt)
    print()
    print()
    print("Tukey Attention")
    print("**************************")
    print(tukeyAtt)
    if saveOWA:
        writeToFile(outputPath,filename,'All_Anova_',resultAll)
        writeToFile(outputPath,filename,'Att_Anova_',resultAtt)
        writeToFile(outputPath,filename,'All_Tukey_',tukeyAll)
        writeToFile(outputPath,filename,'Att_Tukey_',tukeyAtt)


if runTwoWay:
    raw['q_dem_movieUsage'] = raw['q_dem_movieUsage'].replace([1], 0)
    raw['q_dem_movieUsage'] = raw['q_dem_movieUsage'].replace([3], 2)
    raw['q_dem_movieUsage'] = raw['q_dem_movieUsage'].replace([5], 4)
    raw['q_dem_movieUsage'] = raw['q_dem_movieUsage'].replace([6], 4)
    raw['q_dem_movieUsage'] = raw['q_dem_movieUsage'].replace([7], 4)


    raw['q_dem_onlineUsage'] = raw['q_dem_onlineUsage'].replace([6], 4)
    raw['q_dem_onlineUsage'] = raw['q_dem_onlineUsage'].replace([7], 4)


    raw['']
    inColumn1 = 'condition'
    inColumn2 = "q_dem_onlineUsage"
    for x in combination:
        selectedD = raw[[inColumn1,inColumn2, x]]
        print(x)
        print(anova_table(runTwoAnova(selectedD, x, inColumn1,inColumn2)))
        #print(runTwoAnova(selectedD, y, inColumn1, inColumn2))
        #print(runTukey(selectedD, x, inColumn1))

if saveLog:
    sys.stdout.close()