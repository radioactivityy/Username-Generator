def main():
    print("Go on to get yourself a generated username!\n")
first = input("Enter your first name: ")
last= input("Enter your last name: ")
uname = first[2] + last[:4]
print("Your username is:", uname)
main()