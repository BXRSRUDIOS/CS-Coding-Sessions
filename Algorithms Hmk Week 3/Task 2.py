'''TraviBank has just installed an ATM machine at its local branch and
has asked you to write an algorithm which to be used to access users
accounts. The program should allow the user 3 attempts to enter the
correct number. The program needs to be able to validate that the PIN
number entered is a 4 digit number entered. The program should tell
the user each time if the attempt is successful or not. The user should
be given the option of either re-entering the number of withdrawing
their card if the attempt is unsuccessful. If after 3 attempts the program
should output then the attempt was unsuccessful and no further
attempts are permitted.

Write the algorithm in the form of a flowchart and pseudocode'''

pin = 2345
attempts = 0
while attempts != 3:
    if attempts != 2:
        guess = int(input("Enter pin"))
        if len(str(guess)) == 4:
            if guess == pin:
                print("Correct")
                attempts = 3
            else:
                attempts+=1
                tryAgain = input("Incorrect Pin. Try again? Y/n")
                if tryAgain == "n":
                    attempts = 3
        else:
            attempts+=1
            tryAgain = input("Invalid Length. Try again? Y/n")
            if tryAgain == "n":
                attempts = 3
    else:
        guess = int(input("Enter pin"))
        if len(str(guess)) == 4:
            if guess == pin:
                print("Correct")
                attempts = 3
            else:
                attempts+=1
                print("Incorrect. Account Locked")
        else:
            attempts+=1
            print("Incorrect. Account Locked")
        

