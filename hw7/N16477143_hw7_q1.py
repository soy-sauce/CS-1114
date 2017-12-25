import math
lst=[-19, -3, -20, -1, 0, -25]

def max_abs_val(lst):
    max=lst[0];
    for i in range(len(lst)-1):
        if math.fabs(lst[i+1])>math.fabs(lst[i]):
            max=math.fabs(lst[i+1]);
    print(max)
    return max;


max_abs_val(lst);

