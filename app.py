import json
import os
import sys
import glob
import ast

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def render_steps():
    data = open('config.json')
    configuration = json.load(data)

    folder = configuration["featureFileFolder"]
    files = glob.glob("{}/*.py".format(folder))
    return render_template('step_files.html', items = files)

@app.route('/steps')
def get_features():
    data = open('config.json')
    configuration = json.load(data)

    step_file = open(configuration["stepFile"])
    step_id_dict = [{i:j} for i,j in enumerate(step_file.readlines()) if '@' in j]
    return render_template('steps.html',items = step_id_dict)

if __name__ == '__main__':
   app.run()
