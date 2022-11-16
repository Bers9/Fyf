s = '24+1'
i = 0
 
arg1 = []
while True:
    if s[i] in '1234567890':
        arg1.append(s[i])
        i += 1
    else:
        break
arg1 = int(''.join(arg1))
 
if s[i] not in '+-/*':
    raise ValueError
op = s[i]
i += 1
 
arg2 = []
while True:
    try:
        if s[i] in '1234567890':
            arg2.append(s[i])
            i += 1
    except IndexError:
        break
arg2 = int(''.join(arg2))
 
print(arg1, op, arg2)
