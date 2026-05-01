code = input()
res = ""
i = 0
while i < len(code):
    if code[i] == '.':
        res += '0'
        i += 1
    elif code[i:i+2] == '-.':
        res += '1'
        i += 2
    else:
        res += '2'
        i += 2
print(res)