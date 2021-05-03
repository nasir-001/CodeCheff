#Authur: Nasir Lawal
#Date: 23-Nov-2019

"""
Description: Write a program that print Vowel if the given input is vowel else consonants
"""

def main():

	vowel = ["A", "E", "I", "O", "U"]
	user_input = input()
	for x in vowel:
		pass
	if user_input in vowel:
		print("Vowel")
	else:
		print("Consonant")

if __name__ == "__main__":
	main()