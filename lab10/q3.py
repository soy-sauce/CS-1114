def sum_column(filename):
    sum=0
    f=open(filename,'r');
    lines=f.readlines()
    for i in range(len(lines)):
        sum=sum+(int(lines[i]))
    print(sum);
    f.close()

sum_column('lab10_q2.txt')