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
        "year_founded":1970,
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
        "team":"Los Angeles Lakers",
        "location":"Los Angeles",
        "conference": "Western",
        "division":"Pacific",
        "year_founded":1947,
        "arena":"Crypto.com Arena",
        "arena_capacity":19079,
        "championships":17,
        "finals_appearances":32 ,
        "players":[
            {
                "number":"3",
                "name":"Anthony Davis",
                "position":"Center"
            },
            {
                "number":"6",
                "name":"LeBron James",
                "position":"Forward"
            },
            {
                "number":"12",
                "name":"Kendric Nunn",
                "position":"Guard"
            }
        ]
    },
    {
        "team":"Boston Celtics",
        "location":"Los Angeles",
        "conference": "Eastern",
        "division":"Atlantic",
        "year_founded":1946,
        "arena":"TD Garden",
        "arena_capacity":19156,
        "championships":17,
        "finals_appearances":22 ,
        "players":[
            {
                "number":"36",
                "name":"Marcus Smart",
                "position":"Guard"
            },
            {
                "number":"7",
                "name":"Jaylen Brown",
                "position":"Guard"
            },
            {
                "number":"42",
                "name":"Al Horford",
                "position":"Center"
            }
        ]
    },
    {
        "team":"New York Knicks",
        "location":"New York City",
        "conference": "Eastern",
        "division":"Atlantic",
        "year_founded":1946,
        "arena":"Madison Square Garden",
        "arena_capacity":19812,
        "championships":2,
        "finals_appearances":8 ,
        "players":[
            {
                "number":"1",
                "name":"Obi Toppin",
                "position":"Forward"
            },
            {
                "number":"4",
                "name":"Derrick Rose",
                "position":"Guard"
            },
            {
                "number":"45",
                "name":"Jericho Sims",
                "position":"Center"
            }
        ]
    },
    {
        "team":"Toronto Raptors",
        "location":"Toronto",
        "conference": "Eastern",
        "division":"Atlantic",
        "year_founded":1995,
        "arena":"Scotiabank Arena",
        "arena_capacity":19800,
        "championships":1,
        "finals_appearances":1,
        "players":[
            {
                "number":"4",
                "name":"Scottie Barnes",
                "position":"Forward"
            },
            {
                "number":"20",
                "name":"Jeff Dowtin",
                "position":"Guard"
            },
            {
                "number":"24",
                "name":"Khem Birch",
                "position":"Center"
            }
        ]
    },
    {
        "team":"Philadelphia 76ers",
        "location":"Philadelphia",
        "conference": "Eastern",
        "division":"Atlantic",
        "year_founded":1946,
        "arena":"Wells Fargo Center",
        "arena_capacity":20478,
        "championships":3,
        "finals_appearances":9,
        "players":[
            {
                "number":"12",
                "name":"Tobias Harris",
                "position":"Forward"
            },
            {
                "number":"1",
                "name":"James Harden",
                "position":"Guard"
            },
            {
                "number":"21",
                "name":"Joel Embiid",
                "position":"Center"
            }
        ]
    }
]);