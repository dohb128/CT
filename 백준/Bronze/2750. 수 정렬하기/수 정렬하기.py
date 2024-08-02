import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    a = int(sys.stdin.readline())
    li.append(a)

li.sort()
for i in li:
    print(i)