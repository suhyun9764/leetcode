class Solution:
    def numIslands(self, grid):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        n = len(grid)
        m = len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    continue

                cnt +=1
                que = deque()
                que.append((i,j))
                while que:
                    y,x = que.popleft()
                    for k in range(4):
                        ny = y+dy[k]
                        nx = x+dx[k]

                        if ny <0  or ny >=n or nx <0 or nx >= m or grid[ny][nx] == '0':
                            continue

                        grid[ny][nx] = '0'
                        que.append((ny,nx))

        return cnt