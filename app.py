# http://127.0.0.1:5000/

from flask import Flask, request, render_template, send_file, jsonify
import csv
import pandas as pd
import time
import os
import numpy as np


app = Flask(__name__)

"""
SCRIPT FUNCTIONS
"""


def run_alberta():
    exec(open("./alberta/alberta.py").read())


def run_australia():
    exec(open("./australia/australia.py").read())


def run_britishColumbia():
    exec(open("./britishColumbia/britishColumbia.py").read())


def run_california():
    exec(open("./california/california.py").read())


def run_newBrunswick():
    exec(open("./newBrunswick/newBrunswick.py").read())


def run_newfoundlandAndLabrador():
    exec(open("./newfoundlandAndLabrador/newfoundlandAndLabrador.py").read())


def run_newZealand():
    exec(open("./newZealand/newZealand.py").read())


def run_novaScotia():
    exec(open("./novaScotia/novaScotia.py").read())


def run_ontario():
    exec(open("./ontario/ontario.py").read())


def run_quebec():
    exec(open("./quebec/quebec.py").read())


def run_saskatchewan():
    exec(open("./saskatchewan/saskatchewan.py").read())


def run_southAustralia():
    exec(open("./southAustralia/southAustralia.py").read())


def run_unitedStates():
    exec(open("./unitedStates/unitedStates.py").read())


def get_common_names(country1, country2, gender, year):
    country1_names = []
    country2_names = []
    common_names = []

    with open(
        f"./{country1}/{country1}{gender.title()}.csv",
        newline="",
        encoding="iso-8859-1",
    ) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip the header row
        for row in csv_reader:
            if int(row[1]) == year:
                country1_names.append(row[2])
    with open(
        f"./{country2}/{country2}{gender.title()}.csv",
        newline="",
        encoding="iso-8859-1",
    ) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip the header row
        for row in csv_reader:
            if int(row[1]) == year:
                country2_names.append(row[2])
    for name in country1_names:
        if name in country2_names:
            common_names.append(name)
    return common_names


def most_popular_names(country, gender):
    # Load the data for the given country and gender
    df = pd.read_csv(f"{country}/{country}{gender}.csv", names=["Name", "Frequency"])

    # Remove duplicates and sort by count in descending order, then get the top 10 names
    df = df.drop_duplicates(subset=["Name"])
    df["Frequency"] = pd.to_numeric(df["Frequency"], errors="coerce")
    top_names = df.sort_values(by=["Frequency"], ascending=False).head(10)

    # Return a list of tuples containing the name and count
    return [
        (name, count) for name, count in zip(top_names["Name"], top_names["Frequency"])
    ]


"""
function
params: country, gender, year, name
def: find how many times a name exists in a given year. if it does exists
returns: frequency
"""


def name_finder(country, gender, year, name):
    df = pd.read_csv(f"{country}/{country}{gender}.csv")
    filtered_df = df[(df["year"] == year) & (df["name"] == name)]

    if filtered_df.empty:
        return -1

    count = len(filtered_df)

    return count


# Return min max
"""
function
params: country1, country2
def: read the csv file, get the lowest value for year, get the highest value for year
returns: min and max years as int
"""


def get_min_max_years(country, gender):
    df = pd.read_csv(f"{country}/{country}{gender}.csv")
    min_year = df["year"].min()
    max_year = df["year"].max()
    return min_year, max_year


"""
ROUTES
"""


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# decorator
@app.route("/")
def index():
    return render_template("./index.html")


# main script
@app.route("/run-script", methods=["POST"])
def handle_form_submission():
    script = request.form["script"]
    if script == "alberta":
        run_alberta()
    elif script == "australia":
        run_australia()
    elif script == "britishColumbia":
        run_britishColumbia()
    elif script == "california":
        run_california()
    elif script == "newBrunswick":
        run_newBrunswick()
    elif script == "newfoundlandAndLabrador":
        run_newfoundlandAndLabrador()
    elif script == "newZealand":
        run_newZealand()
    elif script == "novaScotia":
        run_novaScotia()
    elif script == "ontario":
        run_ontario()
    elif script == "quebec":
        run_quebec()
    elif script == "saskatchewan":
        run_saskatchewan()
    elif script == "southAustralia":
        run_southAustralia()
    elif script == "unitedStates":
        run_unitedStates()

    df_male = pd.read_csv(f"./{script}/{script}Males.csv", encoding="ISO-8859-1")

    df_female = pd.read_csv(f"./{script}/{script}Females.csv", encoding="ISO-8859-1")

    # Get the top 10 names for each gender
    top_male_names = df_male.head(10)
    top_female_names = df_female.head(10)

    # Get the smallest and highest years for each gender
    min_male_year = df_male["Year"].min()
    max_male_year = df_male["Year"].max()
    min_female_year = df_female["Year"].min()
    max_female_year = df_female["Year"].max()

    # Render the DataFrames as HTML tables and pass the smallest and highest years to the template
    table_male_html = top_male_names.to_html(index=False)
    table_female_html = top_female_names.to_html(index=False)
    return render_template(
        "countryRan.html",
        tableMale=table_male_html,
        tableFemale=table_female_html,
        script=script,
        minMaleYear=min_male_year,
        maxMaleYear=max_male_year,
        minFemaleYear=min_female_year,
        maxFemaleYear=max_female_year,
    )


@app.route("/download-csv/<string:gender>/<string:script>")
def download_csv(gender, script):
    filename = f"{script}/{script}{gender.capitalize()}s.csv"
    return send_file(filename, as_attachment=True)


@app.route(
    "/common_names/<string:script>/<string:latestCountry>/<string:gender>/<int:year>"
)
def common_names(script, latestCountry, gender, year):
    commonNames = get_common_names(script, latestCountry, gender, year)

    return render_template(
        "common_names.html",
        country1=script,
        country2=latestCountry,
        gender=gender,
        year=year,
        common_names=commonNames,
    )


@app.route("/graphs")
def show_graphs():
    graph_dir = "./static/graphs"
    graph_files = os.listdir(graph_dir)
    return render_template("graphs.html", graph_files=graph_files)


@app.route("/popular_names/<country>/<gender>")
def popular_names(country, gender):
    top_names = most_popular_names(country, gender)
    return render_template(
        "popular_names.html", country=country, gender=gender, top_names=top_names
    )


@app.route("/name_finder/<country>/<gender>/<year>/<name>")
def name_finder(country, gender, year, name):
    df = pd.read_csv(f"{country}/{country}{gender}.csv", encoding="ISO-8859-1")
    filtered_df = df[(df["Year"] == int(year)) & (df["Name"] == name)]
    name_count = filtered_df["Frequency"].values[0] if not filtered_df.empty else -1

    return render_template(
        "name_finder.html",
        country=country,
        gender=gender,
        year=year,
        name=name,
        name_count=name_count,
    )


@app.route("/get-year-range", methods=["GET", "POST"])
def get_year_range():
    latest_country = request.args.get("latestCountry")
    script = request.args.get("script")

    # Read in the CSV data
    df_male = pd.read_csv(f"./{script}/{script}Males.csv", encoding="ISO-8859-1")
    df_female = pd.read_csv(f"./{script}/{script}Females.csv", encoding="ISO-8859-1")
    df_latest_male = pd.read_csv(
        f"./{latest_country}/{latest_country}Males.csv", encoding="ISO-8859-1"
    )
    df_latest_female = pd.read_csv(
        f"./{latest_country}/{latest_country}Females.csv", encoding="ISO-8859-1"
    )

    # Find the minimum and maximum years in the data
    min_year = max(
        df_male["Year"].min(),
        df_female["Year"].min(),
        df_latest_male["Year"].min(),
        df_latest_female["Year"].min(),
    )
    max_year = min(
        df_male["Year"].max(),
        df_female["Year"].max(),
        df_latest_male["Year"].max(),
        df_latest_female["Year"].max(),
    )

    # Filter the data by gender and year
    if "year" in request.form:
        year = int(request.form["year"])
        male_filter = df_male["Year"] == year
        female_filter = df_female["Year"] == year
        latest_male_filter = df_latest_male["Year"] >= year
        latest_female_filter = df_latest_female["Year"] >= year
    else:
        male_filter = df_male["Year"] == df_male["Year"].min()
        female_filter = df_female["Year"] == df_female["Year"].min()
        latest_male_filter = df_latest_male["Year"] >= df_latest_male["Year"].min()
        latest_female_filter = (
            df_latest_female["Year"] >= df_latest_female["Year"].min()
        )

    # Return the result
    return jsonify({"minYear": int(min_year), "maxYear": int(max_year)})


if __name__ == "__main__":
    app.run(debug=True)
