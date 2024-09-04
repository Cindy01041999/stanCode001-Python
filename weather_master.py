"""
File: weather_master.py
Name: Chang Yen Yu
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	Assume EXIT=-100, if the temperature != -100,
	should calculate the highest, lowest, average of temperatures, and the number of cold days.
	"""
	print('"Weather Master 4.0"!')
	guess = int(input('Next Temperature: (or -100 to quit)? '))
	if guess == EXIT:
		print('No temperature were entered.')
	else:
		maximum = guess
		minimum = guess
		sum_temp = guess
		sum_count = 1
		cold_day = 0
		if guess < 16:
			cold_day += 1
		while True:
			guess = int(input('Next Temperature: (or -100 to quit)? '))
			if guess == EXIT:
				break
			elif guess > maximum:
				maximum = guess
				sum_count += 1
				sum_temp = sum_temp + guess
			elif guess < minimum:
				minimum = guess
				sum_count += 1
				sum_temp = sum_temp + guess
			else:
				# minimum < guess < maximum
				sum_count += 1
				sum_temp = sum_temp + guess
			if guess < 16:
				cold_day += 1
		average = sum_temp / sum_count
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(float(average)))
		print(str(cold_day) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
