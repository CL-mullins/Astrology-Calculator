def big_two(hour,minute,sun_Sign):
#Something is wrong with the conditional statements where it is alwways evaluating as the first if
#despite falling in a different range
    if (int(hour) >= 6 and int(minute) >= 00) or (int(hour <= 8) and int(minute) <= 00):
        if sun_Sign == "Aries":
            rising_sign = "Taurus"
            print(rising_sign)
        if sun_Sign == "Taurus":
            rising_sign = "Gemini"
            print(rising_sign)   
        if sun_Sign == "Gemini":
            rising_sign = "Cancer"
            print(rising_sign)  
        if sun_Sign == "Cancer":
            rising_sign = "Leo"
            print(rising_sign)
        if sun_Sign == "Leo":
            rising_sign = "Virgo"
            print(rising_sign)
        if sun_Sign == "Virgo":
            rising_sign = "Libra"
            print(rising_sign)
        if sun_Sign == "Libra":
            rising_sign = "Scorpio"
            print(rising_sign)
        if sun_Sign == "Scorpio":
            rising_sign = "Sagittarius"
            print(rising_sign)
        if sun_Sign == "Sagittarius" :
            rising_sign = "Capricorn"
            print(rising_sign)   
        if sun_Sign == "Capricorn":
            rising_sign = 'Aquarius'
            print(rising_sign)
        if sun_Sign == "Aquarius":
            rising_sign = "Pisces"
            print(rising_sign)
        if sun_Sign == "Pisces": 
            rising_sign = "Aries"
            print(rising_sign)
    elif (int(hour) >= 8 and int(minute) >= 00) or (int(hour <= 10) and int(minute) <= 00):

        if sun_Sign == "Aries":
            rising_sign = "Gemini"
            print(rising_sign)
        if sun_Sign == "Taurus":
            rising_sign = "Cancer"
            print(rising_sign)   
        if sun_Sign == "Gemini":
            rising_sign = "Leo"
            print(rising_sign)  
        if sun_Sign == "Cancer":
            rising_sign = "Virgo"
            print(rising_sign)
        if sun_Sign == "Leo":
            rising_sign = "Libra"
            print(rising_sign)
        if sun_Sign == "Virgo":
            rising_sign = "Scorpio"
            print(rising_sign)
        if sun_Sign == "Libra":
            rising_sign = "Sagittarius"
            print(rising_sign)
        if sun_Sign == "Scorpio":
            rising_sign = "Capricorn"
            print(rising_sign)
        if sun_Sign == "Sagittarius" :
            rising_sign = "Aquarius"
            print(rising_sign)   
        if sun_Sign == "Capricorn":
            rising_sign = 'Pisces'
            print(rising_sign)
        if sun_Sign == "Aquarius":
            rising_sign = "Aries"
            print(rising_sign)
        if sun_Sign == "Pisces": 
            rising_sign = "Taurus"
            print(rising_sign)
    elif (int(hour) >= 10 and int(minute) >= 00) or (int(hour <= 12) and int(minute) <= 00):
        if sun_Sign == "Aries":
            rising_sign = "Cancer"
            print(rising_sign)
        if sun_Sign == "Taurus":
            rising_sign = "Leo"
            print(rising_sign)   
        if sun_Sign == "Gemini":
            rising_sign = "Virgo"
            print(rising_sign)  
        if sun_Sign == "Cancer":
            rising_sign = "Libra"
            print(rising_sign)
        if sun_Sign == "Leo":
            rising_sign = "Scorpio"
            print(rising_sign)
        if sun_Sign == "Virgo":
            rising_sign = "Sagittarius"
            print(rising_sign)
        if sun_Sign == "Libra":
            rising_sign = "Capricorn"
            print(rising_sign)
        if sun_Sign == "Scorpio":
            rising_sign = "Aquarius"
            print(rising_sign)
        if sun_Sign == "Sagittarius" :
            rising_sign = "Pisces"
            print(rising_sign)   
        if sun_Sign == "Capricorn":
            rising_sign = 'Aries'
            print(rising_sign)
        if sun_Sign == "Aquarius":
            rising_sign = "Taurus"
            print(rising_sign)
        if sun_Sign == "Pisces": 
            rising_sign = "Gemini"
            print(rising_sign)