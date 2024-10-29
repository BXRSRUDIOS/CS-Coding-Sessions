import sqlite3 as lite
import time as t
db = "PupilDatav2.db"

"""
THIS CODE IS 100% NOT GONNA WORK, THIS IS ONLY OPTIMISED TO DO THE HOMEWORK AND NOT ACTUAL CONCURRENT PROCESSING WITH TRANSACTIONS HENCE WHY IF YOU RAN THIS YOU'LL SEE A TON OF DATABASE IS LOCKED TYPE ERRORS
Lord Forgive My Messy Code And For Not Keeping My Database in Third Normal Form Because This Was How It Was Given To Me For The Homework :(
"""

def getAllRecords():
    con = lite.connect(db, timeout=1)
    cur = con.cursor()
    allRecords = """SELECT *
FROM Pupils
"""
    cur.execute(allRecords)
    results = cur.fetchall()
    cur.close()
    return results

def showList(aList):
    print("b")
    for row in aList:
        print("\t".join([str(x) for x in row]))

def twoQuerySearch(*args):
    con = lite.connect(db, timeout=1)
    cur = con.cursor()
    allRecords = f"{args[0]}\n{args[1]}\n"
    cur.execute(allRecords)
    results = cur.fetchall()
    cur.close()
    return results

def threeQuerySearch(*args):
    con = lite.connect(db, timeout=1)
    cur = con.cursor()
    allRecords = f"{args[0]}\n{args[1]}\n{args[2]}"
    cur.execute(allRecords)
    results = cur.fetchall()
    cur.close()
    return results

def fourQuerySearch(*args):
    con = lite.connect(db, timeout=1)
    cur = con.cursor()
    allRecords = f"{args[0]}\n{args[1]}\n{args[2]}\n{args[3]}\n"
    cur.execute(allRecords)
    results = cur.fetchall()
    cur.close()
    return results

def main():
    # Checking - All Records Print
    allRecords = getAllRecords()
    showList(allRecords)

    # Task 1 - Boys in 10RA
    boys10RA = threeQuerySearch("SELECT *", "FROM Pupils", "WHERE RegGroup ='10RA'")
    showList(boys10RA)

    # Task 2 - Boys in 10SB & Balmoral
    boys10SBBalmoral = threeQuerySearch("SELECT *", "FROM Pupils", "WHERE RegGroup='10SB' AND Hose='Balmoral'")
    showList(boys10SBBalmoral)

    # Task 3 - Boys Scoring <50 Test 1 and <40 Test 2
    boysTest1Test2 = threeQuerySearch("SELECT *", "FROM Pupils", "WHERE TestScore1 < 50 AND TestScore2 < 40")
    showList(boysTest1Test2)

    # Task 4 - Boys Achievement Points < 20 and Behaviour Points > 80
    boysAchPointsBehPoints = threeQuerySearch("SELECT *", "FROM Pupils", "WHERE AchievementPoints < 20 AND BehaviourPoints > 80")
    showList(boysAchPointsBehPoints)

    # Task 5 - Boys DOB Between 1st Jan 2005 and 31st May 2005
    boysDOB = threeQuerySearch("SELECT *", "FROM Pupils", "WHERE DOB > '2005-01-01' AND DOB < '2005-05-31'")
    showList(boysDOB)

    # Task 6 - Adding Attribute Column for Achievement Points - Behaviour Points
    createDiffAttribute = twoQuerySearch("ALTER TABLE Pupils", "ADD PointsDifference")
    boysSetupDifference = twoQuerySearch("UPDATE Pupils", "SET PointsDifference=(AchievementPoints-BehaviourPoints)")
    boysShowDifferences = twoQuerySearch("SELECT FullName, PointsDifference", "FROM Pupils")
    showList(boysShowDifferences)

    # Task 7 - Write a query where the user enters the criteria for all pupils in a tutor group
    selectStatement = input("Enter Select Statement")
    fromStatement = input("Enter From Statement")
    whereStatement = input("Enter Where Statement")
    customStatement = threeQuerySearch(selectStatement, fromStatement, whereStatement)
    showList(customStatement)

    # Task 8 - Write a query for user to enter a house and registration group
    house = input("Enter House")
    regGroup = input("Enter Registration Group")
    whereQuery = f"WHERE Hose='{house}' AND RegGroup='{regGroup}'"
    houseRegGroup = threeQuerySearch("SELECT *", "FROM Pupils", whereQuery)
    showList(houseRegGroup)
    
    # Task 9 - Write Query for user to enter Julian Day for Date of Birth
    dob = input("Enter date of birth in YYYY-MM-DD")
    whereQuery2 = f"WHERE DOB>'{dob}'"
    dobQuery = threeQuerySearch("SELECT *", "FROM Pupils", whereQuery2)
    showList(dobQuery)

    # Task 10 - Write Query for user to enter Registration Group and Behaviour Points
    behPoints = int(input("Enter Behaviour Points"))
    regGroup = input("Enter Registration Group")
    whereQuery3 = f"WHERE BehaviourPoints>{behPoints} AND RegGroup='{regGroup}'"
    behRegGroup = threeQuerySearch("SELECT *", "FROM Pupils", whereQuery3)
    showList(behRegGroup)

    # Task 11 - Write a query to work out each boys lowest, highest and average test scores
    createLowestScoreAttribute = twoQuerySearch("ALTER TABLE Pupils", "ADD LowestScore")
    createHighestScoreAttribute = twoQuerySearch("ALTER TABLE Pupils", "ADD HighestScore")
    createAverageScoreAttributes = twoQuerySearch("ALTER TABLE Pupils", "ADD AverageScore")
    caseLowestStatement = """SET LowestScore = CASE
        WHEN TestScore1 <= TestScore2 AND TestScore1 <= TestScore3 THEN TestScore1
        WHEN TestScore2 <= TestScore1 AND TestScore2 <= TestScore3 THEN TestScore2
        ELSE TestScore3"""
    updateLowestStatement = threeQuerySearch("UPDATE Pupils", caseLowestStatement, "END;")
    caseHighestStatement = """SET Highest = CASE
        WHEN TestScore1 >= TestScore2 AND TestScore1 >= TestScore3 THEN TestScore1
        WHEN TestScore2 >= TestScore1 AND TestScore2 >= TestScore3 THEN TestScore2
        ELSE TestScore3"""
    updateHighestStatement = threeQuerySearch("UPDATE Pupils", caseHighestStatement, "END;")
    updateAverageStatement = twoQuerySearch("UPDATE Pupils", "SET AverageScore=((TestScore1+TestScore2+TestScore3)/3))")
    highLowAverageStatement = threeQuerySearch("SELECT FullName, RegGroup, TestScore1, TestScore2, TestScore3, HighestScore, LowestScore, AverageScore")
    showList(threeQuerySearch)
    
    # Task 12 - Write a query using update to make the boys scored more than 80 behaviour points less than 20 achievement points members of the Dawg house
    dawgUpdateQuery = threeQuerySearch("UPDATE Pupils", "SET Hose='Dawg'", "WHERE BehaviourPoints > 80 AND AchievementPoints < 20")
    dawgSearchQuery = threeQuerySearch("SELECT *", "FROM Pupils", "WHERE Hose='Dawg'")
    showList(dawgSearchQuery)

    # Task 13 - Write a query to calculate the age of each pupil
    ageQuery = twoQuerySearch("SELECT FullName, DOB, CAST((julianday('now') - julianday(DOB)) / 365.25 AS INT) AS Age", "FROM Pupils")
    showList(ageQuery)

    # Task 14 - Write a query to extract first and last names from the full name column
    nameQuery = twoQuerySearch("SELECT FullName, TRIM(substr(FullName, instr(FullName, ',') + 1)) AS FirstName, TRIM(substr(FullName, 1, instr(FullName, ',') - 1)) AS LastName", "FROM Pupils")
    showList(nameQuery)

    # Task 15 - Write a query to make a username based on last 2 digits of yob and first 3 chars of first and last name
    usernameFormation = """LOWER(
        SUBSTR(CAST(STRFTIME('%Y', DOB) AS TEXT), -2) || 
        SUBSTR(TRIM(SUBSTR(FullName, INSTR(FullName, ',') + 1)), 1, 3) || 
        SUBSTR(TRIM(SUBSTR(FullName, 1, INSTR(FullName, ',') - 1)), 1, 3)
    ) AS Username"""
    usernameQuery = twoQuerySearch(f"SELECT FullName, DOB, {usernameFormation}", "FROM Pupils")
    showList(usernameQuery)

    # Task 16 - Write a query to make a username based on last 2 digits of yob + full surname + first 2 chars of first name
    usernameFormation2 = """LOWER(
        SUBSTR(CAST(STRFTIME('%Y', DOB) AS TEXT), -2) || 
        TRIM(SUBSTR(FullName, 1, instr(FullName, ',') - 1)) || 
        SUBSTR(TRIM(SUBSTR(FullName, 1, INSTR(FullName, ',') + 1)), 1, 2)
    ) AS Username"""
    usernameQuery2 = twoQuerySearch(f"SELECT FullName, DOB, {usernameFormation2}", "FROM Pupils")
    showList(usernameQuery2)
    

    
if __name__ == "__main__":
    main()