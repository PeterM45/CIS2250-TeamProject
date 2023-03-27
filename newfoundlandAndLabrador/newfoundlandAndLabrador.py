# command to run: python NewfoundlandAndLabrador.py
# program reads file names from current working directory
import os
import pandas as pd

# get the working directory of python code and files
source_dir = os.getcwd() + "/newfoundlandAndLabrador"


# Output file names
boys_output_file = "./newfoundlandAndLabrador/newfoundlandAndLabradorMales.csv"
girls_output_file = "./newfoundlandAndLabrador/newfoundlandAndLabradorFemales.csv"

# Create dataframes for the boys and girls data
boys_data = pd.DataFrame(columns=["Rank", "Year", "Name", "Frequency"])
girls_data = pd.DataFrame(columns=["Rank", "Year", "Name", "Frequency"])

# Loop through each file from the working source directory. Each time one file is read from directory.
for filename in os.listdir(source_dir):

    # Read all csv file names starting with Top100BabyNames
    if filename.startswith("Top100BabyNames") and filename.endswith(".csv"):
        # Extract the year from the filename based on its position
        if len(filename) == 28:
            year = filename[20:24]
        else:
            year = filename[15:19]

        # Read the source file into a dataframe (skip header row)
        filepath = os.path.join(source_dir, filename)
        with open(filepath) as f:
            first_line = f.readline().strip()

        # If the file read has the below header type:
        if first_line == "BoysName,Rank,GirlsName":
            source_data = pd.read_csv(
                filepath,
                header=None,
                skiprows=1,
                names=["BoysName", "Rank", "GirlsName"],
            )

            # each name begins with upper case
            source_data["BoysName"] = source_data["BoysName"].str.title()
            source_data["GirlsName"] = source_data["GirlsName"].str.title()

            # Separate the data by gender and add a Year column
            # year = filename[15:19]
            # Frequency is not known to us hence -1 is assigned, and rename each GenderName column to Name
            boys_data = pd.concat(
                [
                    boys_data,
                    source_data[["Rank", "BoysName"]]
                    .rename(columns={"BoysName": "Name"})
                    .assign(Frequency="-1", Year=year),
                ]
            )
            girls_data = pd.concat(
                [
                    girls_data,
                    source_data[["Rank", "GirlsName"]]
                    .rename(columns={"GirlsName": "Name"})
                    .assign(Frequency="-1", Year=year),
                ]
            )
        # Else, if file has the other header type:
        elif first_line == "BoysRank,BoysName,GirlsRank,GirlsName":
            source_data = pd.read_csv(
                filepath,
                header=None,
                skiprows=1,
                names=["BoysRank", "BoysName", "GirlsRank", "GirlsName"],
            )

            # each name begins with upper case
            source_data["BoysName"] = source_data["BoysName"].str.title()
            source_data["GirlsName"] = source_data["GirlsName"].str.title()

            # Separate the data by gender and add a Year column
            # year = filename[15:19]

            # Frequency is not known to us hence -1 is assigned, and rename each GenderName column to Name and each GenderRank to Rank

            boys_data = pd.concat(
                [
                    boys_data,
                    source_data[["BoysRank", "BoysName"]]
                    .rename(columns={"BoysRank": "Rank", "BoysName": "Name"})
                    .assign(Frequency="-1", Year=year),
                ]
            )
            girls_data = pd.concat(
                [
                    girls_data,
                    source_data[["GirlsRank", "GirlsName"]]
                    .rename(columns={"GirlsRank": "Rank", "GirlsName": "Name"})
                    .assign(Frequency="-1", Year=year),
                ]
            )
        else:
            print(f"Unknown header format in file {filename}. Skipping...")

# Write the data to the output files
print("Target Boys CSV file generated successfully.")
boys_data.to_csv(boys_output_file, index=False)
print("Target Girls CSV file generated successfully.")
girls_data.to_csv(girls_output_file, index=False)
