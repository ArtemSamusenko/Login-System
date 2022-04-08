import hashlib
import time


def pass_check(password):
    if len(password) < 6:
        return print("Your password is too short! Try again.\n")
    elif not (any(char.isupper() for char in password)):
        return print("There is no capital letters in your Password! Try again.\n")
    elif not (any(char.isdigit() for char in password)):
        return print("There is no number in your Password! Try again.\n")
    elif not password == password.replace(" ", ""):
        return print("There is a space in your Password! Try again.\n")
    else:
        return "break"


def read_file(file):
    with open(file, "r") as openFile:
        read = openFile.read()
        return read


def signup():  # Sign up function

    while True:  # Making the username here
        username = (input("What do you want your username to be? Please don't add spaces as they will be "
                          "removed!\n->:".lower()).replace(" ", ""))
        if len(username) == 0:
            print("Make sure you don't leave it blank!\n")
        elif username in read_file("usernames.txt").split():
            print("Sorry this username already exists! Try again.\n")
        else:
            print("username accepted!\n")
            break

    while True:  # Making the password here
        password = input("Please make a password, make sure the password has at least: \n6 characters\nA capital "
                         "letter\nA number\nNo spaces\n->:").strip()
        if pass_check(password) == "break":
            print("Password accepted!\nYour account has been made, you can login now.\n")
            break

    salt = hash(username)
    salted = password + str(salt)

    with open("salts.txt", "a") as salts:
        salts.write(str(salt) + "\n")

    with open("usernames.txt", "a") as users:
        users.write(username + "\n")

    with open("passwords.txt", "a") as pas:
        pas.write(hashlib.sha256(salted.encode("ascii")).hexdigest() + "\n")


def login():  # Login function
    global userQus
    attempts = 3

    while attempts != 0:
        print(f"\nYou have {attempts} login attempts remaining.")
        userQus = (input("What is your username?\n->:").replace(" ", ""))
        passQus = (input("What is your password?\n->:").strip())

        userList = read_file("usernames.txt").split()

        if userQus not in userList:
            print("\nUsername or Password is wrong!, Try again.\n")
            attempts -= 1
            continue
        userIndex = userList.index(userQus)  # Gets the index of the username to cross-match with password

        passList = read_file("passwords.txt").split()

        salt = read_file("salts.txt").split()

        if not hashlib.sha256((passQus + salt[userIndex]).encode("ascii")).hexdigest() == passList[userIndex]:
            print("Username or Password is wrong!, Try again.\n")
            attempts -= 1
            continue
        else:
            return True
    print("Sorry you have ran out of login attempts!")
    return False


def change_pass(username):
    global passRead
    passList = read_file("passwords.txt").split()

    userList = read_file("usernames.txt").split()
    userIndex = userList.index(username)

    salts = read_file("salts.txt").split()

    while True:
        passQus = input("\nPlease confirm your old password, or type exit to leave\n->:").strip().replace(" ", "")
        if passQus == "exit":
            return
        elif not hashlib.sha256((passQus + salts[userIndex]).encode("ascii")).hexdigest() == passList[userIndex]:
            print("wrong password!")
        else:
            print("Correct!")
            break

    while True:  # Making the password here
        password = input("\nWhat would you like your new password to be? Make sure the new password has at least: \n6 "
                         "characters\nA capital letter\nA number\nNo spaces\n->:").strip()
        if pass_check(password) == "break":
            break

    passRead = read_file("passwords.txt").replace(passList[userIndex], hashlib.sha256((password + salts[userIndex]).encode("ascii")).hexdigest())

    with open("passwords.txt", "w") as file:
        file.write(passRead)
    print("The password has been replaced!")


def main_menu():
    while True:
        choice = input(f"Hello {userQus} What would you like to do?\na)Change password\nb)Quit\n->:").lower().replace(
            " ", "")
        while choice not in ["a", "change password", "b", "quit"]:
            choice = input("Please make sure you put a valid input!\n").lower().replace(" ", "")
        if choice == "a" or choice == "change password":
            change_pass(userQus)
        elif choice == "b" or choice == "quit":
            print("\nYou have been logged out!\n")
            break


while True:
    question = input(
        "Hello! What would you like to do in this useless program?\nA)Sign Up\nB)Login\nC)Quit\n->:").lower().strip()
    while question not in ["a", "sign up", "b", "login", "c", "quit"]:
        question = input("Invalid answer, Please try again.\nA)Sign Up\nB)Login\nC)Quit\n->:").lower().strip()
    if question == "a" or question == "sign up":
        signup()
    elif question == "b" or question == "login":
        if login():
            print("You have been logged in!")
            main_menu()
        else:
            print("\nYou have failed to login, you have been timed-out for 5 seconds\n")
            time.sleep(5)
            continue
    else:
        print("Thank you for using the program, Bye!")
        break
