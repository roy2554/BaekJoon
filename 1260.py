import sys
node, edge, start = map(int, sys.stdin.readline().split())

inf = 987654321

nlist = [[inf for i in range(node+1)] for x in range(node+1)]

visited = [False]*(node+1)

for i in range(edge):
    x, y = map(int, sys.stdin.readline().split())
    nlist[x][y] = y
    nlist[y][x] = x

dfsOut = ""
bfsOut = ""

# dfs
def dfs(nlist, startPos, visited):
    visited[startPos] = True
    print(startPos, end=" ")
    for i in range(1,len(nlist[startPos])):
        if not nlist[startPos][i] == inf:
            if not visited[i]:
                dfs(nlist, i, visited)
                

dfs(nlist, start, visited)

print("") # 줄바꿈

# bfs
visited = [False]*(node+1)

from collections import deque
q = deque()

q.append(start)
visited[start] = True


while q:
    startPos = q.popleft()
    print(startPos, end=" ")
    for i in range(1,len(nlist[startPos])):
        if not nlist[startPos][i] == inf:
            if not visited[i]:
                q.append(i)
                visited[i] = True
