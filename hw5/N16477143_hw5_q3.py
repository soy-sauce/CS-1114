s=input("Enter a mathematical expression: ");

space1=s.index(' ');
space2=s.index(' ',space1+1, len(s));
operand=int(s[:space1]);
op=s[space1+1:space2];
operand2=int(s[(space2)+1:]);

if op=='+':
    print(s," = ",(operand+operand2))
if op=='-':
    print(s," = ",(operand-operand2))
if op=='*':
    print(s," = ",(operand*operand2))
if op=='/':
    print(s," = ",(operand/operand2))



