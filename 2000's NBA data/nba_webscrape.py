import psycopg2
import requests
from bs4 import BeautifulSoup, Comment
import re

# Create connection to postgresql database
connection = psycopg2.connect(database="postgres",
                              user="postgres",
                              host='localhost',
                              password="",
                              port=5432)
cursor = connection.cursor()

# Creating table teams to store scraped data
cursor.execute("""CREATE TABLE teams(
                season TEXT NOT NULL, team TEXT NOT NULL,
                wins INT NOT NULL, losses INT NOT NULL,
                fga INT, fg_per REAL ,
                three_pa INT , three_per REAL ,
                two_pa INT, two_per REAL, 
                fta INT, ft_per REAL,
                off_reb INT, def_reb INT,
                ast INT,  stl INT, 
                blk INT, tov INT, 
                pf INT, pts INT,
                PRIMARY KEY(season, team));""")
connection.commit()

# Create table seasons to store scraped data
cursor.execute("""CREATE TABLE seasons(
                  season TEXT PRIMARY KEY, champion TEXT NOT NULL,
                  mvp TEXT NOT NULL, roty TEXT NOT NULL,
                  ppg_leader TEXT NOT NULL, rpg_leader TEXT NOT NULL,
                  apg_leader TEXT NOT NUll;""")
connection.commit()

# Values to use for searching for what years to scrape data for and for what teams
year_start = 2001
year_end = 2024
team_symbol = "MIA"

# Web scraping for NBA season summaries and storing it in postgresql database
for i in range(year_start, year_end):

    # Request URL page and initialize the html parser
    with requests.Session() as res:
        page_source = res.get("https://www.basketball-reference.com/leagues/NBA_" + str(i) + ".html")
    soup = BeautifulSoup(page_source.text, 'html.parser')

    # Search through the html code to find the data to scrape (or a section close to what you want)
    # and store desired parts into variables; can use those variables to help find the next
    # value you want.
    season = soup.find('div', id = "meta").find_next('span')
    champion = season.find_next('strong').find_next('a')
    mvp = champion.find_next('a')
    roty = mvp.find_next('a')
    ppg_leader = roty.find_next('a')
    rpg_leader = ppg_leader.find_next('a')
    apg_leader = rpg_leader.find_next('a')

    # Store values into database that were extracted
    query = """ INSERT INTO seasons (season, champion, mvp, roty, ppg_leader, rpg_leader, apg_leader) 
                VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    values = (season.text, champion.text, mvp.text, roty.text, ppg_leader.text, rpg_leader.text, apg_leader.text)
    cursor.execute(query, values)
    connection.commit()
    print("Record inserted into database.")

# Web scraping for NBA team summaries by season and storing it in postgresql database
for i in range(year_start, year_end):
    
    # Request URL page and initialize the html parser
    with requests.Session() as res:
        page_source = res.get("https://www.basketball-reference.com/teams/" + team_symbol + "/" + str(i) + ".html")
    soup = BeautifulSoup(page_source.text, 'html.parser')

    # Search through the html code to find the data to scrape (or a section close to what you want)
    # and store desired parts into variables; can use those variables to help find the next
    # value you want.
    wins = "".join(soup.find('div', class_ = "prevnext").find_next('p').text.split())[7:9]
    losses = "".join(soup.find('div', class_ = "prevnext").find_next('p').text.split())[10:12]
    team_season = soup.find('div', id = "info").find_next('span')
    team_name = team_season.find_next('span')

    # The desired data in this section is in an html comment.
    # Extracting the comment text and using a regular expression to filter for
    # numbers only, stored as a tuple.
    stats_string = soup.find('div', id = "team_and_opponent_sh").find_next(string=lambda text: isinstance(text, Comment))
    stats_array = re.findall(r'\d+', stats_string)

    # Indexing the tuple for the desired values and saving then in variables to store in the database
    fga = int(stats_array[28])
    fg_per = float("." + stats_array[29])
    three_pa = int(stats_array[33])
    three_per = float("." + stats_array[35])
    two_pa = int(stats_array[39])
    two_per = float("." + stats_array[41])
    fta = int(stats_array[43])
    ft_per = float("." + stats_array[44])
    offreb = int(stats_array[45])
    defreb  = int(stats_array[46])
    ast = int(stats_array[48])
    stl = int(stats_array[49])
    blk = int(stats_array[50])
    tov = int(stats_array[51])
    pf = int(stats_array[52])
    pts = int(stats_array[53])

    # Store values into database that were extracted
    query = """ INSERT INTO teams (season, team, wins, losses, fga, fg_per, three_pa, three_per, two_pa,
                two_per, fta,  ft_per, off_reb, def_reb, ast, stl, blk, tov, pf, pts) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (team_season.text, team_name.text, wins, losses, fga, fg_per, three_pa, three_per, two_pa, two_per,
              fta, ft_per, offreb, defreb, ast, stl, blk, tov, pf, pts)

    cursor.execute(query, values)
    connection.commit()
    print("Record inserted into database.")


cursor.close()
connection.close()
