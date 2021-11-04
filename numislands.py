# Given an m x n 2D binary grid grid
# which represents a map of '1' s(land) and '0' s(water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.You
# may assume all four edges of the grid are all surrounded by water.
#
# Example 1:

# Input: grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
# Output: 3
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS approach
        #marking visited as 2
        #increment ans every time DFS
        if not grid:
            return 0
        m = len(grid) #rows
        n = len(grid[0]) #cols
        ans = 0

        def dfs(i,j):
            #mark as visited
            grid[i][j] = '2'
            for di, dj in (1,0),(0,1),(-1,0),(0,-1):
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1':
                    dfs(ii,jj)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans+=1
        return ans

    # Input: grid = [
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"]
    # ]
    # Output: 3
    def main(self):
        grid = [
         ["1", "1", "0", "0", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "1", "0", "0"],
         ["0", "0", "0", "1", "1"]
        ]

        ans = self.numIslands(grid)
        print(ans)

obj = Solution()
obj.main()