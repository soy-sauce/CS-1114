import os
class Employee:
    def __init__(self,idnum=0,name="",payrate=0):
        self.idnum=idnum
        self.name=name
        self.payrate=payrate
        self.hoursworked=0

    def addHours(self,hours):
        self.hoursworked+=hours

    def resetHours(self):
        self.hoursworked=0

    def getPay(self):
        return self.payrate*self.hoursworked

    def payEmployee(self):
        total=self.getPay()
        self.resetHours()
        return total

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.idnum+"/"+self.name

def open_file(prompt):
    filename=input(prompt)
    while (not os.path.exists(filename)):
        print("Bad filename")
        filename=input(prompt)
    return open(filename,'r')

def main():
    empFile=open_file("Please enter the Employee filename: ")
    payFile=open_file("Please enter Payroll filename")
    emps=[]
    for line in empFile:
        parts=line.split();
        idnum=int(parts[0])
        payrate=float(parts[0])
        name=" ".join(parts[2:]) #get name as sum of parts
        emps[idnum]=Employee(idnum,name,payrate)
    for line in payFile:
        parts=line.split():
        idnum=int(parts[0])
        hours=float(parts[1])
        if idnum in emps:
            emps[idnum].addHours(hours)
        else:
            print(idnum,"not found in employee file!")

    for emp in emps:
        print(emp[emps].name,"(",emp,") gets paid $",emps[emp].getPay)


main()