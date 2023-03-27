#!/usr/bin/env python3
# This program locates the most popular name of a given year, gender and country
import sys
import csv
import pandas as pd

country = "california"
gender = "females"
year = 1984
with open("./", country, "/", country, gender.title()) as csvDataFile:
    next(csvDataFile)
    csvReader = csv.reader(csvDataFile, delimiter=",")
    for row in csvReader:
        if int(row[1]) == year:
            if int(row[1]) == 1:
                popularName = row[2]
                popularFrequency = row[3]
print(
    "The most popular name of",
    year,
    "is",
    popularName,
    "with a frequency of",
    popularFrequency,
)
