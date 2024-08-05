from cryptography.fernet import Fernet


master_password= input("Enter you master password : ")
def view():
    with open(r"python\python-password-manager\passwords.txt" , 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user , passw = data.split("|")
            print(f"User : {user} | password : {passw}")


def add():
    name = input("Enter your name :")
    pwd = input("Enter your name :")
    with open(r"python\python-password-manager\passwords.txt" , 'a') as f:
        f.write(f"{name} | {pwd}\n")     

def clean():
    with open(r"python\python-password-manager\passwords.txt" , 'w') as f:
        f.truncate(0)  






while True:
    ask = input("DO you want to add a password (add) \nor veiw the passwords (view) \nor want to clear the password file (clean) \nor press q to quit : ")
    if ask == "view":
        view()
    elif ask == "add":
        add()
    elif ask == 'q':
        quit()
    elif ask == "clean":
        clean()
    else:
        print("Invalid Input")
        continue