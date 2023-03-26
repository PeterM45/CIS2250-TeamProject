from flask import Flask, request, render_template
import csv
import pandas as pd

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


"""
ROUTES
"""


@app.route("/")
def index():
    return render_template("./index.html")


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

    # Add elif clauses for the remaining scripts here...
    return """
          <button onclick="window.location.href='/';">Back</button> 
          <h2>Script has been run!</h2>
          """


if __name__ == "__main__":
    app.run(debug=True)
