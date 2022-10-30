#!/bin/bash
echo Creating json dump...
docker exec -i mongo  mongoexport --uri="mongodb://root:password@localhost:27017/open-computing-nba-teams?authSource=admin" --collection "nba_teams" --type=json --jsonArray --pretty> ./db-dumps/nba_teams.json
echo Created JSON dump at $PWD/db-dumps/nba_teams.json
echo Creating CSV dump...
sleep 2
python3 $PWD/mongo_to_csv.py
echo Created CSV dump at $PWD/db-dumps/nba_teams.csv
echo Creating db dump...
docker exec -i mongo  mongodump --archive --uri="mongodb://root:password@localhost:27017/open-computing-nba-teams?authSource=admin" --collection "nba_teams" > ./db-dumps/db.dump
echo Created db dump at $PWD/db-dumps/db.dump
