import re


p = re.compile(r'(\d+):(\d+):(\d+)')
n = int(input())
times = [p.findall(input())[0] for i in range(n)]

print(':'.join(min(times)))
