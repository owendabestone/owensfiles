
from find_pos import *
from openloc import *
import random
##initializing 

class MainGame():
    
    counter = 0 
    one_one = ' '
    one_two = ' '
    one_three = ' '
    two_one = ' '
    two_two = ' '
    two_three = ' '
    three_one = ' '
    three_two = ' '
    three_three = ' ' 
    quit = False
    user_selected = []
    bot_selected = []
    user_input = '0'
    bot_input = []
    user_inputted = []
    result_string = None
    
    
    def __init__(self):    
        
        self.playboard = ['  1 2 3','\n',
        ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
          chr(8213),chr(8213),chr(8213),'\n',
          '1',chr(448),self.one_one,chr(448),self.one_two,chr(448),self.one_three,chr(448),'\n',
          ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
            chr(8213),chr(8213),chr(8213),'\n',
         '2',chr(448),self.two_one,chr(448),self.two_two,chr(448),self.two_three,chr(448),'\n',
          ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
          chr(8213),chr(8213),chr(8213),'\n',
         '3',chr(448),self.three_one,chr(448),self.three_two,chr(448),self.three_three,chr(448),'\n',
            ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
      chr(8213),chr(8213),chr(8213)]
        self.final_string = ''
        for items in self.playboard[0:]:
        
            self.final_string = self.final_string + items
            
            
    def restart(self):
        # resets all the values
        
        self.one_one = ' '
        self.one_two = ' '
        self.one_three = ' '
        self.two_one = ' '
        self.two_two = ' '
        self.two_three = ' '
        self.three_one = ' '
        self.three_two = ' '
        self.three_three = ' ' 
        self.user_selected = []
        self.counter = 0 
        self.bot_input = []
        self.user_input = '0'
        self.user_inputted = []  
        
      
    def result(self):
        # tests if at the current move the game has a winner 
        # by checking any winning conditions have been met
        #horitonals 
        if self.one_one == self.one_two == self.one_three:
            if self.one_one =='X':
                print('Good try, you lost:(')                   
                self.counter =1
                self.result_string = 'lose'
                
                
            if self.one_one == 'Ꙩ':
                print('You won!')
                self.counter =1
                self.result_string = 'win'

            
        if self.two_one == self.two_two == self.two_three:
            if self.two_one =='X':
                print('Good try, you lost:(') 
                self.counter =1
                self.result_string = 'lose'
                
            if self.two_one == 'Ꙩ':
                print('You won!')
                self.counter =1
                self.result_string = 'win'
                
        if self.three_one == self.three_two == self.three_three:
            if self.three_one =='X':
                print('Good try, you lost:(')
                self.counter =1
                self.result_string = 'lose'
                
            if self.three_one == 'Ꙩ':
                print('You won!')
                self.counter = 1
                self.result_string = 'win'
                
        #verticals     
        if self.one_two == self.two_two == self.three_two:
            if self.one_two =='X':
                print('Good try, you lost:(')
                self.counter =1
                self.result_string = 'lose'
                
            if self.one_two == 'Ꙩ':
                print('You won!')
                self.counter = 1
                self.result_string = 'win'
                
        if self.one_one == self.two_one == self.three_one:
            if self.one_one =='X':
                print('Good try, you lost:(')
                self.counter =1
                self.result_string = 'lose'
                
            if self.one_one == 'Ꙩ':
                print('You won!')
                self.counter = 1
                self.result_string = 'win'
                
        if self.one_three == self.two_three == self.three_three:
            if self.one_three =='X':
                print('Good try, you lost:(')
                self.counter = 1
                self.result_string = 'lose'
                
            if self.one_three == 'Ꙩ':
                print('You won!')
                self.counter = 1
                self.result_string = 'win'
                
        #diagonal 
        if self.one_one == self.two_two == self.three_three:
            if self.one_one =='X':
                print('Good try, you lost:(')
                self.counter = 1
                self.result_string = 'lose'
                
            if self.one_one == 'Ꙩ':
                print('You won!')
                self.counter = 1
                self.result_string = 'win'
                
        if self.one_three == self.two_two == self.three_one:
            if self.one_three =='X':
                print('Good try, you lost:(')
                self.counter = 1
                self.result_string = 'lose'
                
            if self.one_three == 'Ꙩ':
                print('You won!')
                self.counter = 1
                self.result_string = 'win'
        else:
            self.counter == 0
            
                
                
    def play(self): 
      # Askes user to input a move. 
        if self.counter == 0 :
            self.user_input = input('The block you selected is:')
            
            
            # checking if user would like to quit the game 
            
            if self.user_input == 'quit' or self.user_input == 'QUIT':
                self.quit = True
                print('Hope you liked the game!')
                
                
            # assuming valid inputs
            else: 
                whats_okay = ['11','12','13','21','22','23','33','32','31']
                
                #system will not register
                while ((self.user_input in whats_okay) == False) or (self.user_input in self.user_inputted) or (self.user_input in self.bot_input):
                    
                    if self.user_input == 'quit' or self.user_input == 'QUIT':
                        
                        self.quit = True
                        
                        print('Bye!See you later!')
                        
                        break
                        
                        
                    self.user_input = input('Please choose a valid input. You have to select an EMPTY box.')
                          
       
                if self.user_input == '11':
                    self.one_one = 'Ꙩ'
                elif self.user_input == '12':
                    self.one_two = 'Ꙩ'
                elif self.user_input == '13':
                    self.one_three = 'Ꙩ'
                elif self.user_input == '21':
                    self.two_one = 'Ꙩ'
                elif self.user_input == '22':
                    self.two_two = 'Ꙩ'
                elif self.user_input == '23':
                    self.two_three = 'Ꙩ'  
                elif self.user_input == '31':
                    self.three_one = 'Ꙩ'
                elif self.user_input == '32':
                    self.three_two = 'Ꙩ' 
                elif self.user_input == '33':
                    self.three_three = 'Ꙩ'
                    
                self.user_inputted.append(self.user_input)
                
            #recording the current board 
            
            self.playboard = ['  1 2 3','\n',
        ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
        chr(8213),chr(8213),chr(8213),'\n',
        '1',chr(448),self.one_one,chr(448),self.one_two,chr(448),self.one_three,chr(448),'\n',
        ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
        chr(8213),chr(8213),chr(8213),'\n',
       '2',chr(448),self.two_one,chr(448),self.two_two,chr(448),self.two_three,chr(448),'\n',
       ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
       chr(8213),chr(8213),chr(8213),'\n',
       '3',chr(448),self.three_one,chr(448),self.three_two,chr(448),self.three_three,chr(448),'\n',
        ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
        chr(8213),chr(8213),chr(8213)]
            
            
            for items in self.playboard[0:]:
                self.final_string = self.final_string + items
                
                
          # indication of the game has finished. Nothing runs after. 
        elif self.counter == 1:
            
            None
            
            
            
    def print_board(self):
        
       # Prints out the interface from a long list of strings. 
    
        self.final_string = ''
        
        self.playboard = ['  1 2 3','\n',
        ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
        chr(8213),chr(8213),chr(8213),'\n',
        '1',chr(448),self.one_one,chr(448),self.one_two,chr(448),self.one_three,chr(448),'\n',
        ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
        chr(8213),chr(8213),chr(8213),'\n',
       '2',chr(448),self.two_one,chr(448),self.two_two,chr(448),self.two_three,chr(448),'\n',
       ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
       chr(8213),chr(8213),chr(8213),'\n',
       '3',chr(448),self.three_one,chr(448),self.three_two,chr(448),self.three_three,chr(448),'\n',
        ' ',chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),chr(8213),
        chr(8213),chr(8213),chr(8213)]
        
        for items in self.playboard[0:]:
            self.final_string = self.final_string + items
            
        print(self.final_string)
   
        
        
    def bot(self):
        
        # the computer that play against the player. It detects what has been selected so far and places a random move.
        
        self.user_selected= find_pos1(self.final_string,'Ꙩ')
        
        self.bot_selected= find_pos1(self.final_string,'X')
        
        location_ava = [21,23,25,41,43,45,61,63,65]
        
        
        location_open = open_loc(location_ava,self.user_selected,self.bot_selected)
        
        for num in location_ava:
            
            if ((num in self.user_selected) == False) and ((num in self.bot_selected) == False):
                
                location_open.append(num)
                
        
        # check if the condition is a draw by checking if location_oepn is not an empty list 
        
        if  len(location_open) != 0 :
            
            if (('22' in self.user_inputted)  == False) and (('22' in self.bot_input) == False):
                bot_drop = 43
                self.bot_input.append('22')
                
            else:
            
                bot_drop = random.choice(location_open)
            
            
            # assign drop locations
            
            if bot_drop == 21 and self.one_one != 'Ꙩ' : 
                self.one_one = 'X'
                self.bot_input.append('11')
                
            elif bot_drop == 23 and self.one_two != 'Ꙩ':
                self.one_two = 'X'
                self.bot_input.append('12')
                
            elif bot_drop == 25 and self.one_three != 'Ꙩ':
                self.one_three = 'X'
                self.bot_input.append('13')
                
            elif bot_drop == 41 and self.two_one != 'Ꙩ':
                self.two_one = 'X'
                self.bot_input.append('21')
                
            elif bot_drop == 43 and self.two_two != 'Ꙩ':
                self.two_two = 'X'
                self.bot_input.append('22')
                
            elif bot_drop == 45 and self.two_three != 'Ꙩ':
                self.two_three = 'X'
                self.bot_input.append('23')
                
            elif bot_drop == 61 and self.three_one != 'Ꙩ':
                self.three_one = 'X'
                self.bot_input.append('31')
                
            elif bot_drop == 63 and self.three_two != 'Ꙩ':
                self.three_two = 'X'
                self.bot_input.append('32')
                
            elif bot_drop == 65 and self.three_three != 'Ꙩ':
                self.three_three = 'X'
                self.bot_input.append('33')
                
            else:
                self.bot()
                
        elif self.result_string == 'win' or self.result_string == 'loss':
            print('')
            
        elif len(location_open) == 0:
            print('Draw!!!')
            self.result_string = 'draw'
            
            

