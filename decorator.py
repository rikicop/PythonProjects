class Employee:
    #The __init__() function is called automatically
    #every time the class is being used
    #to create a new object.
    
    def __init__(self, first, last):
        self.fist = first
        self.last = last
    #decorator allows us to define properties easily without
    #calling the property() function
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('Borraste el Nombre!!')
        self.first = None
        self.last = None
    
        
emp_1 = Employee('Ricardo','Otalora')

emp_1.fullname = 'Fernando Luna'

print(emp_1.first)
print(emp_1.email)
del emp_1.fullname
print(emp_1.fullname)


