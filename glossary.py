import csv


def stats_glossary():
    text = '''Season -- If listed as single number, the year the season ended.
Age -- Age of Player at the start of February 1st of that season.
Tm -- Team
Lg -- League
Pos -- Position
G -- Games
GS -- Games Started
MP -- Minutes Played Per Game
FG -- Field Goals Per Game
FGA -- Field Goal Attempts Per Game
FG% -- Field Goal Percentage
3P -- 3-Point Field Goals Per Game
3PA -- 3-Point Field Goal Attempts Per Game
3P% -- 3-Point Field Goal Percentage
2P -- 2-Point Field Goals Per Game
2PA -- 2-Point Field Goal Attempts Per Game
2P% -- 2-Point Field Goal Percentage
eFG% -- Effective Field Goal Percentage
FT -- Free Throws Per Game
FTA -- Free Throw Attempts Per Game
FT% -- Free Throw Percentage
ORB -- Offensive Rebounds Per Game
DRB -- Defensive Rebounds Per Game
TRB -- Total Rebounds Per Game
AST -- Assists Per Game
STL -- Steals Per Game
BLK -- Blocks Per Game
TOV -- Turnovers Per Game
PF -- Personal Fouls Per Game
PTS -- Points Per Game'''

    glossary = {}
    with open("data/stats_glossary.csv", "wb") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["stat", "description"])
        for line in text.split("\n"):
            item_list = line.split(" -- ")
            writer.writerow(item_list)
            glossary[item_list[0]] = item_list[1]

    print(glossary)


stats_glossary()