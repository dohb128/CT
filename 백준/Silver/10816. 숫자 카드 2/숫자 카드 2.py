import sys
import statistics

n = int(sys.stdin.readline())
nli = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline())
mli = list(map(int, sys.stdin.readline().strip().split()))

cnt_dict = {}
for i in nli:
    if i in cnt_dict:
        cnt_dict[i] += 1
    else:
        cnt_dict[i] = 1

answer = [cnt_dict.get(num, 0) for num in mli]

for i in answer:
    print(i, end=" ")