#!/usr/bin/env python3
# This program is very similar to Nova Scotia's, look on the comments there if your confused. The only difference is some names contain an asterisk
import sys
import csv
import pandas as pd


def main(argv):
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

    with open("./california/20221107_topbabynames.csv") as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=",")
        for row in csvReader:
            if row[1] == "Female":
                if previousFrequencyF == int(row[4]):
                    tiedRanksF += 1
                    rankF.append(rankCounterF - tiedRanksF)
                else:
                    rankF.append(rankCounterF)
                    tiedRanksF = 0
                previousFrequencyF = int(row[4])
                rankCounterF += 1

                yearF.append(row[0])
                # Certain rows have an *, if so remove the asterisk
                if row[3][-1] == "*":
                    nameF.append(row[3][:-1].title())
                else:
                    nameF.append(row[3].title())
                frequencyF.append(row[4])
            elif row[1] == "Male":
                if previousFrequencyM < int(row[4]):
                    rankCounterF = 1
                    previousFrequencyF = -1
                    rankCounterM = 1
                    previousFrequencyM = -1
                if previousFrequencyM == int(row[4]):
                    tiedRanksM += 1
                    rankM.append(rankCounterM - tiedRanksM)
                else:
                    rankM.append(rankCounterM)
                    tiedRanksM = 0
                previousFrequencyM = int(row[4])
                rankCounterM += 1

                yearM.append(row[0])
                if row[3][-1] == "*":
                    nameM.append(row[3][:-1].title())
                else:
                    nameM.append(row[3].title())
                frequencyM.append(row[4])

        females = {"Rank": rankF, "Year": yearF, "Name": nameF, "Frequency": frequencyF}
        females_df = pd.DataFrame(females)
        females_df.to_csv(
            "./california/californiaFemales.csv", sep=",", index=False, encoding="utf-8"
        )

        males = {"Rank": rankM, "Year": yearM, "Name": nameM, "Frequency": frequencyM}
        males_df = pd.DataFrame(males)
        males_df.to_csv(
            "./california/californiaMales.csv", sep=",", index=False, encoding="utf-8"
        )


if __name__ == "__main__":
    main(sys.argv[1:])
