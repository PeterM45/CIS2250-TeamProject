#!/usr/bin/env python3
import sys
import csv
import pandas as pd


def main(argv):
    # Initialize empty lists and counters
    rankF = []
    rankM = []
    rankCounterF = 1
    tiedRanksF = 0
    previousFrequencyF = -1
    rankCounterM = 1
    tiedRanksM = 0
    previousFrequencyM = -1
    currentYear = 1880
    yearF = []
    nameF = []
    frequencyF = []
    yearM = []
    nameM = []
    frequencyM = []
    previousGender = "F"

    # Open and read the csv file containing the data
    with open("./unitedStates/yob1880-2021.txt") as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=",")
        for row in csvReader:
            if row[1] == "F":
                if (
                    previousGender == "M"
                ):  # The file changes years when it shows males again
                    # Set all counters that calculate rank and rank ties to neutral values
                    rankCounterF = 1
                    previousFrequencyF = -1
                    rankCounterM = 1
                    previousFrequencyM = -1
                    currentYear += 1  # Year isn't shown in the csv file so we manually incremement by one; the year change is shown by the frequency jumping up suddenly
                if previousFrequencyF == row[2]:
                    tiedRanksF += 1
                    rankF.append(rankCounterF - tiedRanksF)
                else: #If current frequency is different from previous frequency
                    rankF.append(rankCounterF)
                    tiedRanksF = 0
                previousFrequencyF = row[2]
                rankCounterF += 1
                yearF.append(currentYear)
                nameF.append(row[0].title())
                frequencyF.append(row[2])
                previousGender = row[1]
            elif row[1] == "M":
                if previousFrequencyM == row[2]:
                    tiedRanksM += 1
                    rankM.append(rankCounterM - tiedRanksM)
                else: #If current frequency is different from previous frequency
                    rankM.append(rankCounterM)
                    tiedRanksM = 0
                previousFrequencyM = row[2]
                rankCounterM += 1

                yearM.append(currentYear) # Append the current year to the year list for males
                nameM.append(row[0].title())
                frequencyM.append(row[2])
            previousGender = row[1]

        females = {"Rank": rankF, "Year": yearF, "Name": nameF, "Frequency": frequencyF}
        females_df = pd.DataFrame(females)
        females_df.to_csv(
            "./unitedStates/unitedStatesFemales.csv",
            sep=",",
            index=False,
            encoding="utf-8",
        )

        males = {"Rank": rankM, "Year": yearM, "Name": nameM, "Frequency": frequencyM}
        males_df = pd.DataFrame(males)
        males_df.to_csv(
            "./unitedStates/unitedStatesMales.csv",
            sep=",",
            index=False,
            encoding="utf-8",
        )


if __name__ == "__main__":
    main(sys.argv[1:])
