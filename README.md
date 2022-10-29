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


|            	|                                     	|
|-------------------	|-----------------------------------------------------------	|
|**Title**      	|                      NBA Teams Dataset                      	|
|      **Description**      	|                      General information about basketball teams and players from NBA                      	|
|       **URI**       	| https://github.com/defilippomattia/open-computing-nba-teams 	|
| **Dataset Version** 	|                             1.0                             	|
|      **Author**     	|                      Mattia de Filippo                      	|
|     **Language**    	|                           English                           	|
|     **License**     	|                            CC BY                            	|
|     **Keywords**    	|                   nba, basketball, sports                   	|
|     **Publication**   |                   2022-10-29                   	|
|     **Formats**   |                   JSON, CSV                   	|


# CSV Description

| Field             	| Description                                 	| Data Type 	|
|-------------------	|---------------------------------------------	|-----------	|
| id                	| Row identifier                              	| numeric   	|
| team_id           	| Team identifier                             	| string    	|
| team_name         	| Name of the team                            	| string    	|
| location          	| City name where the team is located         	| string    	|
| conference        	| Conference in which the team is competing   	| string    	|
| division          	| Division in which the team is competing     	| string    	|
| year_founded      	| Year (YYYY) in which the team is founded    	| numeric   	|
| arena             	| Arena where team is hosting home games      	| string    	|
| arena_capacity    	| Number of seats in arena                    	| numeric   	|
| championships     	| Number of championships the team has won    	| numeric   	|
| final_appearences 	| Number of times the team appeared in finals 	| numeric   	|
| players_number    	| Players jersey number                       	| string    	|
| players_name      	| Players name                                	| string    	|
| players_position  	| Position which player is playing            	| string    	|

# JSON Description

| Field             	| Description                                                       	| Data Type 	|
|-------------------	|-------------------------------------------------------------------	|-----------	|
| _id               	| Team identifier                                                   	| string    	|
| team              	| Name of the team                                                  	| string    	|
| location          	| City name where the team is located                               	| string    	|
| conference        	| Conference in which the team is competing                         	| string    	|
| division          	| Division in which the team is competing                           	| string    	|
| year_founded      	| Year (YYYY) in which the team is founded                          	| numeric   	|
| arena             	| Arena where team is hosting home games                            	| string    	|
| arena_capacity    	| Number of seats in arena                                          	| numeric   	|
| championships     	| Number of championships the team has won                          	| numeric   	|
| final_appearences 	| Number of times the team appeared in finals                       	| numeric   	|
| players           	| List of players with data about players number, name and position 	| list      	|