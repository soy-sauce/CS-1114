class Calendar:
    date = input("Please enter today's date in mm/dd/yy format: ")
    weekDay = int(input("Please enter the day of the week today (1 for Monday and 7 for Sunday): "))
    MDY = date.split("/")
    daysOfweekList = ['',"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    monTosun = daysOfweekList[weekDay]
    print(monTosun)

    def __init__(self):
        self.month = int(self.MDY[0])
        self.day = int(self.MDY[1])
        self.year = int(self.MDY[2])
        self.daysOfweek = self.monTosun
        self.to_do_list = ToDoList()

    def __str__(self):
        todoList = ""
        doneList = ""
        for thing in self.to_do_list.todolist:
            todoList += "\n" + thing
        for thing in self.to_do_list.donelist:
            doneList += "\n" + thing
        front = "Today's date is: " + self.daysOfweek + " " + str(self.month) + "/" + str(self.day) + "/" + str(self.year)
        accomplishment = "\n" + "Today's Accomplishment" + '\n' + '========================='
        left = "\n" + "Things Left to Do" + '\n' + '========================='
        return front + accomplishment + doneList +"\n"+ left + todoList

    def __repr__(self):
        return str(self)

    def start_new_day(self):
        todoList = ""
        doneList = ""
        daysOfweek = ['', "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        daysInMonth = ['','31','28','31','30','31','30','31','31','30','31','30','31']
        #print(daysOfweek)
        self.weekDay += 1
        self.daysOfweek = self.monTosun
        self.to_do_list = ToDoList()

        if (self.day) == int(daysInMonth[self.month]):
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1

        front = "Today's date is: " + self.daysOfweek + " " + str(self.month) + "/" + str(self.day) + "/" + str(self.year)
        accomplishment = "\n" + "Today's Accomplishment" + '\n' + '========================='
        left = "\n" + "Things Left to Do" + '\n' + '========================='
        return front + accomplishment + doneList + "\n" + left +todoList



class ToDoList:
    def __init__(self):
        self.todolist = []
        self.donelist = []
    def __str__(self):
        return
    def __repr__(self):
        return str(self)
    def create_to_do_list_item(self):
        todo = input("Enter the task: ")
        self.todolist.append(todo)
        print(self.todolist)
    def check_to_do_list(self):
        for i in range(len(self.todolist)):
            task = self.todolist[i]
            yesNo = input("Did you "+task+"? (y/n): ")
            if yesNo.lower() == "y":
                print(task)
                self.donelist.append(task)
        revList = self.todolist[::-1]
        print(revList)
        for thing in revList:
            if thing in self.donelist:
                self.todolist.pop(self.todolist.index(thing))

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