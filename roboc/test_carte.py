from carte import *
import unittest
import sys

class carteTest(unittest.TestCase):
    def setUp(self):
        self.easyMap     = "OOOOOOOOOO\nO O    O O\nO . OO   O\nO O O   XO\nO OOOO O.O\nO O O    U\nO OOOOOO.O\nO O      O\nO O OOOOOO\nO . O    O\nOOOOOOOOOO\n"
        self.myMap = Carte("test",self.easyMap)
        
    def test_get_robot_position(self):
        self.assertEquals(self.myMap.get_robot_position(),(8,3))

    def test_get_map_situation(self):
        self.assertEquals(self.myMap.get_map_situation(8,4),".")
        self.assertEquals(self.myMap.get_map_situation(8,3),"X")
        self.assertEquals(self.myMap.get_map_situation(9,3),"O")
        self.assertEquals(self.myMap.get_map_situation(0,0),"O")
    
    def test_update_map(self):
        self.myMap.update_map("E")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,3))
        self.myMap.update_map("O")  ;   self.assertEquals(self.myMap.get_robot_position(),(7,3))
        self.myMap.update_map("O")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,3))
        self.myMap.update_map("O")  ;   self.assertEquals(self.myMap.get_robot_position(),(5,3))
        self.myMap.update_map("O")  ;   self.assertEquals(self.myMap.get_robot_position(),(5,3))
        self.myMap.update_map("E")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,3))
        self.myMap.update_map("N")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,2))
        self.myMap.update_map("N")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,1))
        self.myMap.update_map("S")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,2))
        self.myMap.update_map("E")  ;   self.assertEquals(self.myMap.get_robot_position(),(7,2))
        self.myMap.update_map("E")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,2))
        self.myMap.update_map("S")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,3))

if __name__ =='__main__':
    unittest.main()