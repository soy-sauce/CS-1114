class BinaryPositiveInteger:
    def __init__(self,num):
        nbin=[]
        nbin2=''
        while num>0:
            value=int(num%2)
            num=int(num/2)
            nbin.append(value)
        for i in nbin:
            nbin2=str(i)+nbin2
        self.num=nbin2

    def __add__(self, other):
        if len(self.num) < len(self.other):
            self.num = "0" * (len(self.other) - len(self.num)) + self.num

        elif len(self.num > len(self.other)):
            self.other = "0" * (len(self.num) - len(self.other)) + self.other
        self.num = "0" + self.num
        self.other = "0" + self.other

        self.num = self.num[::-1]
        self.other = self.other[::-1]
        newNumber = ""
        carry = 0
        for i in range(len(self.num)):
            if carry == 1:
                # if self.other[i] == "0" and self.num[i] == "0":
                #    carry = 0
                #    newNumber += "1"
                if self.other[i] == "1" and self.num[i] == "1":
                    carry = 1
                    newNumber += "1"
                elif self.other[i] == "0" and self.num[i] == "0":
                    carry = 0
                    newNumber += "1"
                else:
                    carry = 1
                    newNumber += "0"
            else:
                if self.other[i] == "1" and self.num[i] == "1":
                    carry = 1
                    newNumber += "0"
                elif self.other[i] == "0" and self.num[i] == "0":
                    carry = 0
                    newNumber += "0"
                else:
                    carry = 0
                    newNumber += "1"
        if newNumber[0] == "0":
            newNumber = newNumber[1:]
        newNumber = "0b" + newNumber[::-1]
        return newNumber

    def __lt__(self, other):
#        self.other=other
#        num1=0
#        num2=0
#        n=0
#        for i in self.num[::-1]: #converts them to int for comparision
#            if i=='1':
#                num1=num1+(1*(2**n))
#            n+=1
#        n=0
#        for i in self.other[::-1]:
#            if i=='1':
#                num2=num2+(1*(2**n))
#            n+=1

#        if num1<num2:
#            return True
#        else:
#            return False

        self.stripLeadingZeros()
        other.stripLeadingZeros()
        if len(self.s)<len(other.s):
            return True
        elif len(self.s)>len(other.s):
            return False
        else:
            for pt in range(len(self.s)):
                if (self.s[pt])=='1' and (other.s[pt]==0):
                    return False
                elif (self.s[pt]=='0' and other.s[pt]=='1'):
                    return True
            return False

    def is_power_of_2(self): #To check for power of 2, first digit is 1, rest is 0
        if (len(self.num)<=1):
            return False
        else:
            while self.num[0] == 1: #iterates through each position to make sure rest is 0
                for i in range(len(self.num)):
                    if self.num[i+1]!=0:
                        return False
                    return True
            return False

    def __mul__(self,other):
        count=BinaryPositiveInteger(0)
        ret=BinaryPositiveInteger(0)
        while (count<other):
            ret=ret+self
            count=count+BinaryPositiveInteger(1)
        return ret

    def largest_power_of_2(self):
        n=0
        largest_power=2**(len(self.num)-1)
        return largest_power

    def __repr__(self):
        return "0b"+self.num


def main():
    n1=BinaryPositiveInteger(13) #BinaryNumber1
    print(n1.num)
    n2=BinaryPositiveInteger(25) #BinaryNumber2
    print(n2.num)
    print(n1.__lt__(n2.num)) #compares if self is less than other
    print(n1.is_power_of_2()) #is self power of 2
    print(n1.largest_power_of_2()) #largest power of 2
    print(n1.__add__(n2.num)) #Addition
    print("addtion:",n1+n2)
    print(n1.__repr__()) #repr


main()