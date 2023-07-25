SELECT team, ROUND(AVG(wins),1) as wins_per_season
FROM teams
GROUP BY team
ORDER BY wins_per_season DESC