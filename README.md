# open-computing-nba-teams
Open computing lab exercise at fer

# Tools used
Docker version 20.10.17  
Docker Compose version v2.6.1  
Python 3.8

# Starting mongo container
`git clone https://github.com/defilippomattia/open-computing-nba-teams.git`  
`cd open-computing-nba-teams/`  
`docker-compose --file ./Docker/docker-compose.yml up -d`

# Creating JSON & CSV dumps
`chmod +x create_dumps.sh`  
`./create_dumps.sh`

The `.csv` and `.json` file will be stored at `./open-computing-nba-teams/db-dumps`

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
 docker exec -i mongo  mongoexport --uri="mongodb://root:password@localhost:27017/open-computing-nba-teams?authSource=admin" --collection "nba_teams" --type=json --jsonArray --pretty> ../db-dumps/dumpjson.json


