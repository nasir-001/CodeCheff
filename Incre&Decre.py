# Authur: Nasir Lawal
# Date: 16-Aug-2019

"""
Write a program to obtain a number N and increment 
its value by 1 if the number is divisible by 4 
otherwise decrement its value by 1.
"""

def main():

	user_input = int(input())
	if user_input % 4 == 0:
		user_input += 1
		print(user_input)
	else:
		user_input -= 1
		print(user_input)

if __name__ == "__main__":
	main()