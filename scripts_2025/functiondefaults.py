defPassword = "The Password"
defPrompt = "Please enter the password: "
defTries = 2

def askForPassword( prompt = defPrompt, password = defPassword, numTries = defTries ):
    tries = 0

    while tries < numTries:
        tries = tries + 1
        attempt = input( prompt )

        if attempt == password:
            print( "Correct Password." )
            return 1
        
        elif tries < numTries:
            print( "Repeat Your Answer Please." )

    else:
        print( "Incorrect Password, no more tries." )

askForPassword( numTries = 3 )
