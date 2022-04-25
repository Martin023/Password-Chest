# imports for generating random passwords,and Credentials class

import secrets
import string
from password_classes import Credentials,User



def create_new_account(accountname, accountpassword):
	""" Function to create a new account and the accountname & accountpassword"""
	new_credential = Credentials(accountname, accountpassword)
	return new_credential


def save_new_account(credentials):
	"""Function to save all the account details """
	credentials.save_account()

def check_existing_account(name):
    """ Function to check if an account with the exact searched account name exists"""
    
    return Credentials.find_account_by_name(name)

def delete_account(credentials):
    
    """ Function to delete an account together with the accountpassword"""
    
    return Credentials.delete_account(credentials)

def find_account(accountname):
	""" Function to find an account by name"""
	return Credentials.find_account_by_name(accountname)

def display_account():
    """Function to display all accounts saved"""
    return Credentials.display_account()

def delete_account(credentials):
	"""Function to delete all accounts saved"""
	return Credentials.delete_account(credentials)


def login():

	print("Welcome to Pass-Chest")
	print("\n")
	while True:
		
		# Register page
		print("\t\t\tCreate new account or login to exising account: \n\n\n Create account :  cc / CC \n\n Login : ll / LL")
		choice = input().lower()
		if choice == "cc":
			print("Create new username")
			newusername = input().lower()

			print("Enter your password")
			newpassword = input()

			print("Re-enter password")
			confirmpassword = input()

			while confirmpassword != newpassword:
				print("Oops! Passwords do not match!")

				print("Enter your password")
				newpassword = input()

				print("Confirm your password")
				confirmpassword = input()

				print("\n")
			else:
				print(f"\t\t Welcome {newusername} to password the tresure")
				print(f"Your login details are Username: {newusername} \nPassword: {newpassword}")
				print("\n")
				print("++" *100)
				print("Login")
				print("Enter your Username")
				loginUsername = input().lower()
				print("Enter your password")
				loginPassword = input()
			  
				##Verify users:

				if loginUsername != newusername or loginPassword != newpassword:
					print("incorrect password or username")
					print("\n")
					print("Enter your Username")
					loginUsername =input().lower()
					print("\nEnter your password")
					loginPassword = input()
					
				else:
					print(f"\t\t Welcome back, {loginUsername}! ")
					print("\n")
					print("++"*100)
					print("Welcome to password Chest")
					print("Choose options 1,2,3,4 or 5")
					

				while True:
					print("\n \t\t MENU :")
                   
					print("\t\t 1. Add new Account")
					print("\t\t 2. View saved accounts")
					print("\t\t 3. Search saved accounts")
					print("\t\t 4. Delete saved accounts")
					
					menuOpt = input()

					if menuOpt == '1':
						while True:
							print("-"*100)
							print("Add account? y / n")
							choice3 = input()

							if choice3 == 'y':
								print("Enter account name")
								accountname = input()
									# print("Enter your Username")
									# loginUsername =input()
								print("Would you like to enter your password or generate one? en :enter/ a :atomatic generated")
								password = input().lower()
								if password == "en":
									accountpassword = input()
										# print("Enter your password")
								
									print("Succesfull creation of account")
									print(f"Account name: {accountname} \nPassword: {accountpassword}")  
									save_new_account(create_new_account(accountname, accountpassword))                          
								elif password == "a":
									letters = string.ascii_lowercase + string.digits + string.punctuation
									accountpassword = ''.join(secrets.choice(letters) for i in range(1,10))
									print("Success! You have created a new account. See details below.")
									print(f"Account name: {accountname} \nPassword: {accountpassword}")  
									print("\n")
									save_new_account(create_new_account(accountname, accountpassword))
								else:
									print("Invalid! Please enter Valid choice")
									print("\n")
									
									
							elif choice3 == 'n':
								break
							else:
								print("Use either y or n")



					elif menuOpt == '2':
						while True:
    
							print(" Here's a list of accounts saved")
							if display_account():
								for account in display_account():
									print(f"Account Name:{account.accountname}")
									print(f"Password:{account.accountpassword}")
									print("\n")
									print("+"*100)
							else:
								print("Oops! no accounts found!")
							print("Back to Main menu y/n")
							option = input().lower()
							if option == "y":
								break

							elif option == "n":
								continue
							else:
								print("Enter a valid option")
								
					  
					elif menuOpt == '3':
						print("\n")
						print("-"*100)
						print("Search account by name")
						option1 = input()
						if check_existing_account(option1):
							searchaccount = find_account(option1)
							print("Account Found!")
							print(f"Account name: {searchaccount.accountname}")
						else: print("That Account does not exist")
					# delete
					elif menuOpt == '4':
    					
						print("DELETING AN  ACCOUNT ??")
						print("Search account by name")
						option2 = input()
						if check_existing_account(option2):
							searchaccount = find_account(option2)
							print("Account Found!")
							print(f"Account name: {searchaccount.accountname}")
							print(f"Are you sure you want to delete {searchaccount.accountname} y/n")
							option3 = input()
							if option3 == 'y':
								delete_account(searchaccount)
								print("Account Deleted!")
								print("\n")
								print("-"*100)
							elif option3 == 'n':
								continue
							else:
								print("Choose y/n")
						else: 
							print("That Account does not exist")
							print("-"*100)

					
					else:
						print("Invalid choice! Choose from the options below!")
						continue

		elif choice == "ll":
			print("Enter your username")
			existingusername = input().lower

			print("Enter your password")
			existingpassword = input()

			if existingusername != "person" or existingpassword != "11111":
				print("Seems you do not have an account please create one first try again or press Ctrl+z to start again")
                
				print("\n")
                
				print("Enter your username")
				existingusername = input()
				print("Enter your password")
				existingpassword = input()

			elif existingusername == "person" and existingpassword == "11111":
				print("\n")
				print("You have successfully logged in ")
				print("-"*100)
				print("Select an option below")

			while True:
					print("\n")
					print("1.Add new Account")
					print("2.View saved accounts")
					print("3.Search saved accounts")
					print("4.Delete saved accounts")
					
					choice2 = input()

					if choice2 == '1':
						while True:
							print("-"*100)
							print("Add account? y/n")
							choice3 = input()

							if choice3 == 'y':
								print("Enter account name")
								accountname = input()
									# print("Enter your Username")
									# loginUsername =input()
								print("Would you like to enter your password or generate one? E/G")
								password = input()
								if password == "E":
									accountpassword = input()
										# print("Enter your password")
								
									print("Success! You have created a new account. See details below.")
									print(f"Account name: {accountname} \nPassword: {accountpassword}")  
									save_new_account(create_new_account(accountname, accountpassword))                          
								elif password == "G":
									letters = string.ascii_lowercase + string.digits + string.punctuation
									accountpassword = ''.join(secrets.choice(letters) for i in range(1,10))
									print("Success! You have created a new account. See details below.")
									print(f"Account name: {accountname} \nPassword: {accountpassword}")  
									print("\n")
									save_new_account(create_new_account(accountname, accountpassword))
								else:
									print("Invalid! Please enter Valid choice")
									print("\n")
									print("-"*100)
									
							elif choice3 == 'n':
								break
							else:
								print("Use either y: for Yes  or n: For NO")



					elif choice2 == '2':
						while True:
    
							print("\t \t Currently saved accounts are: ")
							if display_account():
								for account in display_account():
									print(f"Account Name:{account.accountname}")
									print(f"Password:{account.accountpassword}")
									print("\n")
									print("-"*100)
							else:
								print("Oops!Seems you have no accounts yet!")
							print("Back to Main menu y/n")
							option = input().lower()
							if option == "y":
								break

							elif option == "n":
								continue
							else:
								print("Enter a valid option")
								
					  
					elif choice2 == '3':
						print("\n")
						print("-"*100)
						print("Search account by name")
						option1 = input()
						if check_existing_account(option1):
							searchaccount = find_account(option1)
							print("Account Found!")
							print(f"Account name: {searchaccount.accountname}")
						else: print("That Account does not exist")
					# delete
					elif choice2 == '4':
    					
						print("THIS OPTION WILL DELETE ALL YOUR ACCOUNT")
						print("Search account by name")
						option2 = input()
						if check_existing_account(option2):
							searchaccount = find_account(option2)
							print("Account Found!")
							print(f"Account name: {searchaccount.accountname}")
							print(f"Are you sure you want to delete {searchaccount.accountname} y/n")
							option3 = input()
							if option3 == 'y':
								delete_account(searchaccount)
								print("Account Deleted!")
								print("\n")
								print("-"*100)
							elif option3 == 'n':
								continue
							else:
								print("Choose y/n")
						else: 
							print("That Account does not exist")
							print("-"*100)

					
		else:
			print("Invalid choice please choose Login or create account")
			continue
   
if __name__ == "__main__":
	login()
