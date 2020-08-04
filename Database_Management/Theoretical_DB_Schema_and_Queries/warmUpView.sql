/* Note that we perform left outer join on each part of stats as to make sure we get all stats on all treks
    No matter if specfic stat is zero (which can happen with number of recommendation for example) */
CREATE VIEW WarmUpView
AS
Select top 1000000 HikersStats.Trek, HikersStats.NumOfHikers, MsgsStats.NumOfForumMsgs, RecommendationStats.NumOfRecommendations
FROM
    (SELECT *
     FROM Treks LEFT OUTER JOIN
        (SELECT Trek, COUNT(DISTINCT Hikes.Hiker) AS NumOfHikers
        FROM Hikes
        GROUP BY Trek) TableA ON TableA.Trek = Treks.Name) HikersStats
     ,
    (SELECT *
    FROM Treks LEFT OUTER JOIN
        (SELECT Trek, COUNT(*) AS NumOfForumMsgs
        From ForumMessages FM, TreksPassingThroughCountry TC
        where FM.RelatedTo = TC.Country
        GROUP BY Trek) TableB ON TableB.Trek = Treks.Name) MsgsStats
     ,
    (SELECT *
    FROM Treks LEFT OUTER JOIN
         (SELECT Trek,COUNT(*) as NumOfRecommendations
     FROM RecommendationsToHikes
     GROUP BY Trek) TableC ON TableC.Trek = Treks.Name) RecommendationStats

WHERE HikersStats.Trek = MsgsStats.Trek AND MsgsStats.Trek = RecommendationStats.Trek
ORDER BY HikersStats.NumOfHikers DESC;
