from dic import *
import unittest
import sys

class MyOutput(object):
            def __init__(self):
                self.data = []
 
            def write(self, s):
                self.data.append(s)
 
            def __str__(self):
                return "".join(self.data)
stdout_org = sys.stdout
my_stdout = MyOutput()

class dicTest(unittest.TestCase):
    def setUp(self):
        self.fruits = OrganizedDico(raisin=50,poires=10,orange=20, pommes=30)
        
    def test_print(self):
        try:
            sys.stdout = my_stdout
            print (self.fruits)
        finally:
            sys.stdout = stdout_org
 
        output ="orange = 20 \npoires = 10 \npommes = 30 \nraisin = 50 \n\n"
        self.assertEquals( str(my_stdout), output)

unittest.main()