from flask import Flask, render_template, request, Response
from pymongo import MongoClient
import json
import os,bson
from bson import json_util
from pathlib import Path
import re



def get_mongo_db():
	CONNECTION_STRING= "mongodb://root:password@localhost:27017/open-computing-nba-teams?authSource=admin"
	client = MongoClient(CONNECTION_STRING)
	db = client["open-computing-nba-teams"]
	return db

nba_teams_collection = get_mongo_db()["nba_teams"]
#myquery = {team: {$regex : /avs/i}}
#regx = bson.regex.Regex('^Tor')
myquery = {'players.name': {'$in': [ re.compile('.*geo*',flags=re.IGNORECASE)]}}
mydoc = nba_teams_collection.find(myquery)
for x in mydoc:
    print("........")
    print(x)