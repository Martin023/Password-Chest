



class User:
    userList=[]
    
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def save_user(self):
        '''
        instance method user to save the user
        save user in user_list
        '''  
        User.userList.append(self)
      
      
    '''
    remove users in user_list
    '''   
    def remove_user(self):
        User.userList.remove(self)

    @classmethod
    def aunthenticate(cls,username):
        '''
        method to check if user exists in users
        '''  
        active_user = ""
        for user in User.userList:
            if (user.username == username ):
                active_user = user.username
                
        return active_user
        
        
        
# class Credentials:
    
#     def loginValidation():
#         user=input("Enter username: ")
#         password=input("Enter password: ")
        
#         if user==Users.new_user and password == Users.new_user.password:
#             print("Success")
#         else:
#             print("No")


    
    