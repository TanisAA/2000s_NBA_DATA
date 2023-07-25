# 2000s NBA Data

This project uses the python packages `BeautifulSoup54` and `requests` to scrape NBA data from ![Basketball Reference](https://www.basketball-reference.com/). The data collected is from the 2000-01 season to the present. A teams stats from each season were collected along with a quick overview of the accolades players received each season (such as who as mvp). I stored this data in a local postgreSQL database; the tables and records were created within the python code. The erd of the two simple tables are shown below:
![nba_data_schema](https://github.com/TanisAA/2000s_NBA_Data/assets/91431371/2925cbaf-f622-4448-8daa-d580497e6575)
