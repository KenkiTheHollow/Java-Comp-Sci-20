from collections import deque

# ---------------------------
# Read input
# ---------------------------
M = int(input())
N = int(input())
grid = []
for _ in range(M):
    row = list(map(int, input().split()))
    grid.append(row)

# ---------------------------
# BFS to see if we can reach (M-1, N-1)
# ---------------------------
visited = [[False]*N for _ in range(M)]
queue = deque()
queue.append((0,0))
visited[0][0] = True

found = False

while queue:
    r, c = queue.popleft()
    
    if r == M-1 and c == N-1:
        found = True
        break
    
    value = grid[r][c]
    
    # Check all factors (a,b) where a*b = value
    for a in range(1, int(value**0.5)+1):
        if value % a == 0:
            b = value // a
            for new_r, new_c in [(a-1,b-1),(b-1,a-1)]:
                if 0 <= new_r < M and 0 <= new_c < N:
                    if not visited[new_r][new_c]:
                        visited[new_r][new_c] = True
                        queue.append((new_r,new_c))

# ---------------------------
# Output
# ---------------------------
if found:
    print("yes")
else:
    print("no")
