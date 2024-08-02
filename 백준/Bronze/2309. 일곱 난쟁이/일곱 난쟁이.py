import sys

li = []

for _ in range(9):
    n = int(sys.stdin.readline())
    li.append(n)

num = sum(li)
target = num - 100

for i in range(9):
    for j in range(i+1, 9):
        if li[i] + li[j] == target:
            li.pop(j)
            li.pop(i)
            break
    else: continue
    break

li.sort()
print("\n".join(map(str,li)))