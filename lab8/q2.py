def internal_str(a, b):
    for i in range(len(a)):
        x=b.find(a[i]);
        if x==-1:
            return False;

        else:
            b=b[:x]+b[x+1:];
    return True

print(internal_str("abcdefg","gfedcba"))