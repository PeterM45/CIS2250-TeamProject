import pandas as pd

# Read baby names from 1952-2021
df = pd.read_csv("./australia/popular_baby_names_1952_to_2021.csv")
# remove any whitespace and change case of name
df["Name"] = df["Name"].str.strip().str.title()

# separate by gender
boys_df = df[df["Gender"] == "Male"]
girls_df = df[df["Gender"] == "Female"]

boys_df = df[df["Gender"] == "Male"].copy()
girls_df = df[df["Gender"] == "Female"].copy()

# calculate ranks for boys and girls separately
boys_df.loc[:, "Rank"] = (
    boys_df.groupby("Year")["Count"].rank(ascending=False, method="dense").astype(int)
)
girls_df.loc[:, "Rank"] = (
    girls_df.groupby("Year")["Count"].rank(ascending=False, method="dense").astype(int)
)

# create csv files for genders
boys_df[["Rank", "Year", "Name", "Count"]].rename(
    columns={"Count": "Frequency"}
).to_csv("./australia/australiaMales.csv", index=False, line_terminator="\n")
girls_df[["Rank", "Year", "Name", "Count"]].rename(
    columns={"Count": "Frequency"}
).to_csv("./australia/australiaFemales.csv", index=False, line_terminator="\n")
