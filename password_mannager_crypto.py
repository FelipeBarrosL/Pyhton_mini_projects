from cryptography.fernet import Fernet


#Generate key.key file, only needed once
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

#Load the key previouly generated
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#Confirm if the user knows the master pwd
def define_pwd():
    master_pwd = input("Define your master password: ")
    with open("password.txt", 'a') as f:
        f.write("Master|Master|" + fer.encrypt(master_pwd.encode()).decode() + "\n")
    print("Master Password defined!")
    

def access_validation():
    validation = input("What is the master password? ")
    with open("password.txt", "r") as f:
        data = f.readline()
        data = data.rstrip()
        if data == "":
            define_pwd()
            access_validation() 

        account, user, passw = data.split("|")
        print(fer.decrypt(passw.encode()).decode())

        if validation == fer.decrypt(passw.encode()).decode():
            print("Password Confirmed!")
            return True
        elif validation == "resetpwd":
            reset_pwd()
        else:
            print("Access Denied!!! ")
            quit()

#Gets called if the user wants to change the master password
def reset_pwd():
    validation = access_validation()
    if validation:
        with open("password.txt", "r") as f:
            data = f.readlines()

        new_master_pwd =  input("Type your new master password: ")
        data[0] = ("Master|Master|" + fer.encrypt(new_master_pwd.encode()).decode() + "\n")

        with open("password.txt", "w") as f:
            f.writelines(data)

#Show the selected password
def view():
    name = input("What account would you like to check? ").lower()
    if name == 'all':
        with open("password.txt", 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                account, user, passw = data.split("|")
                print(f"Account name: {account} -> User name: {user} -> Password: {fer.decrypt(passw.encode()).decode()}")
    else:
        with open("password.txt", 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                account, user, passw = data.split("|")
                if name == account.lower():
                    print(f"Account name: {account} -> User name: {user} -> Password: {fer.decrypt(passw.encode()).decode()}")
                else:
                    continue

#Add new account in the end of the txt
def add():
    name = input("Account name: ")
    login = input("User name: ")
    pwd = input("Password: ")

    with open("password.txt", 'a') as f:
        f.write(name + "|" + login + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


#Loads the crypto key
key = load_key() 
fer = Fernet(key)

#Checks the right to access
access_granted = access_validation()

if access_granted:
    while True:
        mode = input("Would you like to add a new pwd or view existing ones (view/add)?\nPress 'q' to quit:").lower()
        if mode == "q":
            break

        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode!")
            continue
    

