n=int(input("Enter an integer: "));
ast="*";
n2=n
n3=1
n4=n
ast2="*";
spc=0
spc2=0

for i in range (0,n2):
    for j in range (0,i):
        if n2>0:
            ast=((n2*2)*"*")
            ast = ast[:-1]
            n2-=1
            if spc<n:
                ast=(" "*spc)+ast+(" "*spc);
                spc+=1;
            print(ast);

spc-=1;
for i in range (0,n4):
    for j in range (0,i):
        if n3<(n+1):
            ast2=((n3*2)*"*")
            ast2 = ast2[:-1]
            n3+=1;
            if spc>0:
                ast2=(" "*spc)+ast2+(" "*spc);
                spc-=1;
            print(ast2);
