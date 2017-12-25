class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies = []
    def addHobby(self, newhobby):
        self.hobbies.append(newhobby)
    def deleteHobby(self, oldHobby):
        self.hobbies.remove(oldHobby)
    def birthday(self):
        print("Happy birthday", self.name)
        self.age += 1
    def __repr__(self):
        return "Name" + self.name + '\n' + "Age" + self.age + '\n' + "Hobbies" + self.hobbies + '\n'

def main():
    user_list = []
    exit = True
    while exit:
        user_input =input("Select one of the following options:\n" +
                    "=========================================\n" +
                    "1. Create a new Person\n" +
                    "2. Add to an existing person's hobbies\n" +
                    "3. Delete an existing person's hobby\n" +
                    "4. Someone has a birthday\n" +
                    "5. See a list of people\n" +
                    "6. Exit\n")
        if user_input == "1":
            name = input("Please enter the name:")
            age = input("Please enter the age:")
            user = Person(name, age)
            user_list.append(user)
        elif user_input == "2":
            name = input("Who is receiving a new hobby?")
            new_hobby = input("What is this person's new hobby?")
            for person_object in user_list:
                if person_object.name == name:
                    person_object.addHobby(new_hobby)
        elif user_input == "3":
            name = input("Who is losing a hobby?")
            delete_hobby = input("What hobby are you deleting?")
            for person_object in user_list:
                if person_object.name == name:
                    person_object.deleteHobby(delete_hobby)
        elif user_input == "4":
            Person.birthday()
        elif user_input == "5":
            #print(repr(Person)
            for person_object in user_list:
                print(person_object)
        elif user_input == "6":
            print("Goodbye!")
            exit = False

main()