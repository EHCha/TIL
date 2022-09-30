import sys
sys.stdin = open('2806.txt')

# N * N의 체스보드에 N개의 퀸이 서로 공격하지 못하게 배치
# 퀸은 한줄에 하나씩 만 배치 할수 있다
# N개의 줄에 배치할때 퀸을 안전하게 모든 줄에 배치 완료한 후에 경우의수를 하나 올려줄수 있다


def DFS(depth): # 재귀 호출 DFS
    global cnt
    if depth == N: # 줄은 재귀의 깊이로 마지막 줄까지 놓았을때 값을 리턴한다
        cnt += 1
        return

    for i in range(N):
        if visited[i] == 0:
            grid[depth] = i
            flag = True
            for j in range(depth):
                if abs(grid[depth]-grid[j]) == abs(depth-j):
                    flag = False
                    break
            if flag:
                visited[i] = 1  # 방문 한 숫자는 True로 표시해주고
                DFS(depth+1)  # depth를 1 증가시킨 다음 재귀함수 실행, 함수를 다시 실행하면 숫자를 grid 배열에 저장
                visited[i] = 0  # 함수를 나오게 되면 표시를 다시 False로 바꿔 다음탐색



T = int(input())

for tc in range(1, T+1):
    N = int(input())

    grid = [0] * N
    visited = [0] * N
    cnt = 0
    DFS(0)
    print(f'#{tc} {cnt}')
