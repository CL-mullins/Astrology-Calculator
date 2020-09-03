# Astrology-Calculator
A fairly simple calculator that takes in month and date and returns a user's birth sign.

The user enters in their birth month which the script takes as user_birthMonth. The string value for each month's name is then converted to a number #1 through #12 corresponding with month order. Then, the terminal prompts the user for a birth date, which is stored in user_birthDate. This value is stored as an integer. If the number is smaller than 20, the user's zodiacal Sun sign is the one that governs dates 1 - 20 of the month and if above 20, the user's zodiac sign is the one that governs the latter part of the month. 

Each zodiac sign goes in zodiacal order (Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces) with each sign governing about 30 days each starting on the 20th of each month. The zodiacal year begins in Aries which is the latter part of March (21 - 31) through the beginning of April (1 - 20). This same formula follows through the entirety of the calendar year with January beginning with Capricorn and ending with Aquarius.

For more in depth information regarding your zodiac sign, including your entire birth chart check these useful websites:
~https://www.astro.com/index.htm
~https://cafeastrology.com/


Intended Commits:
•Display error message and reprompt input message when user inputs an integer, boolean or float for the user_birthMonth value
•Display error message and reprompt input message when user inputs a string, boolean, or float for user_birthDate value
•Display welcome message at start
•Display "Your Sun Sign is _" to explain to the user that what is being reported is not their "zodiac sign" but rather their sun sign. The      constellation the sun was in at the time of their birth

Potential Commits:
•Moon Sign Integration: Parse data from an Ephemeris such as this one to retrieve user's "Moon sign" or, the sign the moon was in. https://www.findyourfate.com/astrology/ephemeris/2020.html#april
[Note]: Highly unlikely that this will actually be done due to parsing difficulties and the need to pull from atleast 100 data sheets.
[Note]: If this is done, though highly unlikely, I will also make an effort to include the user's Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto placements for more data, effectively creating my own birth chart report.
[Note]: I have not been able to find

