#!/usr/bin/env python3
# The purpose of this program is to remove all quotation marks and equals signs from a csv file. For some reason when I combined the csv files using command prompt quotation marks and equals signs were automatically added. Important to mention, I manually change the file that is opened and written.
import csv

with open("./southAustralia/female_cy1944-2021.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    data = []
    for row in csv_reader:
        # If the character is a quotation mark replace it for nothing same or if the character is a equals sign replace it for nothing
        row = [character.replace('"', "").replace("=", "") for character in row]
        data.append(row)

# Write the new data into another csv file
with open(
    "./southAustralia/cleaned_female_cy1944-2021.csv", "w", newline=""
) as cleaned_csv_file:
    csv_writer = csv.writer(cleaned_csv_file)
    for row in data:
        csv_writer.writerow(row)
