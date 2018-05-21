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
        self.fruits     = OrganizedDico(raisin=50,poires=10,orange=20, pommes=30)
        self.vegetables = OrganizedDico(potatoes=70)
        
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
    
    def test_length(self):
        self.assertEquals(self.fruits.len(), 4)

    def test_sort(self):
        self.fruits.sort()
        output="poires = 10 \norange = 20 \npommes = 30 \nraisin = 50 \n"
        self.assertEquals(self.fruits.__repr__(), output)
    
    def test_get_item(self):
        self.assertEquals(self.fruits['raisin'], 50)
        self.assertEquals(self.fruits['pommes'], 30)
        self.assertEquals(self.fruits['orange'], 20)
        self.assertEquals(self.fruits['poires'], 10)
        self.assertEquals(self.fruits['blabla'], 0)
    
    def test_del_item(self):
        self.assertIn('raisin',self.fruits)
        del self.fruits['raisin']
        self.assertNotIn('raisin',self.fruits)

        with self.assertRaises(ValueError):
            del self.fruits['fraises']

    def test_set_item(self):
        self.fruits['fraises']=31
        self.assertEquals(self.fruits['fraises'], 31)
        self.assertEquals(self.fruits['poires'], 10)
        self.fruits['poires']=23
        self.assertEquals(self.fruits['poires'], 23)

    def test_in(self):
        self.assertTrue('raisin' in self.fruits)
        self.assertFalse('raisinS' in self.fruits)

    def test_addition(self):
        self.fruits     = OrganizedDico(raisin=50,poires=10,orange=20, pommes=30)
        output="orange = 20 \npoires = 10 \npommes = 30 \nraisin = 50 \npotatoes = 70 \n"
        result = self.fruits + self.vegetables
        self.assertEquals(result.__repr__(), output)
        result += self.vegetables
        output="orange = 20 \npoires = 10 \npommes = 30 \nraisin = 50 \npotatoes = 140 \n"
        self.assertEquals(result.__repr__(), output)
        result = self.fruits + self.fruits
        output="orange = 40 \npoires = 20 \npommes = 60 \nraisin = 100 \n"
        self.assertEquals(result.__repr__(), output)

    def test_for_loop(self):
        test=""
        for k,l in self.fruits:
            test += ("{0} - {1} ".format(k,l))
        output="orange - 20 poires - 10 pommes - 30 raisin - 50 "
        self.assertEquals(test, output)

    def test_for_loop_keys(self):
        test=""
        for k in self.fruits.keys():
            test += ("{0} ".format(k))
        output="orange poires pommes raisin "
        self.assertEquals(test, output)

    def test_for_loop_values(self):
        test=""
        for k in self.fruits.values():
            test += ("{0} ".format(k))
        output="20 10 30 50 "
        self.assertEquals(test, output)
    
    def test_init_withObject(self):
        monPanier2 = OrganizedDico(self.fruits)
        output="orange = 20 \npoires = 10 \npommes = 30 \nraisin = 50 \n"
        self.assertEquals(monPanier2.__repr__(), output)

        with self.assertRaises(TypeError):
            monPanier2 = OrganizedDico("blabla")

        monPanier2 = OrganizedDico(self.fruits, banane=1)
        output="banane = 1 \norange = 20 \npoires = 10 \npommes = 30 \nraisin = 50 \n"
        self.assertEquals(monPanier2.__repr__(), output)

if __name__ =='__main__':
    unittest.main()