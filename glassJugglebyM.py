n = int(raw_input())
lst = []
for x in range(n):
    lst.append(int(raw_input()))

lst.sort()
a = lst[1::2]
b = lst[0::2]

c = a[::-1] + b
m = 0
for x in range(1, len(c)):
    d = abs(c[x-1]-c[x])
    if d > m:
        m = d
print m
