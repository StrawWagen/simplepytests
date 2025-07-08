toAverage = 0
sum = 0

numOfNums = int( input( "Enter how many numbers to average: " ) )
sum = 0.0

for count in range( numOfNums ):
    sum = sum + float( input( "Num " + str( count ) + "/" + str( numOfNums ) + ": " ) )

average = sum / numOfNums
print( "Your average is..! :", average )