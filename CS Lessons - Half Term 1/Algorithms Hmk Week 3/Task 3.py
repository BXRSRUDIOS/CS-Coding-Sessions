'''Algorithm 2

If the pin has been successfully entered the ATM offers the
user to the following choices

a) See and View Balance

b) Order a statement

c) Withdraw some cash - if this feature is chosen then the
customer cannot withdraw more money then is in the account
and there is a limit on daily withdrawals of £200

d) exit the ATM

Write a new algorithm to include these features the program
must iterate until one of the choices from above is selected'''


# Hypothetically speaking, there is no details for the person as there is no database with the data of everyone
# So i made it up
def selectChoice(select, cashToWithdraw=None):
    if select == "a)":
        return(f"Balance is {cashToWithdraw}")
    elif select == "b)":
        return "Statement has been ordered"
    elif select == "c)":
        if cashToWithdraw <= 200:
            return f"Withdrawing {cashToWithdraw}"
        else:
            return "Unable to withdraw"
    elif select == "d)":
        return "Exiting ATM"

selection = "" 
confirmed = False

while confirmed == False:
    cashToWithdraw = int(input("Enter balance or Cash To Withdraw"))
    selection = input("""Enter either as follows
                      a) View Balance
                      b) Order a Statement
                      c) Withdraw Cash (Limit £200)
                      d) Exit ATM
    """)
    if selection == "a)" or selection == "b)" or selection != "c)" or selection != "d)":
        confirmed=True
print(selectChoice(selection, cashToWithdraw))


        
