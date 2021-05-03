#Authur: Nasir Lawal
#Date: 19th-11-2019

for i in range(int(input())): # Loop through user_input
	names = list(input().strip().split()) # collect the name from user
	count = 0

	for a in names:
		count += 1	# Check how many names are in the list
	if count == 1:
		print(names[0].title()) # Print the name 

	elif count == 2: # Check the names again
		for a in names[0]: # Loop through the first name
			print(a[0].upper() + ". " + names[1].title()) # Print the name neatly formatted
			break # end the loop
			
	elif count == 3: # Check the names again 
		for a in names[0]: # loop through the first name in the list
			for n in names[1]: # loop through the second name in the list
				break # end the loop
			print(a[0].upper() + ". " + n[0].upper() + ". " + names[2].title()) # print the name 
			break # end the loop