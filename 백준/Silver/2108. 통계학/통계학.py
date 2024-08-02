import sys
import statistics

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    a = int(sys.stdin.readline())
    li.append(a)
li.sort()

avg = round(sum(li)/len(li))
print(avg)

if n%2==0:
    median = (li[n//2] + li[n//2-1])/2
else:
    median = li[n//2]
print(median)

mode = statistics.multimode(li)
mode.sort()
if len(mode)>1:
    print(mode[1])
else:
    print(mode[0])

rang = max(li) - min(li)
print(rang)
