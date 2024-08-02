import sys

# 입력 받기
n = int(sys.stdin.readline())
li = []
endP = 0
count = 0

# 모든 회의의 시작 시간과 종료 시간 입력 받기
for _ in range(n):
    start, end = map(int, sys.stdin.readline().strip().split())
    li.append((start, end))

# 종료 시간을 기준으로 정렬 (끝나는 시간이 같을 경우 시작 시간을 기준으로도 정렬)
li.sort(key=lambda x: (x[1], x[0]))

# 회의 선택
for start, end in li:
    if endP <= start:
        count += 1
        endP = end

print(count)
