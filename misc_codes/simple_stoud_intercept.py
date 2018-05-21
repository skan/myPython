import unittest
import sys
 
def fn_print(nrepeat):
    print "ab"*nrepeat
 
class MyTest(unittest.TestCase):
    def test_stdout(self):
        class MyOutput(object):
            def __init__(self):
                self.data = []
 
            def write(self, s):
                self.data.append(s)
 
            def __str__(self):
                return "".join(self.data)
 
        stdout_org = sys.stdout
        my_stdout = MyOutput()
        try:
            sys.stdout = my_stdout
            fn_print(2)
        finally:
            sys.stdout = stdout_org
 
        self.assertEquals( str(my_stdout), "abab\n") 
 
if __name__ == "__main__":
    unittest.main()