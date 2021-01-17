class Student:
    college_name = 'IIt Bombay' # class attribute - comman for all objects
    
    def __init__(self,name,age,dob): # initializer 
        print('Constructor')
        self.name = name
        self.age  = age
        self.dob = dob


student1 = Student('Raj',20,'09/05/1994') # object
print(student1.name,student1.age,student1.dob,student1.college_name) # printing
