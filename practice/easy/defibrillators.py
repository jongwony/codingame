import math

to_dot = lambda x: float(x.replace(',', '.'))


def rearrange(x):
    *_info, _lon, _lat = x
    return [*_info, to_dot(_lon), to_dot(_lat)]


def dist(defib):
    idx, name, addr, phone, u_lon, u_lat = defib
    dx = (lon - u_lon) * math.cos((lat + u_lat)/2)
    dy = (lat - u_lat)
    return math.hypot(dx, dy) * 6371


lon = to_dot(input())
lat = to_dot(input())

n = int(input())
defibs = [input().split(';') for _ in range(n)]

closest = min(map(rearrange, defibs), key=dist)
print(closest[1])
