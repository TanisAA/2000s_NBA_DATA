SELECT s.season, champion, wins as regular_season_wins
FROM seasons s 
INNER JOIN teams t
ON s.champion = t.team AND s.season = t.season
ORDER BY wins