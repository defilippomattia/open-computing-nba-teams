# Open Computing - NBA Teams
This is a publicly available dataset repository made at Open Computing course lab at University of Zagreb, Faculty of Electrical Engineering and Computing (FER). The dataset provides information about the teams and players in NBA. At the moment, there are 10 teams available and 3 players are listed for each team.
# Dataset 
|            	|                                     	|
|-------------------	|-----------------------------------------------------------	|
|**Title**      	|                      NBA Teams Dataset                      	|
|      **Description**      	|                      General information about basketball teams and players from NBA                      	|
|       **URI**       	| https://github.com/defilippomattia/open-computing-nba-teams 	|
| **Dataset Version** 	|                             1.0                             	|
|      **Author**     	|                      Mattia de Filippo                      	|
|     **Language**    	|                           English                           	|
|     **License**     	|                            CC BY-SA 3.0                            	|
|     **Keywords**    	|                   nba, basketball, sports                   	|
|     **Publication**   |                   2022-10-29                   	|
|     **Formats**   |                   JSON, CSV                   	|
<br>  

## CSV Description

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
<br>  

## JSON Description


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

<br>  

# Tools used
Docker version 20.10.17  
Docker Compose version v2.6.1  
Python 3.8

# Creating JSON & CSV dumps

Database dumps (in JSON and CSV) are already available in `./open-computing-nba-teams/db-dumps`, to recreate them, follow the steps:  

`git clone https://github.com/defilippomattia/open-computing-nba-teams.git`  
`cd open-computing-nba-teams/`  
`docker-compose --file ./Docker/docker-compose.yml up -d`  
`chmod +x create_dumps.sh`  
`./create_dumps.sh`

The `.csv` and `.json` file will be stored at `./open-computing-nba-teams/db-dumps`


# Attribution

Wikipedia, National Basketball Association, accessed 29 October 2022, https://en.wikipedia.org/wiki/National_Basketball_Association

The Sporting News, Gilbert McGregor, NBA Finals winners by team: Where Warriors, Celtics, Lakers and more land on all-time championship list, accessed 29 October 2022, https://www.sportingnews.com/us/nba/news/nba-finals-most-championships-by-team-list/qjornvbimtx59sqitrtkxggl


NBA, NBA ROSTERS SET FOR 2022-23 REGULAR SEASON, accessed 29 October 2022, https://www.nba.com/news/nba-rosters-set-for-2022-23-regular-season
