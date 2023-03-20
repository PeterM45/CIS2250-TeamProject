#!/usr/bin/env python3
#This program is the exact same to Nova Scotia's if your confused look at the comments there
import sys
import csv
import pandas as pd

def main (argv):
    rankF = []
    rankM = []
    rankCounterF = 1
    tiedRanksF = 0
    previousFrequencyF = -1
    rankCounterM = 1
    tiedRanksM = 0
    previousFrequencyM = -1
    yearF = []
    nameF = []
    frequencyF = []
    yearM = []
    nameM = []
    frequencyM = []
    
    with open ( "NB_Top_20_Popular_Baby_Names_1980-2018___Les_20_noms_de_b_b__populaire_au_N.-B._1980-2018.csv" ) as csvDataFile:
        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if row[1] == 'F':
                if previousFrequencyF == int(row[3]):
                    tiedRanksF += 1
                    rankF.append(rankCounterF-tiedRanksF)
                else:
                    rankF.append(rankCounterF)
                    tiedRanksF = 0
                previousFrequencyF = int(row[3])
                rankCounterF +=1

                yearF.append(row[0])
                nameF.append(row[2].title())
                frequencyF.append(row[3])
            elif row[1] == 'M':
                if previousFrequencyM < int(row[3]):
                    rankCounterF = 1
                    previousFrequencyF = -1
                    rankCounterM = 1
                    previousFrequencyM = -1
                if previousFrequencyM == int(row[3]):
                    tiedRanksM += 1
                    rankM.append(rankCounterM-tiedRanksM)
                else:
                    rankM.append(rankCounterM)
                    tiedRanksM = 0
                previousFrequencyM = int(row[3])
                rankCounterM +=1
                
                yearM.append(row[0])
                nameM.append(row[2].title())
                frequencyM.append(row[3])

        females = {'Rank':rankF,'Year':yearF,'Name':nameF,'Frequency':frequencyF}
        females_df = pd.DataFrame(females)
        females_df.to_csv("newBrunkswickFemales.csv", sep=',', index=False, encoding='utf-8')

        males = {'Rank':rankM,'Year':yearM,'Name':nameM,'Frequency':frequencyM}
        males_df = pd.DataFrame(males)
        males_df.to_csv("newBrunkswickMales.csv", sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
    main ( sys.argv[1:] )