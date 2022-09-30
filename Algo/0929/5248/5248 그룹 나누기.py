import sys
sys.stdin = open('5248.txt')


# 수업에 같은 조에 참여하고 싶은 사람끼리 짝을 만듬
# 한 조의 인원에 제한을 두지 않았기 때문에, 한 사람이 여러 장의 종이를 제출하거나,
# 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.
# 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다
# 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성

def find_set(x): # x를 포함하는 집합을 찾는 연산
    if x == P[x]:
        return x
    else:
        return find_set(P[x])


def union(x, y):  # x와 y를 포함하는 두 집합을 통합하는 연산
    P[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    P = [i for i in range(N+1)]  # 출석번호 인덱스를 가진 parent 리스트 만들어주기
    for j in range(0, len(L), 2):  # 두개씩 잘라서 한 쌍마다 union 연산해줌
        union(L[j], L[j+1])

    result = set()

    for k in range(1, N+1):
        result.add(find_set(k))
    rst = len(result)
    print(f'#{tc} {rst}')


