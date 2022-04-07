# ------------------------------------------------------------- 
# Author:  Sam Pollack
# Program: BillingModule
# 
# Description:  Function Storage
# Holds functions for processing in invoice output for Program3
# -------------------------------------------------------------

def readEmployeeName(name):
    employee = ''
    check = True
    while check:
        employee = input(name)
        if employee == '':
            print("Employee name must be entered.")
        else:
            check = False
    return employee

def readHourlyRate(rate):
    hourlyRate = 0.0
    check = True
    HOURLY_RATE_MIN = 20.00
    while check:
        hourlyRate = float(input(rate))
        if hourlyRate > HOURLY_RATE_MIN:
            check = False
        else:
            print("Invalid Hourly Rate, must be at least $20.00/hour.\n")
    return hourlyRate

def readWeeklyHours(hours):
    HOURS_WORKED_MIN = 35
    HOURS_WORKED_MAX = 80
    weekHours = 0.0
    check = True
    while check:
        weekHours = float(input(hours))
        if weekHours >= HOURS_WORKED_MIN and weekHours <= HOURS_WORKED_MAX:
            check = False
        else:
            print("Invalid number of hours, must be between 35 and 80.\n")
    return weekHours
