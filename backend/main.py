from flask import Flask, render_template, request, Response
from pymongo import MongoClient
import json
import os
from bson import json_util
from pathlib import Path

app = Flask(__name__)



def get_mongo_db():
    CONNECTION_STRING= "mongodb://root:password@localhost:27017/open-computing-nba-teams?authSource=admin"
    client = MongoClient(CONNECTION_STRING)
    db = client["open-computing-nba-teams"]
    return db


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_file', methods=['POST'])
def create_file():
    if request.method == 'POST':
        search_field_dropdown = request.form.get('search_field_dropdown')
        input_from_search = request.form.get('input_from_search')

        input_from_search = f"^{input_from_search}"
        myquery = { search_field_dropdown: { "$regex": input_from_search, "$options" : "i"} }
        #myquery = { "conference": { "$regex": ^We } }

        nba_teams_collection = get_mongo_db()["nba_teams"]
        mydoc = nba_teams_collection.find(myquery)
        return_list_of_dicts = []
        for x in mydoc:
            return_list_of_dicts.append(x)
 
        return json.loads(json_util.dumps(return_list_of_dicts))

@app.route('/full_csv_download', methods=['GET'])
def full_csv_download():
    parent_path = Path(os.getcwd()).parent.absolute()
    csv_path = parent_path / "db-dumps" / "nba_teams.csv"
    print(csv_path)
    print(type(csv_path))
    f = open(csv_path, "r")
    lines = f.read()
    return lines

@app.route('/full_json_download', methods=['GET'])
def full_json_download():
    parent_path = Path(os.getcwd()).parent.absolute()
    json_path = parent_path / "db-dumps" / "nba_teams.json"
    print(json_path)
    print(type(json_path))
    f = open(json_path, "r")
    return json.loads(json_util.dumps(f.read()))

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )