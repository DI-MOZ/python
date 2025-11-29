class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last) 
        
        
emp_1=Employee('collo','omosh',30000)
emp_1.fullname()
print(Employee.fullname(emp_1))    
    