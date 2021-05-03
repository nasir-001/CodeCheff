# Authur: Nasir Lawal
# Date: 17th-08-2019

""" Description
Hardness must be greater than 50.
Carbon content must be less than 0.7.
Tensile strength must be greater than 5600.

The grades are as follows:
Grade is 10 if all three conditions are met.
Grade is 9 if conditions (i) and (ii) are met.
Grade is 8 if conditions (ii) and (iii) are met.
Grade is 7 if conditions (i) and (iii) are met.
Garde is 6 if only one condition is met.
Grade is 5 if none of three conditions are met.

The first line contains an integer T, 
total number of testcases. Then follow T lines,
each line contains three numbers hardness, 
carbon content and tensile strength of the steel.
"""

def main():
	user_input = int(input())
	for n in range(user_input):
		num_string = input().strip().split()
		hardness = int(num_string[0])
		carbon = float(num_string[1])
		tensile = int(num_string[2])
		if hardness > 50 and carbon < 0.7 and tensile > 5600:
			print("10")
		elif hardness > 50 and carbon < 0.7 and tensile <= 5600:
			print("9")
		elif hardness <= 50 and carbon < 0.7 and tensile > 5600:
			print("8")
		elif hardness > 50 and carbon >= 0.7 and tensile > 5600:
			print("7")
		elif hardness > 50 or carbon < 0.7 or tensile > 5600:
			print("6")
		elif hardness <= 50 and carbon >= 0.7 and tensile <= 5600:
			print("5")
if __name__ == "__main__":
	main()