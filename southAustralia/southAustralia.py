#!/usr/bin/env python3
import sys
import csv
import pandas as pd

def main (argv):
    currentYear = 1944
    previousRank = 10 #10 is greater than the first rank 
    yearF = []
    nameF = []
    frequencyF = []
    rankF = []
    yearM = []
    nameM = []
    frequencyM = []
    rankM = []
    
    with open ( "cleaned_female_cy1944-2021.csv" ) as csvDataFile:
        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            #If the rank goes down it infers that the next year is being shown, thus change year
            if previousRank < int(row[2]):
                currentYear += 1
            nameF.append(row[0].title())
            yearF.append(currentYear)
            frequencyF.append(row[1])
            rankF.append(row[2])
            previousRank = int(row[2])

    currentYear=1944
    previousRank = 10
    with open ( "cleaned_male_cy1944-2021.csv" ) as csvDataFile:
        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if previousRank < int(row[2]):
                currentYear += 1
            nameM.append(row[0].title())
            yearM.append(currentYear)
            frequencyM.append(row[1])
            rankM.append(row[2])
            previousRank = int(row[2])


        females = {'Rank':rankF,'Year':yearF,'Name':nameF,'Frequency':frequencyF}
        females_df = pd.DataFrame(females)
        females_df.to_csv("southAustraliaFemales.csv", sep=',', index=False, encoding='utf-8')

        males = {'Rank':rankM,'Year':yearM,'Name':nameM,'Frequency':frequencyM}
        males_df = pd.DataFrame(males)
        males_df.to_csv("southAustraliaMales.csv", sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
    main ( sys.argv[1:] )