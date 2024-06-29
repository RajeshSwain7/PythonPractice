import sys
sys.path.append("D:/Python/PythonPractice/pythonPractice/Pack1")

from emp import Employee

e=Employee(101,"Rajesh", 1000000)
e.Dispemp()


sys.path.append("D:/Python/PythonPractice/pythonPractice/Pack2")

from stu import Student
s=Student(111,"Rajesh", "A")
s.DispStu()