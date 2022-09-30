import sys
from collections import deque
sys.stdin = open('5247.txt')


def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1  # 초기값 방문 표시
    d = 0  # 몇번 연산을 했는지 저장 해줄 변수 d
    while q:
        size = len(q)  # 각 레벨당 수 카운트 하고 돌때마다 연산의 카운트를 1씩 올려줌.
        for _ in range(size):
            s = q.popleft()

            if s == M:  # 연산을 시작한 숫자 s 가 M과 같아지면, 연산 횟수 d를 반환한다.
                return d

            if 0 < s + 1 < 1000001 and not visited[s+1]:
                q.append(s+1)
                visited[s+1] = 1
            if 0 < s - 1 < 1000001 and not visited[s-1]:
                q.append(s-1)
                visited[s-1] = 1
            if 0 < s * 2 < 1000001 and not visited[s*2]:
                q.append(s*2)
                visited[s*2] = 1
            if 0 < s - 10 < 1000001 and not visited[s-10]:
                q.append(s-10)
                visited[s-10] = 1
        d += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 2000001
    rst = bfs(N)
    print(f'#{tc} {rst}')