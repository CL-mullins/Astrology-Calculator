#Need to create variables for month and date
#Input function that asks user for birth day and birth month
    #Compares birth day and month to data
    #If Month = 3 && Day > 21 Sun Sign == Pisces

#Was considering doing moon sign, however, getting the ephemeris and reading 
#the data from it might turn this into a week-long project with assistance
#rather than a 3 day long project


 
user_birthMonth = input("What month were you born in? : ")
user_birthDate = input("What day were you born? : ")


if user_birthMonth == "January":
    month = 1
    if int(user_birthDate) <= 19:
        print("You are a Capricorn")
    if int(user_birthDate) >= 20:
        print("You are an Aquarius")

if user_birthMonth == "February":
    month = 2
    if int(user_birthDate) <= 19:
        print("You are an Aquarius")
    if int(user_birthDate) >= 20:
        print("You are a Pisces")

if user_birthMonth == "March":
    month = 3
    if int(user_birthDate) <= 19:
        print("You are a Pisces")
    if int(user_birthDate) >= 20:
        print("You are an Aries")     

if user_birthMonth == "April":
    month = 4
    if int(user_birthDate) <= 19:
        print("You are an Aries")
    if int(user_birthDate) >= 20:
        print("You are a Taurus")                            

if user_birthMonth == "May":
    month = 5
    if int(user_birthDate) <= 19:
        print("You are a Taurus")
    if int(user_birthDate) >= 20:
        print("You are a Gemini")

if user_birthMonth == "June":
    month = 6
    if int(user_birthDate) <= 19:
        print("You are a Gemini")
    if int(user_birthDate) >= 20:
        print("You are a Cancer")  

if user_birthMonth == "July":
    month = 7
    if int(user_birthDate) <= 19:
        print("You are a Cancer")
    if int(user_birthDate) >= 20:
        print("You are a Leo")  

if user_birthMonth == "August":
    month = 8
    if int(user_birthDate) <= 19:
        print("You are a Leo")
    if int(user_birthDate) >= 20:
        print("You are a Virgo")  


if user_birthMonth == "September":
    month = 9
    if int(user_birthDate) <= 19:
        print("You are a Virgo")
    if int(user_birthDate) >= 20:
        print("You are a Libra")  

if user_birthMonth == "October":
    month = 10
    if int(user_birthDate) <= 19:
        print("You are a Libra")
    if int(user_birthDate) >= 20:
        print("You are a Scorpio")  

if user_birthMonth == "November":
    month = 11
    if int(user_birthDate) <= 19:
        print("You are a Scorpio")
    if int(user_birthDate) >= 20:
        print("You are a Sagittarius")  

if user_birthMonth == "December":
    month = 12
    if int(user_birthDate) <= 19:
        print("You are a Sagittarius")
    if int(user_birthDate) >= 20:
        print("You are a Capricorn")                                              
#def sunSign(user_birthMonth,userbirthDay)
