from carte import *
import unittest
import sys

class carteTest(unittest.TestCase):
    def setUp(self):
        self.easyMap     = "OOOOOOOOOO\nO O    O O\nO . OO   O\nO O O   XO\nO OOOO O.O\nO O O    U\nO OOOOOO.O\nO O      O\nO O OOOOOO\nO . O    O\nOOOOOOOOOO\n"
        self.myMap = Carte("test",self.easyMap)
        
    def test_get_robot_position(self):
        output=(3,8)
        result = self.myMap.get_robot_position()
        self.assertEquals(result,output)

    def test_get_map_situation(self):
        self.assertEquals(self.myMap.get_map_situation(8,4),".")
        self.assertEquals(self.myMap.get_map_situation(8,3),"X")
        self.assertEquals(self.myMap.get_map_situation(9,3),"O")
        self.assertEquals(self.myMap.get_map_situation(0,0),"O")
if __name__ =='__main__':
    unittest.main()