class Student:
    #__init__ ---> it is similar to constructorin c++ or java.
    #self ---> it represents the instance of a class and it holds some attributed or binds the attributes with the given arguments

    def __init__(self, name, id):
        self.student_name = name
        self.id_no = id

    def display(self):
        print(self.id_no,self.student_name)
s = Student('Ravi',202)
s.display()

