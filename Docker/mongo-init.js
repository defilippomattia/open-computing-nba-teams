db = db.getSiblingDB('open-computing-nba-teams');

db.createCollection('nba_teams');

db.nba_teams.insertMany([
    {
        "team":"Golden State Warriors",
        "location":"San Francisco",
        "conference": "Western",
        "division":"Pacific",
        "year_founded":1946,
        "arena":"Chase Center",
        "arena_capacity":18064,
        "championships":7,
        "finals_appearances": 12,
        "players":[
            {
                "number":"30",
                "name":"Stephen Curry",
                "position":"Guard"
            },
            {
                "number":"11",
                "name":"Klay Thompson",
                "position":"Guard"
            },
            {
                "number":"22",
                "name":"Andrew Wiggins",
                "position":"Forward"
            }
        ]
    },
    {
        "team":"Los Angeles Clippers",
        "location":"Los Angeles",
        "conference": "Western",
        "division":"Pacific",
        "year_founded":1947,
        "arena":"Crypto.com Arena",
        "arena_capacity":19079,
        "championships":0,
        "finals_appearances":0 ,
        "players":[
            {
                "number":"2",
                "name":"Kawhi Leonard",
                "position":"Forward"
            },
            {
                "number":"13",
                "name":"Paul George",
                "position":"Forward"
            },
            {
                "number":"40",
                "name":"Ivica Zubac",
                "position":"Center"
            }
        ]
    },
    {
        "team":"Aloooooooooooooooooooooooooooooooooooooooooo",
        "location":"Los Angeles",
        "conference": "Western",
        "division":"Pacific",
        "year_founded":1947,
        "arena":"Crypto.com Arena",
        "arena_capacity":19079,
        "championships":0,
        "finals_appearances":0 ,
        "players":[
            {
                "number":"2",
                "name":"Kawhi Leonard",
                "position":"Forward"
            }
        ]
    }
]);