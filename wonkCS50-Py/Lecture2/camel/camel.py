def split_on_uppercase(s):
    string_length = len(s)
    
    output = []
    for i in range(string_length):
        if str(s[i]).isupper():
            if str(s[i-1]).isupper(): output.append(s[i])
            else: output.append(f'_{str(s[i]).lower()}')
        else: output.append(s[i])
    return (''.join(output))

print(split_on_uppercase(str(input('camelCase: '))))

