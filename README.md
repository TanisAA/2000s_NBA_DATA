# 2000s NBA Data
This project uses the python packages `BeautifulSoup4` and `requests` to scrape NBA data from [Basketball Reference](https://www.basketball-reference.com/). The data collected is from the 2000-01 season to the present. A teams stats from each season were collected along with a quick overview of the accolades players received each season (such as who as mvp). I stored this data in a local postgreSQL database; the tables and records were created within the python code. The erd of the two simple tables are shown below:


<img src = "https://github.com/TanisAA/2000s_NBA_Data/assets/91431371/2925cbaf-f622-4448-8daa-d580497e6575" width = 65% height = 65% >

All of the information stored is available in the form of csv files under the `datasets` folder of this project. Some simple sql queries are also provided along with their results, stored in sql and csv files under the `queries` folder of this project.

## Data collected
The first step was to decide what information I wanted to collect off of the website, and then finding that information in the source page to be able to extract it out with the `BeautifulSoap` package. The following two pictures show just this. The information stored for the `seasons` table (shown in red boxes):

<img src = "https://github.com/TanisAA/2000s_NBA_Data/assets/91431371/e1ba7b30-4943-4eca-974d-112762849877" width = 70% height = 70%>
<img src = "https://github.com/TanisAA/2000s_NBA_Data/assets/91431371/2419c77c-f0c7-4ebc-bbe6-504016092901">
<br>
<br>  
<br>
<br>

The information for the `teams` table is showed below (in red boxes):

<img src = "https://github.com/TanisAA/2000s_NBA_Data/assets/91431371/456eecb7-5ef3-48eb-a968-f030918ddd63" width = 70% height = 70%>
<img src = "https://github.com/TanisAA/2000s_NBA_Data/assets/91431371/3f70c613-878b-4bfd-babe-58a385287c4b">

## Visualizing the data
The visualizations were created using tableau public. Information displayed shows how the scoring and the pace of the game has changed over time, the best performing teams during the time period, and more. To interact with the dashboard visit [here](https://public.tableau.com/app/profile/tanis.anderson/viz/2000sNBAdata/2000sNBAData).
![nba_tableau_dashboard](https://github.com/TanisAA/2000s_NBA_DATA/assets/91431371/11d816b7-76c2-47bb-9bb0-d37204150f99)

## Misc.
The code provided can easily be adapted to store the data in file instead of in a database (such as a text or csv file). It is also possible to create more loops to make the web scraping more automated; such as adding a loop that iterates through an array of team symbols along with each season. 
The current method of extracting the team stats data out of the html comment is not the most optimal, but it works. Another method is possible and is being tested. 
