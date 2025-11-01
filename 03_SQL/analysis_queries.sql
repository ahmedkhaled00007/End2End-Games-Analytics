-- ========================================
-- START ANALYSIS QUERIES
-- ========================================

USE [Analysis-Games];
GO

-- 1) Most sales Games Categories and Their Audience
SELECT  
    Category,
    People_Generation,
    SUM(TotalWorld_Sales_millions) AS Total_Sales
FROM dbo.Games_Cleaned
GROUP BY Category, People_Generation
ORDER BY Total_Sales DESC;
GO

-- 2) Gold Era in games production and Number of Games
SELECT TOP 1
    Era_Category,
    SUM(TotalWorld_Sales_millions) AS Total_Sales,
    COUNT(Id) AS Num_Games
FROM dbo.Games_Cleaned
GROUP BY Era_Category
ORDER BY Total_Sales DESC;
GO

-- 3) Top 5 Games per Category
WITH RankedGames AS (
    SELECT
        Name,
        Category,
        MAX(TotalWorld_Sales_millions) AS Total_Sales,
        ROW_NUMBER() OVER (
            PARTITION BY Category
            ORDER BY MAX(TotalWorld_Sales_millions) DESC
        ) AS rn
    FROM dbo.Games_Cleaned
    GROUP BY Name, Category
)
SELECT
    Name,
    Category,
    Total_Sales
FROM RankedGames
WHERE rn <= 5
ORDER BY Category, Total_Sales DESC;
GO

-- 4) Top 3 Publishers by Total North America Sales per Genre
WITH Pub_Data AS (
    SELECT
        Publisher,
        Genre,
        SUM(NorthAmerica_Sales_millions) AS North_America
    FROM dbo.Games_Cleaned
    GROUP BY Publisher, Genre
),
RankedPub AS (
    SELECT
        Publisher,
        Genre,
        North_America,
        ROW_NUMBER() OVER (
            PARTITION BY Genre
            ORDER BY North_America DESC
        ) AS rn
    FROM Pub_Data
)
SELECT
    Publisher,
    Genre,
    North_America
FROM RankedPub
WHERE rn <= 3
ORDER BY Genre, North_America DESC;
GO

-- 5) Top 5 Platforms by Total World Sales
SELECT TOP 5
    Platform,
    SUM(TotalWorld_Sales_millions) AS Total_Sales
FROM dbo.Games_Cleaned
GROUP BY Platform
ORDER BY Total_Sales DESC;
GO

-- 6) Average Game Age per Era
-- CAST Game_Age to INT if needed
SELECT
    Era,
    AVG(CAST(Game_Age AS FLOAT)) AS Avg_Game_Age
FROM dbo.Games_Cleaned
GROUP BY Era
ORDER BY Avg_Game_Age DESC;
GO

-- 7) Most Popular Multiplayer Games per Category
WITH MultiplayerRank AS (
    SELECT
        Name,
        Category,
        Multiplayer,
        TotalWorld_Sales_millions,
        ROW_NUMBER() OVER (
            PARTITION BY Category
            ORDER BY TotalWorld_Sales_millions DESC
        ) AS rn
    FROM dbo.Games_Cleaned
    WHERE Multiplayer = 'Yes'
)
SELECT
    Name,
    Category,
    Multiplayer,
    TotalWorld_Sales_millions
FROM MultiplayerRank
WHERE rn <= 3
ORDER BY Category, TotalWorld_Sales_millions DESC;
GO

-- 8) Highest Selling Games per Decade
WITH DecadeRank AS (
    SELECT
        Name,
        Decade,
        TotalWorld_Sales_millions,
        ROW_NUMBER() OVER (
            PARTITION BY Decade
            ORDER BY TotalWorld_Sales_millions DESC
        ) AS rn
    FROM dbo.Games_Cleaned
)
SELECT
    Name,
    Decade,
    TotalWorld_Sales_millions
FROM DecadeRank
WHERE rn = 1
ORDER BY Decade;
GO

-- 9) Top Genres by North America vs Europe Sales Ratio
SELECT
    Genre,
    SUM(NorthAmerica_Sales_millions) / NULLIF(SUM(Europe_Sales_millions),0) AS NA_EU_Ratio
FROM dbo.Games_Cleaned
GROUP BY Genre
ORDER BY NA_EU_Ratio DESC;
GO

-- 10) Publishers with Most Games Released per Platform
WITH PublisherCount AS (
    SELECT
        Publisher,
        Platform,
        COUNT(Id) AS Num_Games
    FROM dbo.Games_Cleaned
    GROUP BY Publisher, Platform
)
SELECT TOP 10
    Publisher,
    Platform,
    Num_Games
FROM PublisherCount
ORDER BY Num_Games DESC;
GO
