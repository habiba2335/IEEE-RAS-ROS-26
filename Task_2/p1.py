numbers = []

while True:
    num = int(input("Enter numbers:"))
    
    if num == -1: 
        break
        
    numbers.append(num)

if numbers:
    print(f"max={max(numbers)}")
    print(f"min={min(numbers)}")