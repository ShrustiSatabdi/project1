class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(r, c):

            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                grid[r][c] == "0" or
                visited[r][c]
            ):
                return

            visited[r][c] = True

            dfs(r - 1, c)   # Up
            dfs(r + 1, c)   # Down
            dfs(r, c - 1)   # Left
            dfs(r, c + 1)   # Right

        islands = 0

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == "1" and not visited[r][c]:
                    islands += 1
                    dfs(r, c)

        return islands
        