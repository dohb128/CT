import sys

n = int(sys.stdin.readline())
li = [0]*10001

for _ in range(n):
    li[int(sys.stdin.readline())] += 1
    # 5 입력 -> 0,0,0,0,0,1 이런식으로 인덱스 5의 자리에 값 추가해서 갯수 판별

for i in range(10001):
    if li[i] != 0:  # 0이 아닌 입력된 수만 출력
        for j in range(li[i]): # 해당 인덱스에 저장된 값만큼의 수를 출력
            print(i)