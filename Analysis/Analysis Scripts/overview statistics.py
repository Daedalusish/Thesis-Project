import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

'''Summarize the samples based on value. Hindsight is that I probably should've just generated a full table instead
of this abomination'''

localPath = ""
#demographic = ['q_dem_onlineUsage','q_dem_movieUsage','c_ageGroup','c_dem_genderCat']
raw = pd.read_csv(localPath)
rawAtt = raw[raw.v_attention2 != False]
filterby = 'c_dem_genderCat'
filtervalue = 2

CondAX = raw[raw['condition'].isin([1,2,3])]
CondAX = CondAX[CondAX[filterby].isin([filtervalue])]
CondBX = raw[raw['condition'].isin([3,5,6])]
CondBX = CondBX[CondBX[filterby].isin([filtervalue])]
CondA1X = raw[raw['condition'].isin([1])]
CondA1X = CondA1X[CondA1X[filterby].isin([filtervalue])]
CondA2X = raw[raw['condition'].isin([2])]
CondA2X = CondA2X[CondA2X[filterby].isin([filtervalue])]
CondA3X = raw[raw['condition'].isin([3])]
CondA3X = CondA3X[CondA3X[filterby].isin([filtervalue])]
CondB1X = raw[raw['condition'].isin([4])]
CondB1X = CondB1X[CondB1X[filterby].isin([filtervalue])]
CondB2X = raw[raw['condition'].isin([5])]
CondB2X = CondB2X[CondB2X[filterby].isin([filtervalue])]
CondB3X = raw[raw['condition'].isin([6])]
CondB3X = CondB3X[CondB3X[filterby].isin([filtervalue])]
Cond1X = raw[raw['condition'].isin([1,4])]
Cond1X = Cond1X[Cond1X[filterby].isin([filtervalue])]
Cond2X = raw[raw['condition'].isin([2,5])]
Cond2X = Cond2X[Cond2X[filterby].isin([filtervalue])]
Cond3X = raw[raw['condition'].isin([3,6])]
Cond3X = Cond3X[Cond3X[filterby].isin([filtervalue])]

CondAY = rawAtt[rawAtt['condition'].isin([1,2,3])]
CondAY = CondAY[CondAY[filterby].isin([filtervalue])]
CondBY = rawAtt[rawAtt['condition'].isin([3,5,6])]
CondBY = CondBY[CondBY[filterby].isin([filtervalue])]
CondA1Y = rawAtt[rawAtt['condition'].isin([1])]
CondA1Y = CondA1Y[CondA1Y[filterby].isin([filtervalue])]
CondA2Y = rawAtt[rawAtt['condition'].isin([2])]
CondA2Y = CondA2Y[CondA2Y[filterby].isin([filtervalue])]
CondA3Y = rawAtt[rawAtt['condition'].isin([3])]
CondA3Y = CondA3Y[CondA3Y[filterby].isin([filtervalue])]
CondB1Y = rawAtt[rawAtt['condition'].isin([4])]
CondB1Y = CondB1Y[CondB1Y[filterby].isin([filtervalue])]
CondB2Y = rawAtt[rawAtt['condition'].isin([5])]
CondB2Y = CondB2Y[CondB2Y[filterby].isin([filtervalue])]
CondB3Y = rawAtt[rawAtt['condition'].isin([6])]
CondB3Y = CondB3Y[CondB3Y[filterby].isin([filtervalue])]
Cond1Y = rawAtt[rawAtt['condition'].isin([1,4])]
Cond1Y = Cond1Y[Cond1Y[filterby].isin([filtervalue])]
Cond2Y = rawAtt[rawAtt['condition'].isin([2,5])]
Cond2Y = Cond2Y[Cond2Y[filterby].isin([filtervalue])]
Cond3Y = rawAtt[rawAtt['condition'].isin([3,6])]
Cond3Y = Cond3Y[Cond3Y[filterby].isin([filtervalue])]


All = [CondAX,CondBX,CondA1X,CondA2X,CondA3X,CondB1X,CondB2X,CondB3X,Cond1X,Cond2X,Cond3X]
label = ['Condition A','Condition B','A-1','A-2','A-3','B-1','B-2','B-3','list 1','List 2','List 3']
Attention =[CondAY,CondBY,CondA1Y,CondA2Y,CondA3Y,CondB1Y,CondB2Y,CondB3Y,Cond1Y,Cond2Y,Cond3Y]

for x in range(0,len(All)):
    print("All - " + label[x] + " Samples: " + str(All[x].shape[0]))

for x in range(0,len(All)):
    print("Attention - " + label[x] + " Samples: " + str(Attention[x].shape[0]))