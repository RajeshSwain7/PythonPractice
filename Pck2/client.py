import sys
sys.path.append("D:/Python/PythonPractice/pythonPractice/Pck1")

#approch 1
import module1
import module2

module1.display()
module2.show()

#approch-2 which out module name

from module1 import *
from module2 import *

display()
show()




