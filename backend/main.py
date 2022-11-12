from flask import Flask, render_template, request
from pymongo import MongoClient
import json
from bson import json_util

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

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )