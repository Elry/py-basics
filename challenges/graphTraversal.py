def num_islands(grid):
    if not grid: return 0
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def sink(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        # mark as visited
        grid[r][c] = '0'

        # 3. Visit all neighbors
        sink(r + 1, c) # Down
        sink(r - 1, c) # Up
        sink(r, c + 1) # Right
        sink(r, c - 1) # Left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                sink(r, c)

num_islands()
