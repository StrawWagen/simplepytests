
finisher = "-1"
print( "Sum and averager!\nEnter " + finisher + " to finish and get results!" )

result = "0"
count = 0
numSum = 0

while result != finisher:
    result = input( "Enter num: " )
    if result == finisher:
        continue

    try:
        numSum = numSum + float( result )
        count = count + 1

    except:
        print( "Please enter valid numbers only" )

if count != 0:
    average = numSum / count

print( "Average of inputted numbers, " + str( average ) + " Sum, " + str( numSum ) )