# Authur: Nasir Lawal
# Date: 22-05-2022

'''
The weather report of Chefland is Good if the number of sunny days in a week is strictly 
greater than the number of rainy days.
Determine if the weather report of Chefland is Good or not.
'''

def main():
    test_cases = int(input())
    for i in range(test_cases):
        weather = list(map(int, input().split(" ")))
        good_weather = []
        bad_weather = []
        for x in weather:
            if x == 1:
                good_weather.append(x)
            else: 
                bad_weather.append(x)
        if len(good_weather) > len(bad_weather):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
