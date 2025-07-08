print( "Checking voting eligibility..." )

ageIn = input( "Please enter your age: " )
age = int( ageIn )

registered = input( "Are you registered? ( y/n )" )

if age >= 18 and registered == "y":
    print( "You are ready to vote!" )

else:
    print( "You aren't ready to vote..." )
