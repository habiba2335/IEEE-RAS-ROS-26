n = int(input())
max_capacity = 0
current_passengers = 0
for _ in range(n):
    a, b = map(int, input().split())
    current_passengers -= a
    current_passengers += b
    if current_passengers > max_capacity:
        max_capacity = current_passengers
print(max_capacity)