n = int(input(" Enter a positive number:"))

if n <= 0:
    print("Invalid number")
else:
    total_sum = 0


    for x in range(1, n + 1):
        if x % 2 == 0:  
            total_sum += x
        

    print(f"the sum = {total_sum}")