import csv
import time

start_time = time.time()

class Person:
    __slots__ = ('name', 'years', 'rank')

    def __init__(self, name):
        self.name = name
        self.years = {}
        self.rank = {}

    def updateYears(self, year, frequency):
        self.years[year] = frequency

    def updateRank(self, year, rank):
        self.rank[year] = rank

    def getYears(self):
        return self.years

    def getRank(self, year):
        return self.rank[year]

def sortFrequency(person, year):
    years = person.years
    if year in years:
        return (-int(years[year]), person.name, ord(person.name[0]))
    else:
        return (0, person.name, ord(person.name[0]))

def main(argv, fn, index):
  people = []
  names = {}
  start_year = 1980
  end_year = 2022
  count = 0
  filename = argv[index]
  
  with open(filename,encoding="windows-1252") as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
          if row[0] != "Prénom/Année":
              person = Person(row[0])
              years = person.years
              for year in range(start_year, end_year):
                  years[year] = row[year - start_year + 2].replace(',', '')
              people.append(person)
              names[row[0]] = count
              count += 1
  
  for year in range(start_year, end_year):
      sortedFrequencyPeople = sorted(people, key=lambda x: sortFrequency(x, year))
      for j, person in enumerate(sortedFrequencyPeople, 1):
          people[names[person.name]].updateRank(year, j)
  
  
  with open(fn, 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(["Rank", "Year", "Name", "Frequency"])
     for year in range(start_year, end_year):
      rankedList = [(person.name, person.getRank(year)) for person in people if year   in person.rank]
      rankedList.sort(key=lambda x: x[1])
      for person in rankedList:
          years = people[names[person[0]]].getYears()
          writer.writerow([person[1], year, person[0].title(), years[year]])
    
  
if __name__ == "__main__":
    import sys
    # Sets the output file names
    main(sys.argv, "quebecMales.csv", 1)
    main(sys.argv, "quebecFemales.csv", 2)