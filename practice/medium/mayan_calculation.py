from collections import deque

l, h = [int(i) for i in input().split()]

numerals = [input() for _ in range(h)]
numerals_h_split = [list(zip(*[iter(x)] * h)) for x in numerals]
part_numerals = list(zip(*numerals_h_split))

s1 = int(input())
s1_input = (tuple(input()) for x in range(s1))
s1_split = list(zip(*[s1_input] * h))
s2 = int(input())
s2_input = (tuple(input()) for x in range(s2))
s2_split = list(zip(*[s2_input] * h))
operation = input()

left = sum(part_numerals.index(v) * 20 ** i for i, v in enumerate(reversed(s1_split)))
right = sum(part_numerals.index(v) * 20 ** i for i, v in enumerate(reversed(s2_split)))
formulas = '{0}{1}{2}'.format(left, operation, right)
eval_num = int(eval(formulas))

res = deque()
while eval_num > 0:
    d, m = divmod(eval_num, 20)
    res.appendleft(m)
    
    if d <= 0:
        break
    
    eval_num = (eval_num - m) // 20

result = [part_numerals[x] for x in res] or [part_numerals[0]]
for i in result:
    for j in i:
        print(''.join(j))
