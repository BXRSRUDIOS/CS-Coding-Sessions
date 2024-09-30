
def username(fName, sName, yoe):
    username = str(yoe)[-2:] + sName[:4] + fName[:3]
    return username

fname = input("Enter first name: ")
sname = input("Enter surname: ")
yoe = int(input("Enter year of entry: "))

personUsername = username(fname, sname, yoe)
print("Generated Username:", personUsername)
