import random

n=int(input("Enter number n: "))
n2=n
n3=n
line=""

for i in range(n):
    for j in range(n-i):
        line=line+str((random.randint(0,9)))
    print(line)
    line=""




for i in range(n+1):
    for j in range(i):
        line = line + str((random.randint(0, 9)))
    print(line)
    line = ""