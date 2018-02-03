res = {}
def dict_append(d, s):
    s1, *sn = s
    d1 = d.get(s1, {})
    if not d1: d[s1] = d1
    if len(sn) > 0: dict_append(d1, sn)

def dep_count(d):
    return len(d) + sum((dep_count(d[k]) for k in d))

n = int(input())
for i in range(n):
    telephone = input()
    dict_append(res, telephone)

print(dep_count(res))
