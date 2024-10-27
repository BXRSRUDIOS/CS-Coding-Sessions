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

def createQuery(*args):
    con = lite.connect(db)
    cur = con.cursor()
    allRecords = f"{args[0]}\n{args[1]}\n{args[2]}"
    cur.execute(allRecords)
    results = cur.fetchall()
    return results

def main():
    rptAllRecords = getAllRecords()
    print("Show All Records\n")
    showList(rptAllRecords)
    print("\n")

    print("Make my own queries\n")
    rptSomeRecords = createQuery("SELECT Forename, Surname", "FROM ArrayDaLads", "WHERE RegGroup='12CT'") # Task 1
    showList(rptSomeRecords)
    print("\n")
    
    rptSomeRecords = createQuery("SELECT Forename, Surname", "FROM ArrayDaLads", "WHERE RegGroup='12CT' and Hose='Sandringham'") # Task 2
    showList(rptSomeRecords)
    print("\n")

    rptSomeRecords = createQuery("SELECT Forename, Surname", "FROM ArrayDaLads", "WHERE Autumn<50 and Spring<40") # Task 3
    showList(rptSomeRecords)
    print("\n")

    rptSomeRecords = createQuery("UPDATE ArrayDaLads", "SET Hose='Dawg'", "WHERE AchievementPoints<20 and BehaviourPoints>20") # Task 4
    print("\n")

    rptSomeRecords = createQuery("SELECT Forename, Surname, Hose", "FROM ArrayDaLads", "WHERE AchievementPoints<20 and BehaviourPoints>20") # Task 4
    showList(rptSomeRecords)
    print("\n")



if __name__ == "__main__":
    main()

""" Tasks
write a function to enter 2 parameters reggroup and hose - DONE
enter 12CT and a house for example sandringham - DONE
write a function find out all of the boys who scored under 50 - DONE
in test 1 and 40 test 2 - DONE
write a function out all of the boys who scored under 20 - DONE
achievement points and more than 80 behaviour - DONE
update their hose to DAWG update - DONE

1) Boys in your tutor group - DONE
2) Boys in 1 and your house - DONE
3) Boys who scored 50 or less in Autumn and 40 or less in Spring should only display personal and test data not behaviour and achievement
4) Boys who have scored more than 80 behaviour points less than 20 achievement points
5) Boys born between 1st September 2006 and 15 Jan 2007  YYY-MM-DD
sort by the oldest in the year >2005-04-16
6) Boys hi

ghest, lowest and average scores for the 3 tests taken
7) Create an attribute to calculate the difference between achievement points and behaviour points
"""