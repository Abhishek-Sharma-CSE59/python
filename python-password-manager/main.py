from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key" , "wb") as key_file:
#         key_file.write(key)
        
# write_key()


def load_key():
    file = open(r"E:\data files\git\python\python-password-manager\key.key","rb")
    key = file.read()
    file.close
    return key
key = load_key()
fer = Fernet(key)
def view():
    with open(r"python\python-password-manager\passwords.txt" , 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user , passw = data.split("|")
            print(f"---------------------------\nUser : {user} | password : {fer.decrypt(passw.encode()).decode()}\n---------------------------")


def add():
    name = input("Enter your name :")
    pwd = input("Enter your password :")
    with open(r"python\python-password-manager\passwords.txt" , 'a') as f:
        f.write(f"{name} | {fer.encrypt(pwd.encode()).decode()}\n")

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