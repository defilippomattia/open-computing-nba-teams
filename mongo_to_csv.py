import csv,json

f = open("dumpjson.json")
json_dict = json.load(f)

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

#id,team,location,conference,division,year_founded,arena,arena_capacity,championships,finals_appearences,players.number,players.name,players.position
flat_properties_columns = list(json_dict[0].keys())[:-1] #without players
#print(flat_properties_columns)
nested_properties_columns = ["players."+ x for x in list(json_dict[0]["players"][0].keys())]
#print(nested_properties_columns)
column_names = flat_properties_columns + nested_properties_columns
#print(column_names)

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

for i in full_csv:
	for x in i:
		take_out.append(x)
with open("dumpcsv.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(take_out)