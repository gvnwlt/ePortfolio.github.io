#Converting previous Java version ZooUserAccess to Python to make more efficient. 

# import module to attempt authorizing user access
from authenticate import ZooUser

# zoo system  
def runZooSystem(profile):
    #display user profile
    print(profile)
    #now keep the system running until user decides to log out 
    while True:
        prompt = input("Would you like to continue running? 'y' for yes 'n' for no: ")
        if prompt == 'y':
            continue
        elif prompt == 'n':
            return

# begin zoo user access system 
def main():
    user = ZooUser()
    # get current attempts value and handle auth and access in while loop
    # then exit program
    attempts = user.attempts
    while (attempts > 0):
        userName = input("Please enter login name:")
        password = input("Please enter password: ")
        user.authenticate(userName, password)
        if user.passwordValid:
            runZooSystem(user.profile)
            break
        # update attempts left
        attempts = user.attempts
    # Exiting due to user logout or attempt max out  
    print("\n***Exiting program.***")

main()