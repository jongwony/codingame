from statistics import median

n = int(input())
x_list, y_list = list(zip(*[[int(j) for j in input().split()] for _ in range(n)]))
m = int(median(y_list))
print(max(x_list) - min(x_list) + sum(map(lambda x: abs(x - m), y_list)))
