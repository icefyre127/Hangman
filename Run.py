#!/usr/bin/python
#if the file is the main file then start the program
DICTIONARY = "words.txt"
TITLE_FILE="title.txt"
GRAPHIC_FILE = "hanged man.txt"
GRAPHIC_SIZE = 10 
INDENT = ""
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 24


class Tile:
	def __init__(self,ch = None):
		self.character = ch
		self.visible = false


class Hangman():
   def __init__(self): 
        self.graphicFile = open(GRAPHIC_FILE)
        self.update()
        
   def display(self):
        print self.graphic
		

   def update(self):
       lines = []
       for i in xrange(GRAPHIC_SIZE):
          lines.append(self.graphicFile.readline())
       self.graphic = "".join(lines)
          
           
           
screenMatrix = [[" " for x in xrange(SCREEN_WIDTH)] for x in xrange(SCREEN_HEIGHT)] 


def printTitle():
   with open(TITLE_FILE) as titleFile:
      title = titleFile.read()
      print title

def showHangman():
   with open(GRAPHIC_FILE) as titleFile:
      graphic = titleFile.read()
      print title

def newLine(num = 1):
    for i in range(num): print
    
if __name__ == '__main__':
    printTitle()
    newLine(5)
    hangman = Hangman()
    hangman.display()
    hangman.update()
    hangman.display()
def init():
    pass
