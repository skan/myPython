from carte import *
import unittest
import sys

class carteTest(unittest.TestCase):
    def setUp(self):
        self.easyMap     = "OOOOOOOOOO\nO O    O O\nO . OO   O\nO O O   XO\nO OOOO O.O\nO O O    U\nO OOOOOO.O\nO O      O\nO O OOOOOO\nO . O    O\nOOOOOOOOOO\n"
        self.myMap = Carte("test",self.easyMap)
        
    def test_getRobotPosition(self):
        output=(3,8)
        result = self.myMap.get_robot_position()
        self.assertEquals(result,output)

if __name__ =='__main__':
    unittest.main()