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
stdout_origin = sys.stdout
my_stdout = MyOutput()

class dicTest(unittest.TestCase):
    def setUp(self):
        self.fruits = OrganizedDico(raisin=50,poires=10,orange=20, pommes=30)
        
    def test_print(self):
        output="orange = 20 \npoires = 10 \npommes = 30 \nraisin = 50 \n\n"
        try:
            sys.stdout = my_stdout
            print (self.fruits)
            self.assertEquals( str(my_stdout), output)
        finally:
            sys.stdout = stdout_origin
    
    def test_reverse(self):
        output="raisin = 50 \npommes = 30 \npoires = 10 \norange = 20 \n"
        self.fruits.reverse()
        self.assertEquals(self.fruits.__repr__(), output)

if __name__ =='__main__':
    unittest.main()