input=input("End an odd length string: ");

length=len(input);
pos=int((length/2))
pos2=pos-1;

print("Middle Charcter: ",input[pos]);
print("First half: ",input[:pos]);
print("Second half: ",input[pos2:]);