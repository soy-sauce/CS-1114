#q3a return first word
def first_word(s):
    firstSpace=s.find(" ");
    word=s[0:firstSpace];
    return word;

#q3b returns minus first word
def minus_first(s):
    firstSpace=s.find(" ");
    line = s[firstSpace+1:]
    return line

#q3c reverses words
def reverse(s):
    line=s.count(" ")+1
    count=1;
    reverseStr=""
    while count<line:
        reverseStr=first_word(s)+str(" ")+reverseStr;
        s=minus_first(s);
        count+=1
    new=s+" "+reverseStr;
    return new

#q3d main()
s=input("Enter a sentence to reverse: ")
print(reverse(s));