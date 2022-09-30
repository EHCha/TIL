import sys
sys.stdin = open('1267.txt')


T = int(input())

calls = list(map(int, input(). split()))

Y = 0  # 30초 마다 10원씩 30에서 59초는 20원
M = 0  # 60초 마다 15원씩 60에서 119초는 30원

for i in calls:
    Y += i//30 * 10 + 10  # 몫이 0 즉 30초 보다 통화를 적게 했으면 10원만 더해주기
    M += i//60 * 15 + 15  # 같은 맥락으로 ㅇㅇ

if Y == M:
    print('Y M', Y)
elif Y > M:
    print('M', M)
elif Y < M:
    print('Y', Y)

