import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    a = sys.stdin.readline().strip()
    li.append(a)

li = sorted(list(set(li)))
li.sort(key=len)

for i in li:
    print(i)