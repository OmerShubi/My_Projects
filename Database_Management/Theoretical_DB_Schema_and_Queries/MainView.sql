-- All recommendations that where written by a hiker that
--wrote recommendations on all parts of the trek
CREATE VIEW CompleteRecommendation
AS
    SELECT *
    FROM RecommendationsToHikes RTH
    WHERE NOT EXISTS(
        /* All countries that the trek(of a specific recommendation)
            passes through */
        (SELECT DISTINCT TPTC.Country
         FROM TreksPassingThroughCountry TPTC
         WHERE TPTC.Trek = RTH.Trek)

        EXCEPT -- minus alternative
        /* All countries (relevant to the trek in the recommendation)
         that the specific hiker published recommendations on */
        (SELECT DISTINCT RTH2.Country
         FROM RecommendationsToHikes RTH2
         WHERE RTH.WrittenBy = RTH2.WrittenBy AND
               RTH.Trek = RTH2.Trek)
    );

/* Finds all TrendLeaders as defined */
CREATE VIEW TrendLeaders
AS
    SELECT H.ID, H.Name
    FROM Hikers H -- Iterate over all Hikers
    /* If a hiker has at least one trek that more than a 100 people follow
        him after his Complete recommendation then he becomes a TrendLeader*/
    WHERE EXISTS(SELECT *
         FROM Treks --  For each Hiker Iterate over all Treks
         WHERE 100 < (SELECT COUNT(DISTINCT Hikes.Hiker)
              FROM Hikes,
                  /* Returns the last recommendation by the person, about the trek */
                   (SELECT TOP 1 CR.Trek, CR.TimeStamp
                    FROM CompleteRecommendation CR
                    WHERE H.ID = CR.WrittenBy AND Treks.Name = CR.Trek
                    ORDER BY CR.TimeStamp DESC) TheTrek
                /* Verify no more than a year has passed since recommendation*/
              WHERE Hikes.trek = TheTrek.Trek AND
                    DATEDIFF(Day, TheTrek.TimeStamp, Hikes.Date) < 365)
         );

-- Return Stats as requested
SELECT NumOfTreks.ID, Name, NumberOfTreks, NumberOfRecommendations
FROM
    (SELECT TL.ID, TL.Name, COUNT(*) AS NumberOfTreks
    FROM Hikes H, TrendLeaders TL
    WHERE H.Hiker = TL.ID
    GROUP BY TL.ID, TL.Name) NumOfTreks,

    (SELECT TL.ID, COUNT(*) AS NumberOfRecommendations
    FROM Recommendations R, TrendLeaders TL
    WHERE R.WrittenBy = TL.ID
    GROUP BY TL.ID) NumOfRecommendations
WHERE NumOfTreks.ID = NumOfRecommendations.ID
ORDER BY NumOfTreks.ID ASC;




