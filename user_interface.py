# Welcome to Password-Chest section



import password_classes

print("Welcome to Password-Chest")

def login():
    login=input("Do you have an account: Yes: Y --- No: N ::")

    if login=="Y":
        password_classes.Credentials.loginValidation()
        
            
    elif login=="N":
        print("Create account")
        password_classes.Users.save_user(self=password_classes.Users)
        

    else:
        print("Invalid input! Please try again")
        exit()
    
    
login()

userName= input()
userPassword= input()