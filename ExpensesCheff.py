# Authur: Nasir Lawal
# Date: 11-Aug-2019

"""
Problem Source: <== CodeCheff ==>
"""

def main():
	
	user_input = int(input())

	for a in range(user_input):
		q , p = input().split()
		quantity = int(q)
		price = int(p)
		if quantity > 1000:
			per = quantity / 100
			ans = per * 90 * price
			print("{:.6f}".format(ans))
		else:
			ans2 = quantity * price
			print("{:.6f}".format(ans2))

if __name__ == "__main__":
	main()