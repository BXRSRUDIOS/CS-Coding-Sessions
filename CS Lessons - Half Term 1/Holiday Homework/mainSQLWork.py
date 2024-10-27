import sqlite3 as lite
import time as t
db = "PupilDatav2.db"

def getAllRecords():
    con = lite.connect(db)
    cur = con.cursor()
    allRecords = """SELECT *
FROM Pupils
"""
    cur.execute(allRecords)
    results = cur.fetchall()
    return results

def showList(aList):
    print("b")
    for row in aList:
        print("\t".join([str(x) for x in row]))

def twoQuerySearch(*args):
    con = lite.connect(db)
    cur = con.cursor()
    allRecords = f"{args[0]}\n{args[1]}\n"
    cur.execute(allRecords)
    results = cur.fetchall()
    return results

def threeQuerySearch(*args):
    con = lite.connect(db)
    cur = con.cursor()
    allRecords = f"{args[0]}\n{args[1]}\n{args[2]}"
    cur.execute(allRecords)
    results = cur.fetchall()
    return results

def fourQuerySearch(*args):
    con = lite.connect(db)
    cur = con.cursor()
    allRecords = f"{args[0]}\n{args[1]}\n{args[2]}\n{args[3]}\n"
    cur.execute(allRecords)
    results = cur.fetchall()
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
    
if __name__ == "__main__":
    main()