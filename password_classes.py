
class User:
    """ Class User creates user accounts and saves their information"""

    def __init__(self, username, password):
        """
        Method to define the properties of each object
        """
        self.username = username
        self.password = password
    userslist = []

    def save_user(self):
        """
       Function to save user instance
        """
        self.userslist.append(self)

        
        
class Credentials:
    """
    Credentials class to create accounts for users
    """
    credentials_list = []

    def __init__(self, accountname, accountpassword):
        """
        Method that defines the properties of each object
        """
        self.accountname = accountname
        self.accountpassword = accountpassword

  


    def save_account(self):
        """
        Function to save the new objects created in this case -accounts
        """
        self.credentials_list.append(self)

    def delete_account(self):
        """
        Function to delete the accounts saved
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_account_by_name(cls, accountname):
        """
        class method that takes in an account name and returns it if found
        """
        for credential in cls.credentials_list:
            if credential.accountname == accountname:
                return credential

    @classmethod
    def credential_exists(cls, name):
        """
        class method to check if a credential exists
        """
        for credential in cls.credentials_list:
            if credential.accountname == name:
                return True
        return False

    @classmethod
    def display_account(cls):
        """
        Class method to display all accounts saved
        """
        return cls.credentials_list
