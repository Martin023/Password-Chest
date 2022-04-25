



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
    def authenticate(cls,username,password):
        '''
        method to check if user exists in users
        '''  
        active_user = ""
        for user in User.userList:
            if (user.username == username and user.password == password):
                active_user = user.username
                
        return active_user
        
        
        
class Credentials:
    '''
    Class that generates new instances of details
    and stores our credentials
    '''
    credential_items=[]
    def __init__(self, social_sitename,social_siteusername,social_sitepassword) :
        self.social_sitename=social_sitename
        self.social_siteusername=social_siteusername
        self.social_sitepassword=social_sitepassword

    def save_creds(self):
        '''
        method to save a credential
        '''
        Credentials.credential_items.append(self)
        
    @classmethod
    def search_cred(cls,site_name):
        '''
        search for credential by name
        '''
        for cred in cls.credential_items:
            if cred.social_sitename == site_name:
                return cred
    @classmethod
    def display_creds(cls):
        '''
        return a list of all credentials 
        '''
        return cls.credential_items

    def remove_cred(self):
        '''
        method to remove credential
    
        '''
        Credentials.credential_items.remove(self) 
      
    
    

    
    
