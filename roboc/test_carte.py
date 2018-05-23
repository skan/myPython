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
    
    def test_robot_composed_move(self):
        self.myMap.move_robot("2N")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,1))
        self.myMap.move_robot("2S")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,3))
        self.myMap.move_robot("9O")  ;   self.assertEquals(self.myMap.get_robot_position(),(5,3))
        self.myMap.move_robot("8E")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,3))

    def test_robot_move_sequence_win_simple_map(self):
        """ move up and down"""
        self.myMap.move_robot("N")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,2))
        self.myMap.move_robot("S")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,3))
        """ going lef until a whole (3 walls around)"""
        self.myMap.move_robot("O")  ;   self.assertEquals(self.myMap.get_robot_position(),(7,3))
        self.myMap.move_robot("h")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,3))
        self.myMap.move_robot("o")  ;   self.assertEquals(self.myMap.get_robot_position(),(5,3))
        self.myMap.move_robot("O")  ;   self.assertEquals(self.myMap.get_robot_position(),(5,3))
        self.myMap.move_robot("j")  ;   self.assertEquals(self.myMap.get_robot_position(),(5,3))
        self.myMap.move_robot("N")  ;   self.assertEquals(self.myMap.get_robot_position(),(5,3))
        """ go back once et move up until the wall""" 
        self.myMap.move_robot("E")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,3))
        self.myMap.move_robot("n")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,2))
        self.myMap.move_robot("k")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,1))
        self.myMap.move_robot("N")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,1))
        """ go back donw and move right until the wall""" 
        self.myMap.move_robot("S")  ;   self.assertEquals(self.myMap.get_robot_position(),(6,2))
        self.myMap.move_robot("E")  ;   self.assertEquals(self.myMap.get_robot_position(),(7,2))
        self.myMap.move_robot("l")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,2))
        self.myMap.move_robot("E")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,2))
        """ go back donw to the initial position""" 
        self.myMap.move_robot("S")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,3))
        """ go down through the doord""" 
        self.myMap.move_robot("S")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,4))
        self.myMap.move_robot("S")  ;   self.assertEquals(self.myMap.get_robot_position(),(8,5))
        self.assertEquals(self.myMap.get_map_situation(8,4),".")
        self.assertEquals(self.myMap.gameOver,0)
        self.myMap.move_robot("E")  ;   self.assertEquals(self.myMap.get_robot_position(),(9,5))
        self.assertEquals(self.myMap.gameOver,1)
        
        #with self.assertRaises(NameError):
        #    self.myMap.move_robot("x") 
        #    self.myMap.move_robot("p") 

if __name__ =='__main__':
    unittest.main()