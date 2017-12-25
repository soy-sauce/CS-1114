class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.hobbies=[]

    def addHobby(self,newHobby):
        self.hobbies.append(newHobby)

    def deleteHobby(self,oldHobby):
        self.hobbies.remove(oldHobby)

    def birthday(self):
        print("Happy Birthday, ", self.name, "!")
        self.age = str(int(self.age) + 1)

    def __repr__(self):
        myString = ("Name: " + str(self.name) + '\n' + "Age: " + str(self.age) + '\n' + "Hobbies: \n")
        for item in self.hobbies:
            myString += item+"\n"

        return myString

    def print_list(self):
        print(self.hobbies)

def main():
    user_list=[]
    keepgoing=True
    while keepgoing:
        user_input=input("Select one of the following options:\n" +
                    "=========================================\n" +
                    "1. Create a new Person\n" +
                    "2. Add to an existing person's hobbies\n" +
                    "3. Delete an existing person's hobby\n" +
                    "4. Someone has a birthday\n" +
                    "5. See a list of people\n" +
                    "6. Exit\n")

        if user_input=="1":
            name=input("Please enter the name: ")
            age=input("Please enter the age: ")
            user=Person(name, age)
            user_list.append(user)

        elif user_input=="2":
            name=input("Who is receiving a new hobby? ")
            newHobby=input("What is the new hobby? ")
            for person_object in user_list:
                if person_object.name==name:
                    person_object.addHobby(newHobby)

        elif user_input=="3":
            name=input("Who is losing a hobby? ")
            oldHobby=input("What hobby are you deleting? ")
            for person in user_list:
                if person.name==name:
                    person.deleteHobby(oldHobby)

        elif user_input=="4":
            name=input("Who is having a birthday? ")
            for person_object in user_list:
                if person_object.name == name:
                    person_object.birthday()

        elif user_input=="5":
            for i in range(len(user_list)):
                print(repr(user_list[i]))

        elif user_input=="6":
            print("Goodbye!")
            keepgoing=False

main()