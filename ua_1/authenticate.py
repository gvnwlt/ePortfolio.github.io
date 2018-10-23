# Authentication class to handle user access

# using hashlib for md5 hashing and re to pull text from file strings 
import hashlib
import re


class ZooUser: 
    # build user profile here 
    def __init__(self):
        print("Welcome to the Zoo User Access System!")
        # create instance of hash tool
        self.attempts = 3
        self.passwordValid = False
        self.profile = ""
        # open file, read lines to string var; close file
        _ = open('credentials.txt', 'r'); self.credentials = _.readlines(); _.close()
        
    
    # authenticates user by examining a credentials text file line by line 
    def authenticate (self, userName, password):
        # construct user messages and update attempts
        self.attempts -= 1
        nameFound = False
        e_name_message = "User \"" + userName + "\" not found. You have " + str(self.attempts) + " attempts left."
        e_password_message = "Password is incorrect. You have " + str(self.attempts) + " attempts left."
        success_message = "***Zoo user login for " + userName.capitalize().split('.')[0] + " successful.***\n"
        # hash the password
        hashedPassword = hashlib.md5(password.encode('utf8')).hexdigest()
        for line in self.credentials:
            #find if name matches @ beginning of line with regex 
            if re.match(r'^' + userName, line):
                nameFound = True 
                if hashedPassword in line:
                    self.passwordValid = True
                    # get role profile for user at end of line
                    role = line.split()[-1]
                    # open file, read lines to string var; close file
                    _ = open(role+'.txt', 'r'); self.profile = _.read(); _.close()
                    print(success_message)
                    return True
        # if name is found print regular error, otherwise notify user about name and error (ternary backwards <-) 
        print((e_name_message, e_password_message)[nameFound])
        
    
        
            
                    
            