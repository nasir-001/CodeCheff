#Authur: Nasir Lawal
#Date: 20th-08-2019

def main():

	user_input = int(input())

	for a in range(user_input):
		num_one, num_two = list(map(int, input().split()))
		
		if num_one > num_two:
			print(">")
		elif num_one < num_two:
			print("<")
		elif num_one == num_two:
			print("=")

if __name__ == "__main__":
	main()