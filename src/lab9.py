def count_paths(grid, H, W):
    from collections import defaultdict

    dp = [[0]*W for _ in range(H)]

    for r in range(H):
        dp[r][0] = 1

    letter_positions = defaultdict(list)
    for c in range(W):
        for r in range(H):
            letter_positions[grid[r][c]].append((r, c))

    for c in range(W - 1):

        transferred = defaultdict(list)
        for r in range(H):
            if dp[r][c] == 0:
                continue
            dp[r][c+1] += dp[r][c]

            current_letter = grid[r][c]
            for rr, cc in letter_positions[current_letter]:
                if cc > c:
                    dp[rr][cc] += dp[r][c]
            letter_positions[current_letter] = [(rr, cc) for (rr, cc) in letter_positions[current_letter] if cc <= c]

    return dp[0][W-1] + dp[H-1][W-1]

with open(r"C:\IT\lab9.2semestr\ijones.in") as f:
    W, H = map(int, f.readline().split())
    grid = [list(f.readline().strip()) for _ in range(H)]

result = count_paths(grid, H, W)

with open(r"C:\IT\lab9.2semestr\ijones.out", "w") as f:
    f.write(str(result) + "\n")
