#guessing_Game
#!/usr/bin/env python3
import string                                                               
import os                                                                   # Used for clearing the term window
import time                                                                 # Used for 5 second buffer at the end of the game
import random                                                               # To pick random word from list
from tkinter import *                                                       # GUI
import tkinter as tk                                                        # GUI
from tkinter import messagebox                                              # GUI Message Box

'''
    Start of Console Code
'''
class hangman:
    played_word = ""                                                        # Word in play
    gameboard = []                                                          # Playing game board
    gameboard_finished = []                                                 # End-State game board
    guess = ''                                                              # Guess that's made
    guess_archieve = ['Guesses:']                                           # Creates list of all guesses
    lives = ['Lives(5):']                                                      # Players life count
    end_state = False                                                       # Is the game over
    # List create from random word generator
    word_list = ['stun','amuse','comment','systematic','adviser','argument','chemistry','ward','goal','knot','confession','desk','opinion','dilute','horoscope','number','overall','dark','girl','association','reserve','shrink','autonomy','worker','confrontation','mountain','conception','corpse','prestige','family','belief','mobile','trouble','temptation']
 

    def set_Word(self):
        word = random.choice(self.word_list)                                # Using random to grab random word from word_list
        self.played_word = word

    def set_finished_board(self,word):
        word_list_finished = list(word)
        self.gameboard_finished = word_list_finished

    def set_create_board(self,word):
        word_list_playing = ['_'] * len(word)
        self.gameboard = word_list_playing

    def set_move(self,guess,location):
        self.gameboard[location] = guess

    def set_guess(self,player_guess):
        if(player_guess in self.guess_archieve):                            # Check if guess has already been made
            print("You have already tried to play " + player_guess)    
        elif(player_guess in self.gameboard_finished):                      # Checking if guess is in found in gameboard_finished
            for position,char in enumerate(self.gameboard_finished):
                if char== player_guess:                                     # Checks for all chances of the guess within gameboard_finished
                    self.set_move(self,player_guess,position)
            self.guess_archieve.append(player_guess)
        else:
            self.lives.append('x')                                          # Add x to lives
            self.guess_archieve.append(player_guess)                    


    def get_eg_status(self):
        if(len(self.lives) == 6):
            os.system('cls' if os.name == 'nt' else 'clear')                # Clear term
            self.end_state = True
            messagebox.showinfo("GAME OVER!", "GAME OVER: Thanks for playing! \n Answer:\t" + str(''.join([str(elem) for elem in self.gameboard_finished])))
            main_form.quit()
        elif(self.gameboard == self.gameboard_finished):
            os.system('cls' if os.name == 'nt' else 'clear')                # Clear term
            self.end_state = True
            messagebox.showinfo("Congrats!", "You won! Thanks for playing!")
            main_form.quit()


    def get_user_guess(self,letter):
        char = str(letter)
        if(len(char) == 1 and char.isalpha()):
            self.set_guess(self,char.lower())
        else:
            print("Guess must be a single letter!")
            
game = hangman                                                              # Create Game Object
game.set_Word(game)                                                         # Word in play
game.set_create_board(game,game.played_word)                                # game board
game.set_finished_board(game,game.played_word)                              # end-state 
'''
    End of Console Code
'''

'''
    Build GUI interface using Tkinter
'''
main_form = Tk()                                                            # Create Form Object
main_form.title("Guessing_Game")
main_form.geometry("600x310")                                               # Set form size
main_form.resizable(0,0)                                                    # Disables Resizing

# GUI Vars
alphaList = list(string.ascii_lowercase)                                    # Creates Alpha list
game.gameboard


gui_gameboard = tk.Label(main_form, text=game.gameboard ,font = "Verdana 30 bold")
gui_gameboard.pack(side="top")

gui_guess_archieve = tk.Label(main_form, text=game.guess_archieve ,font = "Verdana 10 bold")
gui_guess_archieve.pack()
gui_guess_archieve.place(bordermode=OUTSIDE, x=200, y=260)

gui_lives = tk.Label(main_form, text=game.lives ,font = "Verdana 10 bold")
gui_lives.pack()
gui_lives.place(bordermode=OUTSIDE, x=200, y=280)

def btn_Click(self,letter):
    self.config(state="disabled")
    game.get_user_guess(game,letter.lower())
    gui_gameboard['text'] = game.gameboard
    gui_guess_archieve['text'] = game.guess_archieve
    gui_lives['text'] = game.lives
    game.get_eg_status(game)                                                # Check End-Game Status
    print(letter)    

def create_button(letter,xpos,ypos,index):
    letter = tk.Button(main_form, text=(alphaList[index].upper()),command = lambda: btn_Click(letter,alphaList[index].upper()))
    letter.pack()
    letter.place(bordermode=OUTSIDE, height=50, width=100,x=xpos,y=ypos)

def populate_board():                                                       # Generates Form with Alpha. buttons 
    c = 0
    startpos = 60
    xpos = 0
    ypos = startpos
    while(c < 26):
        # Formating Buttons
        if(c == 6):
            ypos = startpos + 50
            xpos = 0
        elif(c == 12):
            ypos = startpos + 100
            xpos = 0
        elif(c == 18):
            ypos = startpos + 150
            xpos = 0
        elif(c == 24):
            ypos = startpos + 200
            xpos = 0

        create_button(alphaList[c],xpos,ypos,c)
        xpos = xpos + 100
        c = c + 1 
populate_board()
main_form.mainloop()
'''
    End of GUI Build
'''