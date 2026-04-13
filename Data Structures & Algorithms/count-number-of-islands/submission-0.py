class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # island is "1", and must not be visited
        # bfs starting with the first top left "1" or island, and sweep across the grid

        # deque() for bfs
        # visited set()
        # num_islands = 0

        # no need to check for empty grid since length is >= 1
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        num_islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q: # go up right down left
                row, col = q.popleft()
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    # check if its in range and valid
                    if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        # loop through grid

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    # loop through all adjacent 1's to keep track of curr island
                    bfs(r, c)
                    num_islands += 1
        
        return num_islands
