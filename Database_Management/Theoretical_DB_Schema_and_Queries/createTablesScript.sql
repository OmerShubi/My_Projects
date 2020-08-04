CREATE TABLE Countries
(
    Name varchar(50) PRIMARY KEY,
    Capital varchar(50) NOT NULL,
    Language varchar(50) NOT NULL
);

CREATE TABLE Treks
(
    Name varchar(50) PRIMARY KEY ,
    Length DOUBLE PRECISION NOT NULL
);

CREATE TABLE TreksPassingThroughCountry
(
    Trek VARCHAR(50),
    Country VARCHAR(50),
    PRIMARY KEY (Trek, Country),
    FOREIGN KEY (Trek) REFERENCES Treks(Name) ON DELETE CASCADE ,
    FOREIGN KEY (Country) REFERENCES Countries(Name) ON DELETE CASCADE
);

CREATE TABLE Hikers(
    ID INT PRIMARY KEY ,
    Name VARCHAR(50) NOT NULL,
    Level VARCHAR(50) NOT NULL CHECK (Level='Beginner' OR Level = 'Experienced'),
    Country VARCHAR(50) NOT NULL ,
    FOREIGN KEY (Country) REFERENCES Countries(Name)  ON DELETE CASCADE
);

CREATE TABLE Hikes(
    Hiker INT,
    Trek VARCHAR(50),
    Date DATETIME,
    PRIMARY KEY (Hiker, Trek, Date),
    FOREIGN KEY (Hiker) REFERENCES Hikers(ID)  ON DELETE CASCADE,
    FOREIGN KEY (Trek) REFERENCES Treks(Name)  ON DELETE CASCADE
);

CREATE TABLE Messages
(
    TimeStamp TIMESTAMP,
    WrittenBy INT,
    Content VARCHAR(30) NOT NULL ,
    Type VARCHAR(50) NOT NULL CHECK (Type='Forum' OR Type = 'Private'),
    PRIMARY KEY (TimeStamp, WrittenBy) ,
    FOREIGN KEY (WrittenBy) REFERENCES Hikers(ID) ON DELETE CASCADE
);

CREATE TABLE PrivateMessages(
    TimeStamp TIMESTAMP,
    WrittenBy INT,
    WrittenTo INT NOT NULL ,
    PRIMARY KEY (TimeStamp, WrittenBy) ,
    FOREIGN KEY (TimeStamp, WrittenBy) REFERENCES Messages(TimeStamp, WrittenBy),
    FOREIGN KEY (WrittenTo) REFERENCES Hikers(ID),
);

CREATE TABLE ForumMessages(
    TimeStamp TIMESTAMP,
    WrittenBy INT,
    RelatedTo VARCHAR(50) NOT NULL ,
    PRIMARY KEY (TimeStamp, WrittenBy) ,
    FOREIGN KEY (TimeStamp, WrittenBy) REFERENCES Messages(TimeStamp, WrittenBy),
    FOREIGN KEY (RelatedTo) REFERENCES Countries(Name),
);

CREATE TABLE Recommendations(
    TimeStamp DATETIME,
    WrittenBy INT,
    Rank INT NOT NULL CHECK (Rank BETWEEN 1 AND 10),
    Description VARCHAR(20) NOT NULL ,
    PRIMARY KEY (TimeStamp, WrittenBy) ,
    FOREIGN KEY (WrittenBy) REFERENCES Hikers(ID)
);

CREATE TABLE RecommendationsToHikes(
  TimeStamp DATETIME ,
  WrittenBy INT,
  Trek VARCHAR(50),
  Country VARCHAR(50),
  PRIMARY KEY (TimeStamp,WrittenBy,Trek,Country),
  FOREIGN KEY (TimeStamp,WrittenBy) REFERENCES Recommendations,
  FOREIGN KEY (Trek,Country) REFERENCES TreksPassingThroughCountry
);

CREATE TABLE Peaks(
    PeakHeight DOUBLE PRECISION,
    LocatedIn VARCHAR(50),
    PRIMARY KEY (PeakHeight,LocatedIn),
    FOREIGN KEY (LocatedIn) REFERENCES Countries(Name)
);

CREATE TABLE Mountains(
    Name VARCHAR(50),
    PassingThrough VARCHAR(50),
    PeakHeight DOUBLE PRECISION NOT NULL ,
    PeakLocation VARCHAR(50) NOT NULL ,
    PRIMARY KEY (Name, PassingThrough),
    FOREIGN KEY (PeakHeight, PeakLocation) REFERENCES Peaks(PeakHeight, LocatedIn),
    FOREIGN KEY (PassingThrough) REFERENCES Countries(Name) ON DELETE CASCADE
);

CREATE TABLE TreksPassingThroughMountain
(
    Trek VARCHAR(50),
    MountainName VARCHAR(50),
    CountryName VARCHAR(50),
    PRIMARY KEY (Trek, MountainName, CountryName),
    FOREIGN KEY (Trek) REFERENCES Treks(Name) ON DELETE CASCADE,
    FOREIGN KEY (MountainName, CountryName) REFERENCES Mountains(Name, PassingThrough) ON DELETE CASCADE,
);

CREATE TABLE ExperiencedHikers(
    ID INT PRIMARY KEY ,
    ShoeModel DOUBLE PRECISION NOT NULL,
    HighestMountainName VARCHAR(50) not null ,
    HighestMountainLocation VARCHAR(50) not null ,
    FOREIGN KEY (ID) REFERENCES Hikers(ID)  ON DELETE CASCADE,
    FOREIGN KEY (HighestMountainName, HighestMountainLocation) REFERENCES Mountains(name, passingthrough)
);

CREATE TABLE BeginnerHikers(
    ID INT PRIMARY KEY ,
    FitnessLevel INT NOT NULL CHECK (FitnessLevel BETWEEN 1 AND 5),
    InChargeOf INT NOT NULL,
    FOREIGN KEY (ID) REFERENCES Hikers(ID) ON DELETE CASCADE ,
    FOREIGN KEY (InChargeOf) REFERENCES ExperiencedHikers(ID)
);