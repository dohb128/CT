import bisect
import sys

n = int(sys.stdin.readline())
input = sys.stdin.readline()

nli = list(map(int, input.split()))
nli.sort()

m = int(sys.stdin.readline())
input = sys.stdin.readline()

mli = list(map(int, input.split()))

for i in mli:
    index = bisect.bisect_left(nli, i)
    if index < len(nli) and nli[index] == i:
        print(1)
    else:
        print(0)