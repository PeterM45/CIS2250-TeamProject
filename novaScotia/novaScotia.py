#!/usr/bin/env python3
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
    
    with open ( "NS_Top_Twenty_Baby_Names_-_1920-Current.csv" ) as csvDataFile:
        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if row[1] == 'F':
                #If there is a tie in frequency then subtract one from the rank (per tie) to make the rank the same
                if previousFrequencyF == int(row[3]):
                    tiedRanksF += 1
                    rankF.append(rankCounterF-tiedRanksF)
                else:
                    rankF.append(rankCounterF)
                    tiedRanksF = 0 #Set back to 0 so the subtraction isn't overlapped with the next tie
                previousFrequencyF = int(row[3])
                rankCounterF +=1

                yearF.append(row[0])
                nameF.append(row[2].title())#.title() capitalizes the names appropriately
                frequencyF.append(row[3])
            elif row[1] == 'M':
                #Since each year starts with a male check only when a male row is being read. When the year does change, reset rank calculation variables
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

      #Write the lists into two output csv files
        females = {'Rank':rankF,'Year':yearF,'Name':nameF,'Frequency':frequencyF}
        females_df = pd.DataFrame(females)
        females_df.to_csv("novaScotiaFemales.csv", sep=',', index=False, encoding='utf-8')

        males = {'Rank':rankM,'Year':yearM,'Name':nameM,'Frequency':frequencyM}
        males_df = pd.DataFrame(males)
        males_df.to_csv("novaScotiaMales.csv", sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
    main ( sys.argv[1:] )