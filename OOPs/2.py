class Student:
    college_name = 'IIt Bombay' # class attribute - comman for all objects

    def printonlyname(self,name): # function
            print('Student name: '+ name)


student2 = Student() # object
student2.printonlyname('Rahul')
