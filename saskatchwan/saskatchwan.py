#!/usr/bin/env python3
import sys
import csv
import pandas as pd


def main(argv):
    # initializing vars
    rankF = []
    rankM = []
    rankCounterF = 1
    tiedRanksF = 0
    previousFrequencyF = -1  # formatting decision
    rankCounterM = 1
    tiedRanksM = 0
    previousFrequencyM = -1  # formatting decision
    previousYear = 2013  # the first year the data begins
    yearF = []
    nameF = []
    frequencyF = []
    yearM = []
    nameM = []
    frequencyM = []

    with open("./saskatchwan/saskatchwanTop20BabyNames.csv") as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=",")
        for row in csvReader:
            if int(row[0]) > previousYear:  # for when year increments
                # resets vars
                rankCounterF = 1
                previousFrequencyF = -1
                rankCounterM = 1
                previousFrequencyM = -1
                previousYear = int(row[0])
            if row[3] == "Female":
                # counts ranks specifically so that when there is a tie, next rank is skipped
                if previousFrequencyF == row[4]:
                    tiedRanksF += 1
                    rankF.append(rankCounterF - tiedRanksF)
                else:
                    rankF.append(rankCounterF)
                    tiedRanksF = 0
                previousFrequencyF = row[4]
                rankCounterF += 1

                # adding proper elements to the lists
                yearF.append(row[0])
                nameF.append(row[2].title())
                frequencyF.append(row[4])
            elif row[3] == "Male":
                # counts ranks specifically so that when there is a tie, next rank is skipped
                if previousFrequencyM == row[4]:
                    tiedRanksM += 1
                    rankM.append(rankCounterM - tiedRanksM)
                else:
                    rankM.append(rankCounterM)
                    tiedRanksM = 0
                previousFrequencyM = row[4]
                rankCounterM += 1

                # adding proper elements to the lists
                yearM.append(row[0])
                nameM.append(row[2].title())
                frequencyM.append(row[4])

        # data goes into dataframes then put into seperate csv files
        females = {"Rank": rankF, "Year": yearF, "Name": nameF, "Frequency": frequencyF}
        females_df = pd.DataFrame(females)
        females_df.to_csv(
            "./saskatchwan/saskatchewanFemales.csv",
            sep=",",
            index=False,
            encoding="utf-8",
        )

        males = {"Rank": rankM, "Year": yearM, "Name": nameM, "Frequency": frequencyM}
        males_df = pd.DataFrame(males)
        males_df.to_csv(
            "./saskatchwan/saskatchewanMales.csv",
            sep=",",
            index=False,
            encoding="utf-8",
        )


if __name__ == "__main__":
    main(sys.argv[1:])
