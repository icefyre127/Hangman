#!/usr/bin/python
#if the file is the main file then start the program

import os

DICTIONARY = "words.txt"
TITLE_FILE="title.txt"
GRAPHIC_FILE = "hanged man.txt"
GRAPHIC_SIZE = 10 
END_STATE = 7
INDENT = ""
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 24


class Tile:
   def __init__(self,ch = None):
        self.character = ch
	self.visible = false


class HangmanPic():
   def __init__(self): 
        self.graphicFile = open(GRAPHIC_FILE)
        self.state = 0
        self.update()
        
   def __str__(self):
        return self.graphic
		

   def update(self):

       if (self.state == END_STATE): 
               return

       self.state = self.state + 1
       lines = []
       for i in xrange(GRAPHIC_SIZE):
          lines.append(self.graphicFile.readline())

       self.graphic = "".join(lines)


          

class Screen():
   def __init__(self):        
       self.screenBuffer = [[" " for x in xrange(SCREEN_WIDTH)] for x in xrange(SCREEN_HEIGHT)] 

   def putChar(self,x,y,char):
       self.screenBuffer[y][x] = char

   def refresh(self): 
       os.system("clear")
       for i in xrange(SCREEN_HEIGHT):
          print "".join(self.screenBuffer[i])
          

# class HangmanGame:
#    def __init__(self):
#        self.

# class Hangman:
#    def __init__(self):
#       self.num_letters_wrong = 0
#       self.num_letters_correct = 0 
#       self.secret_word = random.choice(word_list).upper()
#       self.letter_complete_status = list(" _ " * len(secret_word)

        


def printTitle():
   with open(TITLE_FILE) as titleFile:
      title = titleFile.read()
      print title


def newLine(num = 1):
    for i in range(num): print


            
    
if __name__ == '__main__':

    printTitle()
    newLine(5)

    hangman = HangmanPic()
    screen = Screen()
    screen.putChar(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,"@")
    screen.refresh()
    

def init():
    pass
