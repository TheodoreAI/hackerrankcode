# Mateo Estrada 
# Easy Challenge
# Make a program that tells you whether an input int 
# is a leap year or not.

# Description: In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.


def is_leap(year):
	"""To Figure this one out you need to think in 
	terms of the modulo operator as opposed to division."""
	leap = False

	if year % 4 == 0:
		leap = True
		if year % 100 ==0:
			leap = False
			if year % 400 == 0:
				leap = True


	return leap 


year = int(input()) # reads from the STDIN and passes to the function.
print(is_leap(year))