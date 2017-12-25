import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mime_type = {}
for _ in range(n):
    ext, mt = input().split()
    mime_type[ext.lower()] = mt

for _ in range(q):
    fname = input()
    if '.' not in fname:
        print('UNKNOWN')
        continue

    f_ext = fname.split('.')[-1].lower()
    print(f_ext, fname, file=sys.stderr)
    print(mime_type.get(f_ext, 'UNKNOWN'))
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
