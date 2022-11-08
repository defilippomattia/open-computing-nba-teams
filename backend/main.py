from flask import Flask, render_template, request
from pymongo import MongoClient

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
        #print("xmattia................................")
        #print(request)
        #print(request.form.get('search_field_dropdown'))
        #print(request.form)
        search_field_dropdown = request.form.get('search_field_dropdown')
        input_from_search = request.form.get('input_from_search')
        #print(input_from_search)
        #print(search_field_dropdown)

        input_from_search = f"^{input_from_search}"
        myquery = { search_field_dropdown: { "$regex": input_from_search, "$options" : "i"} }
        #myquery = { "conference": { "$regex": ^We } }

        nba_teams_collection = get_mongo_db()["nba_teams"]

        mydoc = nba_teams_collection.find(myquery)
        for x in mydoc:
            print(x)
            print("--------------------------")

        with open(f"{request.form.get('name')}.txt", "w") as f:
            f.write('FILE CREATED AND SUCCESSFULL POST REQUEST!')
        return ('', 204)

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )