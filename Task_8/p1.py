
q = int(input())

for _ in range(q):
     n = int(input())
     t , s = input().split()
    

     if sorted(t) == sorted(s):
      print("YES")
     else:  
      print("NO")