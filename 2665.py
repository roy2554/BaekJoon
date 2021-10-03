'''
백준 2665번 문제
출발지점에서 도착지점까지 가는 최소비용을 구하는것이므로 다익스트라 알고리즘을 사용한다.
'''
import heapq

n = int(input())
inf = float('inf')
board = [[inf for x in range(n+1)] for i in range(n+1)]
cost = [[inf for x in range(n+1)] for i in range(n+1)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = []

for i in range(n):
    inp = input()
    for x in range(len(inp)):
        board[i+1][x+1] = int(inp[x])

cost[1][1] = 0

heapq.heappush(q,[1,1])
while q:
    x, y = map(int, heapq.heappop(q))
    for i in range(4):
        if x+dx[i] > 0 and x+dx[i] <= n and y+dy[i] > 0 and y+dy[i] <= n:  
            if board[x+dx[i]][y+dy[i]] == 1:
                movecost = 0
                                   
            elif board[x+dx[i]][y+dy[i]] == 0:
                movecost = 1
            # update
            if cost[x+dx[i]][y+dy[i]] > cost[x][y] + movecost:
                cost[x+dx[i]][y+dy[i]] = cost[x][y] + movecost
                heapq.heappush(q,[x+dx[i],y+dy[i]])
            

print(cost[n][n])
