from os import system
from time import sleep

# Change This Password For You
password = '123'

def Main():
    Register()
    print("- - - - - - - - | Hello User! |- - - - - - - -")
    print("=> Please Select From The Following Options:")
    print("=> Check An Existing Password")
    print("=> Add A New Password")

def Register():
    print("> > > > > Registeration < < < < <")
    print("Enter your password below:")
    givenPassword = input()

    if givenPassword == password:
        print("\033[1;32;40m Access Accepted - You Will Be Redirected To The Main Menu In 5s \033[1;37;40m \n")
        sleep(5)
        system('cls')
    else:
        system('cls')
        print("\033[1;31;40m Access Denied - Application Will Close In 5s \033[1;37;40m \n")
        sleep(5)
        exit()
    

if __name__ == "__main__":
    Main()
    