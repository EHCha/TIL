from collections import deque


def bfs(a):
    queue = deque()
    queue.append(a)
    visited[a] = 1
    d = 0
    while queue:
        # 각 레벨의 수를 카운트 해주고, 그 카운트가 넘어갈 때마다
        # 연산의 카운트를 1씩 늘려준다.
        size = len(queue)
        for _ in range(size):
            a = queue.popleft()

            if a == m:
                return d

            # 의도치 않은 하드코딩..
            if 0 < a + 1 < 1000001 and not visited[a + 1]:
                queue.append(a + 1)
                visited[a + 1] = 1
            if 0 < a - 1 < 1000001 and not visited[a - 1]:
                queue.append(a - 1)
                visited[a - 1] = 1
            if 0 < a * 2 < 1000001 and not visited[a * 2]:
                queue.append(a * 2)
                visited[a * 2] = 1
            if 0 < a - 10 < 1000001 and not visited[a - 10]:
                queue.append(a - 10)
                visited[a - 10] = 1
        d += 1


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    # null null하게 200만까지 만들어주었다.
    visited = [0] * 2000010
    print(f"#{_ + 1} {bfs(n)}")