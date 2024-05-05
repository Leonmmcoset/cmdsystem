import pickle
import os
from system import color
def start():

    try:
        os.path.isdir('C:\\cmd')
    except:
        os.mkdir('C:\\cmd')
    import pickle

    def save_password(password):
        with open("C:\\cmd\\user.dat", "wb") as f:
            pickle.dump(password, f)

    def load_password():
        try:
            with open("C:\\cmd\\user.dat", "rb") as f:
                password = pickle.load(f)
        except FileNotFoundError:
            password = None
        return password

    def set_password():
        password = load_password()
        if password:
            print(color.red+"Password is set!"+color.end)
        else:
            new_password = input("Please input the password:")
            save_password(new_password)
            print(color.green+"Password set done."+color.end)

    def login():
        global login_      #Are this bug is arouding by me?
        login_ = ''        #How???
        password = load_password()
        if password is None:
            print(color.red+"None password!Please set it!"+color.end)
        else:
            attempt = input("Password:")
            if attempt == password:
                print(color.green+"Login done!"+color.end)
                login_ = 'Yes'
            else:
                print(color.red+"Password failed!"+color.end)
                login_ = 'No'
    def delete():
        login_ = ''
        password = load_password()
        if password is None:
            print(color.red+"None password!Please set it!"+color.end)
        else:
            attempt = input("Password:")
            if attempt == password:
                print(color.green+"Password true!Delete password..."+color.end)
                os.remove('C:\\cmd\\user.dat')
            else:
                print(color.red+"Password failed!"+color.end)

    while True:

        print("1. Set Password")
        print("2. Login")
        print("3. Delete Password")
        print("4. Exit")
        choice = input("Choice:")

        if choice == "1":
            set_password()
        elif choice == "2":
            login()
            if login_ == 'Yes':
                break
        elif choice == "3":
            delete()
        elif choice == "4":
            exit()
        else:
            print(color.red+"Choice error!"+color.end)