#!/bin/bash
echo Creating json dump...
docker exec -i mongo  mongoexport --uri="mongodb://root:password@localhost:27017/open-computing-nba-teams?authSource=admin" --collection "nba_teams" --type=json --jsonArray --pretty> ./db-dumps/dumpjson.json
echo Created JSON dump at $PWD/db-dumps/jsondump.json
echo Creating CSV dump...
sleep 2
python3 $PWD/mongo_to_csv.py
echo Created CSV dump at $PWD/db-dumps/csvdump.json
