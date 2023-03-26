#!/usr/bin/env python3

# Libraries
import sys
import csv
import pandas as pd


def main(argv):
    # initializing variables
    rankF = []
    rankM = []
    rankCounterF = 1
    tiedRanksF = 0
    previousFrequencyF = -1
    rankCounterM = 1
    tiedRanksM = 0
    previousFrequencyM = -1
    previousYearM = 1917
    previousYearF = 1913
    yearF = []
    nameF = []
    frequencyF = []
    yearM = []
    nameM = []
    frequencyM = []

    with open(
        "./ontario/ontario_top_baby_names_female_1917-2019_en_fr.csv"
    ) as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=",")
        for row in csvReader:
            if int(row[0]) > previousYearF:  # for when year increments
                # resets vars
                rankCounterF = 1
                previousFrequencyF = -1
                previousYearF = int(row[0])
            # handles ties in rank
            if previousFrequencyF == int(row[2]):
                tiedRanksF += 1
                rankF.append(rankCounterF - tiedRanksF)
            else:
                rankF.append(rankCounterF)
                tiedRanksF = 0
            previousFrequencyF = int(row[2])
            rankCounterF += 1
            # stores data in lists
            yearF.append(row[0])
            nameF.append(row[1].title())
            frequencyF.append(row[2])
    with open(
        "./ontario/ontario_top_baby_names_male_1917-2019_en_fr.csv"
    ) as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=",")
        for row in csvReader:
            if int(row[0]) > previousYearM:  # for when year increments
                # resets vars
                rankCounterM = 1
                previousFrequencyM = -1
                rankCounterM = 1
                previousYearM = int(row[0])
            if previousFrequencyM < int(row[2]):
                rankCounterF = 1
                previousFrequencyF = -1
                rankCounterM = 1
                previousFrequencyM = -1
            if previousFrequencyM == int(row[2]):
                tiedRanksM += 1
                rankM.append(rankCounterM - tiedRanksM)
            else:
                rankM.append(rankCounterM)
                tiedRanksM = 0
            previousFrequencyM = int(row[2])
            rankCounterM += 1
            # stores data in lists
            yearM.append(row[0])
            nameM.append(row[1].title())
            frequencyM.append(row[2])

        females = {"Rank": rankF, "Year": yearF, "Name": nameF, "Frequency": frequencyF}
        females_df = pd.DataFrame(females)
        females_df.to_csv(
            "./ontario/ontarioFemales.csv", sep=",", index=False, encoding="utf-8"
        )

        males = {"Rank": rankM, "Year": yearM, "Name": nameM, "Frequency": frequencyM}
        males_df = pd.DataFrame(males)
        males_df.to_csv(
            "./ontario/ontarioMales.csv", sep=",", index=False, encoding="utf-8"
        )


if __name__ == "__main__":
    main(sys.argv[1:])
