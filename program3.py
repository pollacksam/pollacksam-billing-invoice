# ------------------------------------------------------------- 
# Author:  Sam Pollack
# Program: Program3
# 
# Description:  Invoice
# Collects hours worked by employee to calculate amount due (includes overtime hours) 
# ------------------------------------------------------------- 

import BillingModule

def main():
    repeat = "y"
    while repeat == "y":
        totalHours = 0.0
        averageHours = 0.0
        overtimeHours = 0.0
        NUM_WEEKS = 4.0
        OT_RATE = 1.05
        REGULAR_HOURS = 160.0

        employee = BillingModule.readEmployeeName("\nEmployee Name: ")
        hourlyRate = BillingModule.readHourlyRate("Hourly Rate: ")
        week1 = BillingModule.readWeeklyHours("Enter hours worked for week 1: ")
        week2 = BillingModule.readWeeklyHours("Enter hours worked for week 2: ")
        week3 = BillingModule.readWeeklyHours("Enter hours worked for week 3: ")
        week4 = BillingModule.readWeeklyHours("Enter hours worked for week 4: ")

        #Calculations
        totalHours = week1 + week2 + week3 + week4
        regularHourRate = hourlyRate * REGULAR_HOURS
        averageHours = totalHours / NUM_WEEKS #Assuming all months have 4 weeks
        hoursWorked = totalHours - overtimeHours
        regularHourRate = hourlyRate * hoursWorked

        resource = 'Resource: ' + employee + '\tAverage weekly hours: ' + format(averageHours, '.2f')
        billable_hours = '\nTotal billable hours: ' + format(totalHours, '.2f') + '\trate: $' + format(hourlyRate, '.2f')
        regular_hours = 'Regular Hours: ' + format(hoursWorked, '.2f') + ' @ $' + format(hourlyRate, '.2f') + '\t= $' + format(regularHourRate, ',.2f')

        #Invoice Processing
        if totalHours > REGULAR_HOURS:
            overtimeRate = OT_RATE * hourlyRate
            overtimeHours = totalHours - REGULAR_HOURS
            overtimeHourRate = round(overtimeRate,2)
            overtimeHourAmount = round(overtimeHourRate * overtimeHours,2)
            overtimeTotal = round(overtimeHours * overtimeHourRate,2)
            invoiceAmount = regularHourRate + overtimeHourAmount
            overtimeHours = totalHours - REGULAR_HOURS
            output = '\n' + employee + " worked " + str(overtimeHours) + " hours of overtime. "
            billable_hours += '\nOvertime Hours: ' + format(overtimeHours, '.2f') + ' @ $' + format(overtimeRate, '.2f') + '\t= $' + format(overtimeHourAmount, ',.2f')
            
        else:
            invoiceAmount = regularHourRate
            overtimeHours = 0
            output = '\n' + employee + ' worked no overtime. '

        #Output
        print(output)
        print('\nInvoice')
        print(resource)
        print(billable_hours)
        print(regular_hours)
        print('Amount Due: $' + format(invoiceAmount, ',.2f'))
        repeat = input('Enter another employee? ("y"=yes): ')

main()
