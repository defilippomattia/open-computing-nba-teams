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


@app.errorhandler(405)
def not_allowed_error(error):
	final_response = {}
	final_response["status"] = "Error"
	final_response["message"] = "Method not allowed"
	final_response["response"] = None
	return Response(json_util.dumps(final_response), mimetype='application/json',status=405)
 

#638b864ab0dc209b60b9beee"

#find location of openapi.json file
#openapi_json_file = Path(__file__).parent / "openapi.json"
@app.route('/openapi')
def openapi():
	filel=  Path(__file__).parent / "openapi.json"
	return send_file("openapi.json",mimetype='application/json',status=200)


@app.route('/locations', methods=['GET'])
def get_locations():
	locations = nba_teams_collection.distinct("location")
	final_response = {}
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
@app.route('/nba-teams/<string:id>',methods=['GET','DELETE','PUT'])
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
	
	#handle PUT
	elif request.method == 'PUT':
		if(id is None):
			final_response = {}
			final_response["status"] = "Error"
			final_response["message"] = "PUT method not allowed on whole dataset"
			final_response["response"] = None
			return Response(json_util.dumps(final_response), mimetype='application/json',status=405)
		else:
			try:
				nba_teams_collection.update_one({"_id": ObjectId(id)}, {"$set": request.get_json()})
				final_response = {}
				final_response["status"] = "OK"
				final_response["message"] = "Updated NBA team with id: "+id
				final_response["response"] = None
				return Response(json_util.dumps(final_response), mimetype='application/json',status=200)
			except Exception as e:
				print(e)
				final_response = {}
				final_response["status"] = "Not Found"
				final_response["message"] = "Didn't update because NBA team with id: "+id+" not found or not valid PUT body"
				final_response["response"] = None
				return Response(json_util.dumps(final_response), mimetype='application/json',status=404)
	




if __name__ == '__main__':
	app.run(
		host='127.0.0.1',
		port=5001,
		debug=True
	)