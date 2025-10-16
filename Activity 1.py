class A:
    def __init__(self,a):
        self.a = a 

    def __lt__(self,other):
        if(self.a<other.a):
            return 'The first object is less than the second one'
        else:
            return 'The second object is less than the first one'
        
    def __eq__(self,other):
        if(self.a==other.a):
            return 'The values are both equal'
        else:
            return 'The values are both not equal'
        
ob1 = A(4)
ob2 = A(3)
print("The values passed", ob1.a,ob2.a)
print(ob1<ob2)

ob3 = A(6)
ob4 = A(6)
print("The values passed", ob3.a,ob4.a)
print(ob3 == ob4)

