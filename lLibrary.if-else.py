expected_day=int(input("enter your day"))
return_day=int(input("enter your day"))
expected_month=int(input("enter your month"))
return_month=int(input("enter your munth"))
expected_year=int(input("enter your year"))
return_year=int(input("enter your year"))
if expected_day>=return_day:
	if expected_month>=return_month:
		if expected_year>=return_year:
			print("no charge")
		else:
			print(10,000*(return_year-expected_year))
	else:
		print(500*(return_month-expected_month))
else:
	print(15*(return_day-expected_day))
    
    
    
    
    
    
    
    
    
    
    
    
 