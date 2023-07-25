SELECT season, t1.team, ppg
FROM teams t1
INNER JOIN(
	SELECT team, MAX(ROUND(pts*1.0  / (wins + losses),1)) as ppg
	FROM teams
	GROUP BY team) t2
ON t2.team = t1.team AND t2.ppg = (ROUND(t1.pts * 1.0 / (t1.wins +t1.losses),1))
ORDER BY ppg DESC

