#constructor-> special method which is automatically called when the object is created
class MyClass:
  def m1(self):
    print("this is normal method.....")
  def __init__(self):
    print("this is constructor method.....")
mc = MyClass()
mc.m1()