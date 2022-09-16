# Authur: Nasir Lawal
# Date: 21-05-2022

'''
Faizal is very sad after finding out that he is responsible for Sardar's death. 
He tries to drown his sorrows in alcohol and gets very drunk. Now he wants to return home
but is unable to walk straight. For every 333 steps forward, he ends up walking one step backward.

Formally, in the 1st second he moves 3 steps forward, in the 2nd second 
he moves 1 step backwards, in the 3rd second he moves 3 steps forward, in 4th
second 1 step backwards, and so on.
'''

def main():
    text_cases = int(input())
    for i in range(text_cases):
        user_input = int(input())
        steps = 0
        for x in range(1, user_input+1):
            if x % 2 != 0:
                steps += 3
            else:
                steps -= 1
        print(steps)

if __name__ == '__main__':
    main()