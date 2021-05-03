#Authur: Nasir Lawal
#Date: 23rd-08-2019

"""
Description
Having a user to enter an integer followed by 
another integer and operator and then perform an 
operation based on the operator entered by the user.
"""

def main():

	first_num = int(input())
	second_num = int(input())

	operator = input()

	if operator == "+":
		print(first_num + second_num)
	elif operator == "-":
		print(first_num - second_num)
	elif operator == "*":
		print(first_num * second_num)
	elif operator == "/":
		print(first_num / second_num)

if __name__ == "__main__":
	main()