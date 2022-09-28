# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1：
#
#
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#
#
#  示例 2：
#
#
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 300
#  grid[i][j] 的值为 '0' 或 '1'
#
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 1922 👎 0
import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        g_l = len(grid)
        if g_l == 0:
            return 0

        g_c_l = len(grid[0])

        res = 0
        for l in range(g_l):
            for c_l in range(g_c_l):
                if grid[l][c_l] == "1":
                    res += 1
                    grid[l][c_l] = "0"
                    neighbors = collections.deque([(l, c_l)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]:
                            if 0 <= x < g_l and 0 <= y < g_c_l and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = 0
        return res


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(Solution().numIslands(grid))
grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(Solution().numIslands(grid))
