# open-computing-nba-teams
Open computing lab exercise at fer


# Useful commands

Kill all docker continers
docker rm -f $(docker ps -a -q)

create virutal env venv-nba
python3 -m venv venv-nba

activate virtual environemnt
source venv-nba/bin/activate

Recreate contianer
 docker-compose up -d --force-recreate


#exports to jsonarray (withot jsonArray is not "valid" json file)
 docker exec -i mongo  mongoexport --uri="mongodb://root:password@localhost:27017/open-computing-nba-teams?authSource=admin" --collection "nba_teams" --type=json --jsonArray --pretty> dumpjson.json

