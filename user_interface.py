from password_classes import Credentials, User

##Users Section

def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_by_uname(username)

def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()

def auth(name,password):
    '''
    method to check if a uer already exists in the users list
    '''
    return User.authenticate(name,password)


##Credentials section

def create_credential(sitename,siteusername,sitepassword):
    '''
    Function to create a new credential
    '''
    new_credential = User(sitename,siteusername,sitepassword)
    return new_credential

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_creds()

def search_creds(name):
    '''
    method to search for a credential by name
    '''
    return Credentials.search_cred(name)


def disp_creds():
    '''
    method to display a list of credentials
    '''
    return Credentials.display_creds()


def main():
    print("Hello Welcome to your Password_Chest. What is your name?")
    uname = input()

    print(f"Hello {uname}. what would you like to do?")
    print('\n')
    while True:
            print("Use these short codes : nu - create a new user, du - display users, lg - login ex -exit the password-chest ")
            short_code = input().lower()
            if short_code == 'nu':
                    print("\n New User :")
                    print("-"*10)
                    print ("User name ....")
                    u_name = input()
                    print(" Create password ...")
                    pass_name = input()
                    
                    save_user(create_user(u_name,pass_name)) # create and save new user
                    print ('\n')
                    print(f"New User :{u_name} with password  :{pass_name} created")
                    print ('\n')
            elif short_code == 'du':
                    if display_users():
                            print("Here is a list of all pass-chest users")
                            print('\n')
                            for user in display_users():
                                    print(f"{user.first_name} ")
                            print('\n')
                    else:
                            print('\n')
                            print("No users currently using Pass-chest")
                            print('\n')
            elif short_code == 'lg':

                print("Enter username.....")
                search_user_name = input()
                print("Enter password.....")
                search_user_pass = input()
                user = auth(search_user_name,search_user_pass)
                if search_user_name==user:
                        print(f"\t\t\t\t\tHello, {search_user_name}.Proceed to select a short code to navigate")

                        while True:
                            print("\t\t\t\t"+"*"*50)
                            print("\t\t\t\t"+"*"*50)
                            print('\n')
                            print("ND  - create an a new Details")
                            print("DC - display credentials")
                            print("FD - search credentials")
                            print("\t\t\t\t\trm - remove credential")
                            print("\t\t\t\t\tup - update credential")
                            print("\t\t\t\t\tcp - copy credential")
                            print("\t\t\t\t\tex - exit app")
                            print('\n')
                            print("\t\t\t\t"+"*"*50)
                            print("\t\t\t\t"+"*"*50)
                    
                            menu_choice = input("\t\t\t\t\tShortcode:").lower().strip()
                            print("\n")
                            if menu_choice == 'nd':
                                # create a new details
                                print("\t\t\t\t\tEnter details ")
                                social_media_site_name = input("\t\t\t\t\tSocial site Name:").strip()
                                choose_user_name = input("\t\t\t\t\tUser Name:").strip()
                                while True:
                                    print("\t\t\t\t\tEnter Own  - to type in your own password")
                                    # print("\t\t\t\t\tEnter gp - to be generated password\n")


                                    password_choice = input("\t\t\t\t\tChoice: ").lower().strip()

                                    if password_choice == 'own':
                                        password = input("\t\t\t\t\tEnter password: ")
                                        break
                                    # elif password_choice == 'Gen':
                                    #     print("\t\t\t\t\tEnter the length of the password you want")
                                    #     print("\t\t\t\t\tPassword must be between 8 and 12")
                                    #     len=int(input("\t\t\t\t\tLength: "))

                                    #     if len > 12 or len < 8:
                                    #         print("\t\t\t\t\tlength must not be greater than 12 or less than 8")

                                    #     else:
                                    #         password = Credentials.generate_password(len)
                                    #         print(f"\t\t\t\t\tyour password is {password}")
                                    #         break
                                    # else:
                                    #     print("\t\t\t\t\tInvalid Choice.Please use short codes")
                                    password=password.strip() 
                                    if social_media_site_name == "" or choose_user_name == "" or password == "":
                                        print("One or more fields is empty")
                                       
                                    else:
                                        save_credentials(create_credential(social_media_site_name,choose_user_name,password))
                            elif menu_choice == 'fd':
                                print("\tEnter the name of the account you want to find")
                                print("\n")
                                account_name = input("\tAccount Name:").strip()
                                print("\n")

                                if search_creds(account_name):
                                    account = search_creds(account_name)
                                    print("\tAccount\tUsername\tPassword")
                                    
                                    print(f"\t{account.site_name}\t{account.username}\t{account.password}")


                                else:
                                    print("\tAccount not found")
                                
                    
                            
                            elif menu_choice == 'dc':
                                if disp_creds():
                                    for cred in disp_creds(): 
                                        print(f"{cred.social_sitename}\t{cred.username}\t{cred.password}")
                                        print("\n")

                                else:
                                    print("\n")
                                    print("\t No details available")
                                    print("\n") 
                            
                        
                       
                            
                      

                    
                else:
                        print("That user does not exist")
                        create_user("","")
            elif menu_choice == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()