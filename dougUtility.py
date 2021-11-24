# ============================#
# GETTING STRINGS FROM THE USER
# ============================#

# not empty
def getNotEmptyString(prompt):
    while True:
        try:
            userString = str(input(prompt + ":\t"))
            if userString == "":
                print("You cannot leave this field blank! Please enter a value.")
            else:
                return userString
        except ValueError:
            print("Input must be a valid string!")
        except Exception as e:
            print("Unexpected error: ", type(e), e)
            print("Shutting down program.")
            exit()

#not empty from list of choices
def getNotEmptyStringFromChoices(prompt, choices):
    while True:
        try:
            userString = str(input(prompt + ":\t"))
            if userString == "":
                print("You cannot leave this field blank! Please enter a value.")
            elif userString.lower() not in choices:
                string = "( "
                for choice in choices:
                    string += choice + " "
                string += ")" 
                print("You must choose a valid option! " + string)
            else:
                return userString
        except ValueError:
            print("Input must be a valid string!")
        except Exception as e:
            print("Unexpected error: ", type(e), e)
            print("Shutting down program.")
            exit()


# not empty single letter
def getNotEmptyChar(prompt):
    while True:
        try:
            userString = str(input(prompt + ":\t"))
            if userString == "":
                print("You cannot leave this field blank! Please enter a value.")
            elif len(userString) > 1:
                print("Your answer cannot exceed one character.")
            elif not userString.isalpha():
                print("You must enter a non-numeric letter.")
            else:
                return userString
        except ValueError:
            print("Input must be a valid string!")
        except Exception as e:
            print("Unexpected error: ", type(e), e)
            print("Shutting down program.")
            exit()

# ============================#
# GETTING NUMBERS FROM THE USER
# ============================#

# greater than zero -- isFloat True = float || False = int
def getNumberGZ(prompt, isFloat):
    while True:
        try:
            if isFloat:
                userNumber = float(input(prompt + ":\t"))
            else:
                userNumber = int(input(prompt + ":\t"))
            if userNumber < 1:
                print("Number must be greater than zero.")
            else:
                return userNumber
        except ValueError:
            print("Must be a valid integer!")
        except Exception as e:
            print("Unexpected error: ", type(e), e)
            print("Shutting down program.")
            exit()


# greater than zero with limit -- isFloat True = float || False = int
def getNumberGZL(prompt, limit, isFloat):
    while True:
        try:
            if isFloat:
                 userNumber = float(input(prompt + ":\t"))
            else:
                userNumber = int(input(prompt + ":\t"))
            if userNumber < 1 or userNumber > limit:
                print("Number must be greater than zero and less than " + str(limit) + ".")
            else:
                return userNumber
        except ValueError:
            print("Must be a valid number!")
        except Exception as e:
            print("Unexpected error: ", type(e), e)
            print("Shutting down program.")
            exit()

def getNumberFromChoices(prompt, choices, isFloat):
    while True:
        try:
            if isFloat:
                 userNumber = float(input(prompt + ":\t"))
            else:
                userNumber = int(input(prompt + ":\t"))
            if userNumber not in choices:
                print("You must choose an option from the list below: ")
                for choice in choices:
                    print(choice)
            else:
                return userNumber
        except ValueError:
            print("Must be a valid number!")
        except Exception as e:
            print("Unexpected error: ", type(e), e)
            print("Shutting down program.")
            exit()