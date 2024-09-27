class employee:
    no_of_employee=0
    raise_amnt=1.05
    def __init__(self,name,age,pay):
        self.name=name
        self.age=age
        self.pay=pay
        employee.no_of_employee+=1    #employee.no_pf employee because the total no of emloyee needs to be changes
        self.no_of_employee+=2   #returen 0
        #self.raise_amnt*=0
        #employee.raise_amnt *= 0

    def fullname(self):
        return '{} {}'.format(self.name,self.age)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amnt)
e1=employee('raj',21,5000)
e2=employee('reena',20,500000)
#print(employee.fullname(e1))
# print(e1.pay)
# e1.apply_raise()
# print(e1.pay)
# print(e1.__dict__)
print(employee.no_of_employee)
print(employee.raise_amnt )