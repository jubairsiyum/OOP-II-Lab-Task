# Python Program to Check Leap Year
def CheckLeap(year):
   
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print("Given Year is a leap year")
    else:
        print("Given Year is not a leap year")


year = int(input("Enter the year: "))


CheckLeap(year)
