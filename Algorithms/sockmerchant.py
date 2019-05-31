from itertools import groupby
n = int(raw_input())
ar = map(int, raw_input().split())

pairs = 0
for num in [len(list(group)) for key, group in groupby(sorted(ar))]:
    pairs = pairs +  num/2
print pairs