#!/usr/bin/python
#if the file is the main file then start the program

import os
import random

DICTIONARY = "words.txt"
TITLE_FILE="title.txt"
GRAPHIC_FILE = "hanged man.txt"
GRAPHIC_SIZE = 10 
END_STATE = 7
INDENT = ""
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 24
WORD_FILE = "LIST_OF_WORDS.txt"


class Word:
   def __init__(self,string):
      self.word = [Letter(ch) for ch in string]
   
   def __str__(self):
      for ch in self.word:
         print ch, 

   class Letter:
      def __init__(self,char = None):
         self.character = char
         self.visible = false

      def __str__(self):
         if self.visible: return " %s " % self.char 
         else: return " _ "
      

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
          


class HangmanGame:
 
   def __init__(self):

       #used to store previously picked words
       self.previousWords=[]        

       #load the word dictionary into memory
       self.words = open(WORD_FILE).readlines()
       self.words = [str.rstrip(word) for word in self.words]

       self.pickWord()  #picks a random word to store internal variable called self.word


   #picks a random word from word list and stores it in self.word
   def pickWord(self):
      
      #pick a random word from word list by array index
      lineNum = random.randint(0,len(self.words)-1)

      #if word was previously picked, keep picking randomly until you get a word that wasn't picked
      while lineNum in self.previousWords:
          lineNum = random.randint(0,len(self.words)-1)
      
      self.previousWords.append(lineNum)       
      self.word = self.words[lineNum]
      
   
   def debug(self):
      print "word = %s, previousWords = %s" % (self.word,self.previousWords)

   

       
#    def getWord(self):
#       return self.word

       
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

    # hangman = HangmanPic()
    # screen = Screen()
    # screen.putChar(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,"@")
    # screen.refresh()
   
    game = HangmanGame()
    for i in xrange(10):
       game.debug()
       game.pickWord()


def init():
    pass
