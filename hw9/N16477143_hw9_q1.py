class Student:

    def __init__(self,name,NYU_id,net_id):
        self.name=name
        self.NYU_id=NYU_id
        self.net_id=net_id
        self.grade_list=[]

    def add_grade(self, catalog_name, grade):
        grade=(catalog_name,int(grade))
        self.grade_list.append(grade)
        return grade

    def average(self):
        self.average=0
        for i in range(len(self.grade_list)):
            self.average=self.average+(self.grade_list[i][1])
        self.average=(self.average/(len(self.grade_list)))
        return self.average

    def get_email(self):
        return self.netID+"@nyu.edu"

    def __repr__(self):
        return "Name: "+self.name+'\n'+"NYU_id: "+self.NYU_id+'\n'+"net_id: "+self.net_id+"\n"+"grades_list: "+str(self.grade_list)


def load_students(students_data_filename):
    file = open(students_data_filename, "r")
    students_list=[]
    header=file.readline()
    header=header[0:-1]
    header=header.splitlines()
    for line in file:
        line=line[0:-1]
        parts=line.split(',')
        aStudent = Student(parts[1], parts[0], parts[2])
        i=3
        grades=parts[3:10]
        for grade in parts[3:10]:
            if grade!="":
                aStudent.add_grade(header[i],grade) #I cant get this to work no matter what, i keep getting errors
                i+=1
            else:
                i+=1
        students_list.append(aStudent)
    file.close()
    return students_list

def generate_performance_report(students_lst, out_filename):
    file=open(out_filename,"w")
    file.write("NYU ID, Average")
    average=0
    sum=0
    for object in students_lst:
        average=object.average()
        file.write(str(object.NYU_id)+str(average))

    file.close()


def generate_course_mailing_list(students_lst,catalog_name,out_filename):
    file=open(out_filename,"w")
    for object in students_lst:
        if object.grade_lst!="":
            file.write(object.net_id)

def main():
    print(load_students('grades.csv'))
    file=open('grades.csv','r')
    students_lst=load_students('grades.csv')
    generate_performance_report(students_lst,'performance.csv')
main()
