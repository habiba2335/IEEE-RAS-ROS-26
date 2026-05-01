n = int(input())
total_solved = 0
for _ in range(n):
    if sum(map(int, input().split())) >= 2:
        total_solved += 1
print(total_solved)