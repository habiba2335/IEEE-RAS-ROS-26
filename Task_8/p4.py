t = int(input())
for _ in range(t):
    nums = sorted(list(map(int, input().split())))
    if nums[0] + nums[1] == nums[2]:
        print("YES")
    else:
        print("NO")