overtime = 40
overtimeRateAdded = 0.5
print( "Hourly pay calculator!" )

rateIn = input( "Enter hourly rate: " )
rate = int( rateIn )

hoursIn = input( "Enter hours worked this week: " )
hours = int( hoursIn )

hoursWorkedOvertime = hours - overtime

rawPay = hours * rate
pay = rawPay
overtimePay = hoursWorkedOvertime * rate * overtimeRateAdded
overtimePay = round( overtimePay )

overtimeAdded = ""

if overtimePay > 0:
    pay = pay + overtimePay
    overtimeAdded = "Overtime pay, " + str( overtimePay ) + "\n"

print( "Your pay is " + str( rawPay ) + "\n" + overtimeAdded + "Total, final pay is; " + str( pay ) + "\n" )
