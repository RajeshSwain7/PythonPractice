class Student:
    def __init__(self,sid,sname, sgrade):
        self.sid = sid
        self.sname = sname
        self.sgrade = sgrade
    def DispStu(self):
        print("stuid:{} stuname:{} stugrade:{}". format(self.sid,self.sname,self.sgrade))


