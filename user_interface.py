from password_classes import User

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

def auth(name):
    '''
    method to check if a uer already exists in the users list
    '''
    return User.aunthenticate(name)



def main():
    print("Hello Welcome to your contact list. What is your name?")
    uname = input()

    print(f"Hello {uname}. what would you like to do?")
    print('\n')
    while True:
            print("Use these short codes : nu - create a new user, du - display users, lg - login ex -exit the password-chest ")
            short_code = input().lower()
            if short_code == 'nu':
                    print("New Contact")
                    print("-"*10)
                    print ("User name ....")
                    u_name = input()
                    print("Last name ...")
                    pass_name = input()
                    
                    save_user(create_user(u_name,pass_name)) # create and save new user
                    print ('\n')
                    print(f"New User {u_name} {pass_name} created")
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
                user = auth(search_user_name)
                if search_user_name==user:
                        print("Sucessful ...")
                else:
                        print("That user does not exist")
                        create_user()
            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
        main()