#Question 4 - Write a function to return if the given year 
# is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
#The second one is your leap year question. If I put in 1900 it will return as True, 
# when 1900 was not a leap year and should be false.

def is_leap_year(a_year):
    if int(a_year) % 4 == 0:
        if int(a_year) % 100 == 0 and int(a_year) % 400 != 0:
            print(False)
        else: print(True)
    else: print(False)  

prompt = "Let's test is your year is a leap year."
prompt += "\nEnter 'quit' to end the program."

a_year= ""

while a_year != 'quit':
    a_year=input("Please enter the year to see if it is a leap year: ")
    print(is_leap_year(a_year))