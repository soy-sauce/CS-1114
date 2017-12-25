import random;

def write_random_numbers(filename,n):
    f = open(filename, 'w')
    while n>0:
        f.write(str(random.randint(0,100))+'\n')
        n-=1;
    f.close()

write_random_numbers('lab10_q2.txt',5)
