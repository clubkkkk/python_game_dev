import sys

def silly_age_joke():
	print("How old are you?")
	
	
	age = int(sys.stdin.readline())
	if age >= 10 and age <= 20:
		print('What is @@@@@@@@@@@@@@@@@?')
	else:
		print('Huh?')
		
silly_age_joke()