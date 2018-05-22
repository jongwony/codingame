import sys


r_1 = int(input())
r_2 = int(input())


while r_1 != r_2:
    while r_1 < r_2:
        r_1 += sum(map(int, str(r_1)))
    while r_1 > r_2:
        r_2 += sum(map(int, str(r_2)))
        
print(r_1)
