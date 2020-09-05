import datetime
from calculations import big_two
#Need to create variables for month and date
#Input function that asks user for birth day and birth month
    #Compares birth day and month to data
    #If Month = 3 && Day > 21 Sun Sign == Pisces

#Was considering doing moon sign, however, getting the ephemeris and reading 
#the data from it might turn this into a week-long project with assistance
#rather than a 3 day long project

sun_Sign = ""
rising_sign = ""
print("Welcome to the Astrological Calculator!") 
print("This program will allow you to figure out where the Sun was at the time you were born!")
#month = input("What month were you born in? : ")
#day = input("What day were you born? : ")
date_entry = input('Enter your birthdate in YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
time_entry = input('Enter the time you were born in HH-MM format(Set to 12-00 if time is unknown): ')
hour, minute = map(int, time_entry.split('-'))
time1 = datetime.time(hour, minute)

#if the hour is 6 or greater and the minute is 00 or greater, return Aquarius

#capricorn_rs = { 
#        6 : 'Aquarius', 
#        7 : 'Aquarius',
#        8 : 'Aquarius',
#        8:'Pisces'
#        }

#Set Sun Sign from Month + Date
if month == int('01'):
    if int(day) <= 19:
        sun_Sign = "Capricorn"
        print("You are a " + sun_Sign)

    if int(day) >= 20:
        sun_Sign = "Aquarius"
        print("You are an Aquarius")

if month == int('02'):
    if int(day) <= 19:
        sun_Sign = "Aquarius"
        print("You are an Aquarius")
    if int(day) >= 20:
        sun_Sign = "Pisces"
        print("You are a Pisces")

if month == int('03'):
    if int(day) <= 19:
        sun_Sign = "Pisces"
        print("You are a Pisces")
    if int(day) >= 20:
        sun_Sign = "Aries"
        print("You are an Aries")     

if month == int('04'):
    if int(day) <= 19:
        sun_Sign = "Aries"
        print("You are an Aries")
    if int(day) >= 20:
        sun_Sign = "Taurus"
        print("You are a Taurus")                            

if month == int('05'):
    if int(day) <= 19:
        sun_Sign = "Taurus"
        print("You are a Taurus")
    if int(day) >= 20:
        sun_Sign = "Gemini"
        print("You are a Gemini")

if month == int('06'):
    if int(day) <= 19:
        sun_Sign = "Gemini"
        print("You are a Gemini")
    if int(day) >= 20:
        sun_Sign = "Cancer"
        print("You are a Cancer")  

if month == int('07'):
    if int(day) <= 19:
        sun_Sign = "Cancer"
        print("You are a Cancer")
    if int(day) >= 20:
        sun_Sign = "Leo"
        print("You are a Leo")  

if month == int('08'):
    if int(day) <= 19:
        sun_Sign = "Leo"
        print("You are a Leo")
    if int(day) >= 20:
        sun_Sign = "Virgo"
        print("You are a Virgo")  


if month == int('09'):
    if int(day) <= 19:
        sun_Sign = "Virgo"
        print("You are a Virgo")
    if int(day) >= 20:
        sun_Sign = "Libra"
        print("You are a Libra")  

if month == int('10'):
    if int(day) <= 19:
        sun_Sign = "Libra"
        print("You are a Libra")
    if int(day) >= 20:
        sun_Sign = "Scorpio"
        print("You are a Scorpio")  

if month == int('11'):
    if int(day) <= 19:
        sun_Sign = "Scorpio"
        print("You are a Scorpio")
    if int(day) >= 20:
        sun_Sign = "Sagittarius"
        print("You are a Sagittarius")  

if month == int('12'):
    if int(day) <= 19:
        sun_Sign = "Sagittarius"
        print("You are a Sagittarius")
    if int(day) >= 20:
        sun_Sign = "Capricorn"
        print("You are a Capricorn") 

big_two(hour,minute,sun_Sign)

#Set Rising Sign from time_entry Time + sun_Sign
#if sun_Sign == "Capricorn":
#        rising_sign == capricorn_rs[hour]
#        print("You have an Aquarius Rising!")


#check if birth time falls in a certain range

#create a dictionary for each zodiac sign with the key as a tuple (range) and value being zodiac sign
#each key should be a variable that represents a certain range. The range should be in 24hr HHMM form. Ex. 0600 to 0800.
#Each should exclude numbers that fall out of time range such as 0660+ & 0860

#if sun_Sign == "Capricorn":

#    rising_sign = capricorn_rs[birth_hour]
#aries_rs = { '6-8' : 'Taurus','8-10': 'Gemini'}


#print(rising_sign)


