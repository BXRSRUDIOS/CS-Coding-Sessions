# Consolidation Lesson
import sqlite3 as lite
import time as t
db = "PupilDatav2.db"

def getAllRecords():
    con = lite.connect(db)
    cur = con.cursor()
    allRecords = """SELECT *
FROM ArrayDaLads
"""
    cur.execute(allRecords)
    results = cur.fetchall()
    return results

def showList(aList):
    for row in aList:
        print("\t".join([str(x) for x in row]))

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
    studentRecords = getAllRecords()
    test1Query = threeQuerySearch("SELECT PupilId, Forename, Surname, RegGroup, DoB, achievementPOints, BehaviourPoints, Autumn, Spring, UCAS", "FROM ArrayDaLads", "WHERE Autumn < 50 AND Spring < 40")
    test2Query = threeQuerySearch("SELECT PupilId, Forename, Surname, RegGroup, DoB, achievementPOints, BehaviourPoints, Autumn, Spring, UCAS", "FROM ArrayDaLads", "WHERE UCAS < 20")
    behaviourPointsQuery = fourQuerySearch("SELECT PupilId, Forename, Surname, RegGroup, DoB, achievementPOints, BehaviourPoints, Autumn, Spring, UCAS", "FROM ArrayDaLads", "WHERE BehaviourPoints <= 80 AND achievementPOints >= 20", "ORDER BY BehaviourPoints DESC")
    achPointsBehPointsQuery = threeQuerySearch("SELECT PupilId, Forename, Surname, RegGroup, DoB, achievementPOints, BehaviourPoints, Autumn, Spring, UCAS", "FROM ArrayDaLads", "WHERE achievementPOints < 20 AND BehaviourPoints > 80")
    achPointsBehPointsUpdateQuery = threeQuerySearch("UPDATE ArrayDaLads", "SET Hose='Dawg'", "WHERE (achievementPOints-BehaviourPoints) < -60")
    dawgQueries = threeQuerySearch("SELECT PupilId, Forename, Surname, RegGroup, DoB, achievementPOints, BehaviourPoints, Autumn, Spring, UCAS", "FROM ArrayDaLads", "WHERE (achievementPOints-BehaviourPoints) < -60")
    showList(dawgQueries)


if __name__ == "__main__":
    main()