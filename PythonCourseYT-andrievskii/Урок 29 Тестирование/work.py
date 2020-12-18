def full_name(first, last, middle = ""):
	if middle:
		full = first + " " + last + " " + middle
	else: 
		full = first + " " + last

	return full.title()
#print(full_name("Oleg", "Ivanov"))