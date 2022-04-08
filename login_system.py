def signup():
    with open("usernames.txt","r") as users:
        read = users.read()
        list_users = read.split()
    while True:
        username = ((input("\nWhat do you want your username to be? Please dont add spaces as they will be removed!\n->:").strip()).lower()).replace(" ","")
        if len(username) == 0:
            print("Make sure you dont leave it blank!\n")
            continue
        elif username in list_users:
            print("Username already exists! Try again.\n")
            continue
        print("username accepted!\n")
        break
    while True:
        password = ((input("Please make a password, make sure the password has; 6 Charecters, Capital letter, a number!\n->:")).strip()).replace(" ","")
        if len(password) < 6:
            print("Your password is too short! Try again.\n")
            continue
        elif not (any(char.isupper() for char in password)):
            print("There is no Capital Letters in your Password! Try again.\n")
            continue
        elif not (any(char.isdigit() for char in password)):
            print("There is no number in your Password! Try again.\n")
            continue
        break
    print("Password accepted!\nYour account has been made, you can login now.\n")
    with open("usernames.txt","a") as users:
            users.write(username+"\n")
    with open("passwords.txt","a") as pas:
            pas.write(password+"\n")

def login():
    global user_qus
    global user_index
    global pass_qus
    global pas_list
    attempts = 3
    while True and attempts != 0:
        print("\nYou have", attempts ,"login attempts remaining.")
        user_qus = ((input("What is your username?\n->:").strip()).lower()).replace(" ","")
        pass_qus = (input("What is your password?\n->:").strip()).replace(" ","")
        with open("usernames.txt","r") as user:
            lines = user.read()
            user_list = lines.split()
        if user_qus not in user_list:
            print("\nUsername or Password is wrong!, Try again.\n")
            attempts -= 1
            continue
        user_index = user_list.index(user_qus)
        with open("passwords.txt","r") as pas:
            pas_read = pas.read()
            pas_list = pas_read.split()
        if pas_list[user_index] != pass_qus:
            print("Username or Password is wrong!, Try again.\n")
            attempts -= 1
            continue
        else:
            return True
    print("Sorry you have ran out of attempts!")

def changepass():
    passqus = (input("\nPlease confirm your password, or type exit to leave\n->:").strip()).replace(" ","")
    while passqus != pass_qus:
        if passqus == "exit":
            break
        passqus = (input("wrong password!\n->:").strip()).replace(" ","")
    newpass = (input("\nWhat would you like your new password to be?\n->:").strip()).replace(" ","")
    with open("passwords.txt","r") as file:
        allpass = file.read()
    allpass = allpass.replace(passqus,newpass)
    with open("passwords.txt","w") as file:
        file.write(allpass)
    print("The password has been replaced!")

def main_menu():
    while True:
        choice = ((input("\nHello {} What would you like to do?\na)Change password\nb)Quit\n->:".format(user_qus))).lower()).strip()
        while choice != "a" and choice != "b" and choice != "quit" and choice != "changepass":
            choice = input("Please make sure you put a valid input!\n")
        if choice == "a" or choice == "changepass":
            changepass()
        elif choice == "b" or choice == "quit":
            print("\nYou have been logged out!\n")
            break
welcome()

quit = False
while quit == False:
    qustion = (input("Hello! What would you like to do in this useless program?\nA)Sign Up\nB)Loggin\nC)Quit\n->:").strip()).lower()
    while qustion != "a" and qustion != "sign up" and qustion != "b" and qustion != "loggin" and qustion != "c" and qustion != "quit":
        qustion = input(("Invalid awnser, Please try again.\nA)Sign Up\nB)Loggin\nC)Quit\n->:").lower()).strip()
    if qustion == "a" or qustion == "sign up":
        signup()
    elif qustion == "b" or qustion == "loggin":
        if login() == True:
            print("You have been logged in!")
            main_menu()
        else:
            print("\nYou have failed to loggin, either make a new account or remeber your passwords dumb dumb...\n")
            continue
    else:
        print("Thank you for using the program, Bye!")
        quit = True