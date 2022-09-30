import sys
sys.stdin = open('5249.txt')

# 그래프에서 사이클을 제거 하고 모든 노드를 포함 하는 트리를 구성할 때,
# 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리
# 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오

def prim1(r, V):
    MST = [0]*(V+1)  # MST 포함여부 체크
    key = [10000]*(V+1)
    key[r] = 0
    for _ in range(V): # 총 V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중(MST[u]=0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i]<minV:
                u = i
                minV = key[i]
        MST[u] = 1          # 정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v]>0:
                key[v] = min(key[v], adjM[u][v])        # u를 통해 MST에 포함되는 비용과 기존 비용을 비교, 갱신
    return sum(key)         # MST 가중치의 합




T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # V = 마지막 노드번호, E 간선의 갯수

    # adjM or adjL
    adjM = [[0]*(V+1) for _ in range(V+1)]  # 인접 행렬로 만들기

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = w
        adjM[n2][n1] = w
    # print(adjM)
    rst = prim1(0, V)
    print(f'#{tc} {rst}')