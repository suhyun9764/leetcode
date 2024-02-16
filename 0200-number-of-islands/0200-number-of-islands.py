from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        m = len(grid)
        n = len(grid[0])

        cnt =0
        def dfs(r,c) :
            if r < 0 or r >= m or c < 0 or c >=n or grid[r][c] != '1':
                return

            grid[r][c] = '0'
            for i in range(4):
                dfs(r+dx[i], c+dy[i])

            return
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue

                dfs(i,j)
                cnt+=1

        return cnt

