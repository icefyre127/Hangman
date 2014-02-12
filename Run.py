#!/usr/bin/python
#if the file is the main file then start the program

import os
import random
import platform

DICTIONARY = "words.txt"
TITLE_FILE="title.txt"
GRAPHIC_FILE = "hanged man.txt"
GRAPHIC_SIZE = 10 
END_STATE = 7
INDENT = ""
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 24
WORD_FILE = "LIST_OF_WORDS.txt"
HIDDEN_LETTER = " _ "


class Word:
   def __init__(self,string):
      self.word = [self.Letter(ch) for ch in string]
#     self.debug = string
   def __str__(self):
      word = []
      for char in self.word:
         word.append(str(char))

      return "".join(word)

   #checks whether a letter exists in a word, sets the matches to visible and returns the number of matches found
   def checkGuess(self, guess):
      matches = 0
      for letter in self.word:
         if guess == letter.character:
            letter.visible = True
            matches = matches + 1      
      return matches

   def revealed(self):
      for letter in self.word:
         if letter.character != " " and not letter.visible: 
            return False
      return True

   class Letter:
      def __init__(self,char = None):
         self.character = char
         self.visible = False

      def __str__(self):
         if self.visible: 
            return " %s " % self.character 
         else: 
            return HIDDEN_LETTER
      

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

      
class HangmanGame:
 
   def __init__(self):

       with open(TITLE_FILE) as titleFile:
         self.title = titleFile.read()

       #used to store indexes of previously picked words, only storing indexes instead of words to conserve memory (line numbers take less space than the word)
       self.previousWords=[]        
       
       #load the word dictionary into memory (keeping full list in memory for speed, shouldn't be a problem unless word list is insanely large)
       self.words = open(WORD_FILE).readlines()
       self.words = [str.rstrip(word) for word in self.words]
       self.pickWord()  #picks a random word to store internal variable called self.word
       self.guessedLetters = []
       self.hangman = HangmanPic()


   #picks a random word from word list and stores it in self.word
   def pickWord(self):
      
      #pick a random word from word list by array index
      lineNum = random.randint(0,len(self.words)-1)

      #if word was previously picked, keep picking randomly until you get a word that wasn't picked
      while lineNum in self.previousWords:
          lineNum = random.randint(0,len(self.words)-1)
      
      self.previousWords.append(lineNum)       
      
      #store uppercase version of randomly selected word (uppercase is easier to read)
      self.word = Word(self.words[lineNum].upper())


   #return number of matches found in word. If guess is NOT a letter, return -1 as error code
   def checkGuess(self,guess):

      if str.isalpha(guess):
         self.guessedLetters.append(guess)
         matches = self.word.checkGuess(guess)
         return matches
      
      return -1

            
   def reset(self):

       #picks a random word to store internal variable called self.word
       self.pickWord()
       self.guessedLetters = []
       self.hangman = HangmanPic()

   def playAgain(self):
      yesNo = raw_input("Play again? (Y/N): ")
      if yesNo[0].upper() == 'Y': 
         self.reset()
      else:
         print "Thanks for playing!"
         exit(0)      

   def play(self):
      print self.title
      print "\n"*5


#message variable is used to store and communicate messages back to the player (e.g. correct guess, win, lose etc...)
      message = """
Welcome to hangman! Please guess one letter at a time, only the first letter typed will be taken as a guess 
For example: if you type 'dog', I will only read the first letter 'd' as your guess)
"""


      while True:
         print self.hangman
         print "\nWord:", self.word
         print "Previously guessed letters: ", ", ".join(self.guessedLetters)
#used for debugging        print "WORD IS: ", self.word.debug  
         print message
         guess = raw_input("\nGuess letter: ")
         guess = guess[0]

         
         if not guess.isalpha():
            message = "Error! Please only guess letters!"
            continue
         
         guess = guess.upper()
         
         if guess in self.guessedLetters:
            message = "You have already guessed that letter! Try another!"
            continue

         
         matches = self.checkGuess(guess)

         if matches == 0:
            self.hangman.update()
            message = "Sorry, the letter " + guess + " was not found!"
            
            #Check if player lost the game
            if self.hangman.state == END_STATE: 
               print self.hangman
               print "Sorry, you lose!"
               self.playAgain()            

            
         elif matches > 0 :
            message =  "Congratulations! I've found "+ str(matches) + " match(s) for the letter "+ guess + "!"
            
            #check if player won the game
            if self.word.revealed():
               print "You've won the game!"            
               self.playAgain()




    
if __name__ == '__main__':

    game = HangmanGame()
    game.play()
    

def init():
    pass
