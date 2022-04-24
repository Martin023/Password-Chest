class Users:
    userList=[]
    
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def save_user(self):
        newuser=input("Enter username: ")
        newpassword=input("Enter password: ")
        self.new_user =Users(newuser,newpassword)
        Users.userList.append(self)
        print("You will be redirected into the app")
        exit()
        
class Credentials(Users):

    def loginValidation():
        user=input("Enter username: ")
        password=input("Enter password: ")
        if user==new_user.username and password == new_user.password:
            print("Success")
        else:
            print("No")


    
    
