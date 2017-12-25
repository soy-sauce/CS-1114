class Calendar:
    date=input("Please enter a date in mm/dd/yy format: ")
    dayOfWeek = int(input("Please enter the day of the week(1 for Monday and 7 for Sunday) :" ))
    MDY=date.split("/")
    daysOfWeekList=['',"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
    monToSun=daysOfWeekList[dayOfWeek]

    def __init__(self):
        self.day=int(self.MDY[0])
        self.month=int(self.MDY[1])
        self.year=int(self.MDY[2])
        self.daysOfWeek=self.monToSun
        self.to_do_list=ToDoList()

    def __repr__(self):
        todoList=""
        doneList=""
        for thing in self.to_do_list.todolist:
            todoList += "\n" + thing
        for thing in self.to_do_list.donelist:
            doneList += "\n" + thing
        top = "Today's date is: " + self.daysOfWeek + " " + str(self.month) + "/" + str(self.day) + "/" + str(self.year)
        done = "\n" + "Today's Accomplishment" + '\n' + '========================='
        left = "\n" + "Things Left to Do" + '\n' + '========================='
        return top + done + doneList +"\n"+ left + todoList

    def start_new_day(self):
        toDoList=""
        doneList=""
        days=['',"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
        monthDays=["","31","28","31","30","31","30","31","31","30","31","30","31"]
        self.dayOfWeek+=1
        self.dayOfWeek=self.monToSun

        if (self.day)==int(monthDays[self.month]):
            self.day=1
            if self.month==12:
                self.month=1
                self.year+=1
            else:
                self.month+=1
        else:
            self.day+=1

        top="Today's date is: "+self.daysOfWeek+" "+str(self.month)+"/"+str(self.day)+"/"+str(self.month)+"/"+str(self.year)
        done="\n"+"Today's Accomplishment"+"\n"+"========================="
        left="\n"+"Things Left To Do"+"\n"+"=========================="
        return top + done +doneList+"\n"+left+toDoList



class ToDoList:
    def __init__(self):
        self.todolist=[]
        self.donelist=[]
    def create_to_do_list_item(self):
        todo=input("Enter the task: ")
        self.todolist.append(todo)
        print(self.todolist)

    def check_to_do_list(self):
        for i in range(len(self.todolist)):
            task=self.todolist[i]
            ans=input("Did you "+task+"? (y/n)")
            if ans.lower()=='y':
                print(task)
                self.donelist.append(task)
        newList=self.todolist[::-1]
        for i in newList:
            if i in self.donelist:
                self.todolist.pop(self.todolist.index(i))


    def __repr__(self):
        return

def main():
    calendar = Calendar()
    while True:

        print("\nMain Menu:")
        print("1. Create New Calendar")
        print("2. Add To-Do List Item")
        print("3. Check Off To-Do List")
        print("4. Show Today's Calendar")
        print("5. Start The Next Day\n")

        answer = input("What would you like to do? ")
        if answer == '1':
            calendar = Calendar()
        elif answer == '2':
            calendar.to_do_list.create_to_do_list_item()
        elif answer == '3':
            calendar.to_do_list.check_to_do_list()
        elif answer == '4':
            print(repr(calendar))
        elif answer == '5':
            calendar.start_new_day()

main()