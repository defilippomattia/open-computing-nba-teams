from flask import Flask, render_template, request, Response, send_file
from pymongo import MongoClient
import json
import os
from bson import json_util
from pathlib import Path
import re
from bson.objectid import ObjectId


app = Flask(__name__)
CONNECTION_STRING= "mongodb://root:password@localhost:27017/open-computing-nba-teams?authSource=admin"
client = MongoClient(CONNECTION_STRING)
db = client["open-computing-nba-teams"]
nba_teams_collection = db["nba_teams"]


# def get_mongo_db():
# 	CONNECTION_STRING= "mongodb://root:password@localhost:27017/open-computing-nba-teams?authSource=admin"
# 	client = MongoClient(CONNECTION_STRING)
# 	db = client["open-computing-nba-teams"]
# 	return db

#638b864ab0dc209b60b9beee"

@app.route('/locations', methods=['GET'])
def get_locations():
	locations = nba_teams_collection.distinct("location")
	final_response = {}
	for l in locations:
		print(l)
	final_response["status"] = "OK"
	final_response["message"] = "Fecthed all locations"
	final_response["response"] = locations
	return Response(json_util.dumps(final_response), mimetype='application/json',status=200)

@app.route('/players', methods=['GET'])
def get_players():
	players = nba_teams_collection.distinct("players")
	final_response = {}
	final_response["status"] = "OK"
	final_response["message"] = "Fecthed all players"
	final_response["response"] = players
	return Response(json_util.dumps(final_response), mimetype='application/json',status=200)

@app.route('/arenas', methods=['GET'])
def get_arenas():
	arenas = nba_teams_collection.distinct("arena")
	final_response = {}
	final_response["status"] = "OK"
	final_response["message"] = "Fecthed all arenas"
	final_response["response"] = arenas
	return Response(json_util.dumps(final_response), mimetype='application/json',status=200)

@app.route('/nba-teams',methods=['GET','POST'])
@app.route('/nba-teams/<string:id>',methods=['GET','DELETE'])
def index(id=None):
	print(request.args)
	#check if methos is GET
	if request.method == 'GET':
		if(id is None):
			mydoc = nba_teams_collection.find()
			print(mydoc.retrieved)
			final_response = {}
			final_response["status"] = "OK"
			final_response["message"] = "Fecthed whole NBA teams dataset"
			final_response["response"] = mydoc
			return Response(json_util.dumps(final_response), mimetype='application/json',status=200)
		else:
			try:
				nba_team_doc = [i for i in  nba_teams_collection.find({"_id": ObjectId(id)})]
				final_response = {}
				final_response["status"] = "OK"
				final_response["message"] = "Fecthed NBA team with id: "+id
				final_response["response"] = nba_team_doc
				return Response(json_util.dumps(final_response), mimetype='application/json',status=200)

			except Exception as e:
				final_response = {}
				final_response["status"] = "Not Found"
				final_response["message"] = "NBA team with provided id: "+id+" not found"
				final_response["response"] = None
				return Response(json_util.dumps(final_response), mimetype='application/json',status=404)
	#handle DELETE
	elif request.method == 'DELETE':
		if(id is None):
				final_response = {}
				final_response["status"] = "Error"
				final_response["message"] = "DELETE method not allowed on whole dataset"
				final_response["response"] = None
				return Response(json_util.dumps(final_response), mimetype='application/json',status=405)
		else:
			try:
				nba_teams_collection.delete_one({"_id": ObjectId(id)})
				final_response = {}
				final_response["status"] = "OK"
				final_response["message"] = "Deleted NBA team with id: "+id
				final_response["response"] = None
				return Response(json_util.dumps(final_response), mimetype='application/json',status=200)

			except Exception as e:
				print(e)
				final_response = {}
				final_response["status"] = "Not Found"
				final_response["message"] = "Didn't delete because NBA team with id: "+id+" not found"
				final_response["response"] = None
				return Response(json_util.dumps(final_response), mimetype='application/json',status=404)
	#handle POST
	elif request.method == 'POST':
		if(id is None):
			try:
				nba_teams_collection.insert_one(request.get_json())
				final_response = {}
				final_response["status"] = "OK"
				final_response["message"] = "Inserted NBA team"
				final_response["response"] = None
				return Response(json_util.dumps(final_response), mimetype='application/json',status=201)
			except Exception as e:
				print(e)
				final_response = {}
				final_response["status"] = "Error"
				final_response["message"] = "Didn't insert NBA team, not valid POST body"
				final_response["response"] = None
				return Response(json_util.dumps(final_response), mimetype='application/json',status=500)
		else:
			final_response = {}
			final_response["status"] = "Error"
			final_response["message"] = "POST method not allowed on specific NBA team"
			final_response["response"] = None
			return Response(json_util.dumps(final_response), mimetype='application/json',status=405)


'''
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/create_table', methods=['POST'])
def create_table():
	if request.method == 'POST':
		search_field_dropdown = request.form.get('search_field_dropdown')
		input_from_search = request.form.get('input_from_search')

		if search_field_dropdown=="all":
			rgx_str = f".*{input_from_search}.*"
			myquery = {
				'$or':[
					{"team": {'$in':[re.compile(rgx_str,flags=re.IGNORECASE)]}},
					{"arena": {'$in':[re.compile(rgx_str,flags=re.IGNORECASE)]}},
					{"location": {'$in':[re.compile(rgx_str,flags=re.IGNORECASE)]}},
					{"conference": {'$in':[re.compile(rgx_str,flags=re.IGNORECASE)]}},
					{"division": {'$in':[re.compile(rgx_str,flags=re.IGNORECASE)]}},
				]
			}
		else:
			rgx_str = f".*{input_from_search}.*"
			myquery = {search_field_dropdown: {'$in':[re.compile(rgx_str,flags=re.IGNORECASE)]}}

		nba_teams_collection = get_mongo_db()["nba_teams"]
		mydoc = nba_teams_collection.find(myquery)
		return_list_of_dicts = []

		for x in mydoc:
			for p in x["players"]:
				dict_struct = {}
				dict_struct["arena"] = x["arena"]
				dict_struct["arena_capacity"] = x["arena_capacity"]
				dict_struct["championships"] = x["championships"]
				dict_struct["team"] = x["team"]
				dict_struct["location"] = x["location"]
				dict_struct["conference"] = x["conference"]
				dict_struct["division"] = x["division"]
				dict_struct["year_founded"] = x["year_founded"]
				dict_struct["finals_appearances"] = x["finals_appearances"]

				dict_struct["players_number"] = p["number"]
				dict_struct["players_name"] = p["name"]
				dict_struct["players_position"] = p["position"]
				return_list_of_dicts.append(dict_struct)

		return json.loads(json_util.dumps(return_list_of_dicts))



'''


if __name__ == '__main__':
	app.run(
		host='127.0.0.1',
		port=5001,
		debug=True
	)