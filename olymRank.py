# Authur: Nasir Lawal
# Date: 22-05-2022

'''
In Olympics, the countries are ranked by the total number of medals won. 
You are given six integers G1G_1G1​, S1S_1S1​, B1B_1B1​, and G2G_2G2​, S2S_2S2​, B2B_2B2​, 
the number of gold, silver and bronze medals won by two different countries respectively. 
Determine which country is ranked better on the leaderboard. It is guaranteed that there 
will not be a tie between the two countries.
'''

def main():
    test_cases = int(input())
    for i in range(test_cases):
        scores = list(map(int, input().split(" ")))
        country1 = scores[:3]
        country2 = scores[3:]
        if sum(country1) > sum(country2):
            print("1")
        else: 
            print("2")

if __name__ == '__main__':
    main()