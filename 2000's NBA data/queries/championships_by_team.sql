SELECT champion as team, COUNT(champion) as championships
FROM seasons
GROUP BY champion
ORDER BY championships DESC