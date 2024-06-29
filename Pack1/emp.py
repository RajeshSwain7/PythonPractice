class Employee:
    def __init__(self,eid,ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal
    def Dispemp(self):
        print("empid:{} empname:{} empsal:{}". format(self.eid,self.ename,self.sal))


