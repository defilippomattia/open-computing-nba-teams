from flask import Flask, render_template, request, Response
from pymongo import MongoClient
import json
import os
from bson import json_util
from pathlib import Path
import re

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

@app.route('/filtered_json_download', methods=['POST'])
def filtered_json_download():
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

@app.route('/filtered_csv_download', methods=['POST'])
def filtered_csv_download():
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
		
		return convert_to_csv(json.loads(json_util.dumps(return_list_of_dicts)))


def flatten_csv(csv_with_dict_inside):
	multiple_lines = []

	players = csv_with_dict_inside[-1]
	for x in players:
		base = csv_with_dict_inside[:-1]
		base.append(x["number"])
		base.append(x["name"])
		base.append(x["position"])
		multiple_lines.append(base)
	return multiple_lines

def convert_to_csv(received_dict):
	json_dict = received_dict
	flat_properties_columns = list(json_dict[0].keys())[:-1] #without players
	nested_properties_columns = ["players."+ x for x in list(json_dict[0]["players"][0].keys())]
	column_names = flat_properties_columns + nested_properties_columns
	almost_csv = []
	org_keys = list(json_dict[0].keys())
	for one_dict in json_dict:
		one_row = []
		for element in one_dict.keys():
			if element == "_id":
				one_row.append(one_dict[element]["$oid"])
			elif element in ["year_founded","arena_capacity","championships","finals_appearances"]:
					one_row.append(int(one_dict[element]))
			else:
				one_row.append(one_dict[element])
		almost_csv.append(one_row)

	full_csv = []
	for x in almost_csv:
		multiple_lines = flatten_csv(x)
		full_csv.append(multiple_lines)

	take_out = []

	csv_string=""
	for i in full_csv:
		print(i)
		print("..............................")
		for x in i:
			take_out.append(x)
	
	for idx,x in enumerate(take_out):
		x.insert(0,idx)
		print(x)
		csv_string = csv_string +','.join(str(v) for v in x) + '\n'
	

	return csv_string

if __name__ == '__main__':
	app.run(
		host='127.0.0.1',
		port=5001,
		debug=True
	)