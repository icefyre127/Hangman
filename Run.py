#!/usr/bin/python
#if the file is the main file then start the program
DICTIONARY = "words.txt"
TITLE_FILE="title.txt"
GRAPHIC_FILE = "hanged man.txt"
INDENT = ""

class Tile:
	def __init__(self,ch = None):
		self.character = ch
		self.visible = false

		

screenMatrix = [[" " for x in xrange(5)] for x in xrange(5)] 


def printTitle():
   with open(TITLE_FILE) as titleFile:
      title = titleFile.read()
      print title

def showHangman():
   with open(GRAPHIC_FILE) as titleFile:
      title = titleFile.read()
      print title

def newLine(num = 1):
    for i in range(num): print
    
if __name__ == '__main__':
    printTitle()
    newLine(5)
    showHangman()
def init():
    pass
