## TO RUN CODE: python ./britishColumbia.py bc-popular-boys-names.csv bc-popular-girls-names.csv
import csv
import time

start_time = time.time()


class Person:
    __slots__ = ("name", "years", "rank")

    # Define __init__ method
    def __init__(self, name):
        self.name = name
        self.years = {}  # Initialize empty dictionary for years
        self.rank = {}  # Initialize empty dictionary for rank

    # Define method to update year and frequency
    def updateYears(self, year, frequency):
        self.years[year] = frequency

    # Define method to update year and rank
    def updateRank(self, year, rank):
        self.rank[year] = rank

    # Define method to return years
    def getYears(self):
        return self.years

    # Define method to return rank for a specific year
    def getRank(self, year):
        return self.rank[year]


# Define function to sort people based on frequency
def sortFrequency(person, year):
    years = person.years
    if year in years:
        return (-int(years[year]), person.name, ord(person.name[0]))
    else:
        return (0, person.name, ord(person.name[0]))


# Define main
def main(argv, fn, index):
    # Initialize lists
    people = []
    names = {}
    # Define variables
    start_year = 1922
    end_year = 2022
    count = 0
    filename = argv[index]
    # Open csv file using encoding
    with open(filename, encoding="windows-1252") as csvfile:
        # Read csv file using csv.reader
        reader = csv.reader(csvfile)
        # Iterate through each row in csv file
        for row in reader:
            if row[0] != "Name":
                person = Person(row[0])
                years = person.years
                for year in range(start_year, end_year):
                    years[year] = row[year - start_year + 2].replace(",", "")
                # Append person to people list
                people.append(person)
                # Add person's name to names dictionary with value as count
                names[row[0]] = count
                count += 1

    # Iterate through years from start_year to end_year
    for year in range(start_year, end_year):
        sortedFrequencyPeople = sorted(people, key=lambda x: sortFrequency(x, year))
        for j, person in enumerate(sortedFrequencyPeople, 1):
            people[names[person.name]].updateRank(year, j)

    # Write output to csv file
    with open(fn, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Rank", "Year", "Name", "Frequency"])
        # Loop iterates over each year.
        for year in range(start_year, end_year):
            temp = -1
            new_rank = 0
            rankedList = [
                (person.name, person.getRank(year))
                for person in people
                if year in person.rank
            ]
            rankedList.sort(key=lambda x: x[1])
            for person in rankedList:
                years = people[names[person[0]]].getYears()
                if temp == -1:
                    temp = years[year]
                    new_rank = 1
                else:
                    if temp != years[year]:
                        temp = years[year]
                        new_rank += 1

                if years[year] != "0":
                    writer.writerow([new_rank, year, person[0].title(), years[year]])


if __name__ == "__main__":
    import sys

    # Sets the output file names
    main(sys.argv, "./britishColumbia/britishColumbiaMales.csv", 1)
    main(sys.argv, "./britishColumbia/britishColumbiaFemales.csv", 2)
