def internal_str(a, b):
    for char in a:
        if b.find(char):
            return False;

        else:
            b=b[:i]+b[i+1:];
    return True

print(internal_str('abcdefg', "gfedcba"))