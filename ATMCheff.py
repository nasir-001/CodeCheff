# Authur: Nasir Lawal
# Date: 1st-08-July

""" 
Description: Positive integer 0 < X <= 2000 - the amount
of cash which Pooja wishes to withdraw.
Nonnegative number 0<= Y <= 2000 with two digits
of precision - Pooja's initial account balance.

"""

# Problem Source: <== CodeCheff ==>

def main():
	
	user_input()

def user_input():
	user_input = input("Enter the amount here: " + "\n")
	seperate = user_input.split(" ")
	amount = int(seperate[0])
	balance = float(seperate[1])
	if amount % 5 == 0 and amount < balance - 0.50:
		answer = balance - amount - 0.50
		print("{:.2f}".format(answer))
	elif amount % 5 != 0 or amount >= balance - 0.50:
		print("{:.2f}".format(balance))
		
if __name__ == "__main__":
	main()