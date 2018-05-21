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
    
    def test_set_item(self):
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


#print("test print direct addition fruits avec patates")
#mesLegumes = OrganizedDico(patates=70)
#print (mesLegumes+mesFruits)
#print ("mes legumes pour check, que patates")
#print (mesLegumes)
#
##print ("print dico result test"):wa

##dicoResult= mesLegumes + mesFruits
##print (dicoResult)
#
#print ("mon panier")
#print(monPanier)

#monPanier = OrganizedDico(cerises=77)
#print("test addition legumes avec += cerises")
#mesLegumes += monPanier
#print (mesLegumes)
#print("test addition legumes avec += fruits")
#mesLegumes += mesFruits
#print (mesLegumes)
#
#for k,l in mesFruits:
#    print ("item {0} & {1}".format(k,l))
#
#for k in mesFruits.keys():
#    print ("test key {0} ".format(k))
#
#for k in mesFruits.values():
#    print ("test values {0} ".format(k))
#
#for k,l in mesFruits.items():
#    print ("test items {0} {1} ".format(k,l))
#
#
#monPanier2 = OrganizedDico(mesFruits, cornichon=21, carottes=43)
#print (monPanier2)
#
#print ("test blabla input")
#blabla={}
#monPanier2 = OrganizedDico(blabla, cornichon=21, carottes=43)

if __name__ =='__main__':
    unittest.main()