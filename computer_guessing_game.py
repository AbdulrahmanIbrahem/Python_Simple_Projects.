


""" 
computer guessing number program => the computer will gusess
the user's number 

"""
import random

play_game = 'y'
start = 0
end   = 100
direction = 'N'

while play_game == 'y' :
    
    smallest = start 
    largest  = end 
    print('Gusess a number between 1 and 100: ')
    try_number = random.randint(start, end) 
    print(try_number) 
    counter = 0
    
    while direction != 'C' :
        direction = input('is it too large (L), too small (S), or correct (C) : ').strip()
        
        if direction == 'S' :
            
            if try_number > smallest :
                
                smallest = try_number + 1 
                
            try_number = random.randint(smallest, largest) 
            print(try_number) 
            
        if direction == 'L' :
            
            if try_number < largest :
                
                largest = try_number - 1
            try_number = random.randint(smallest, largest) 
            print(try_number)
            
        counter += 1
        
    print('I got it! I tried ' + str(counter) + ' tries')   
    play_game = input('Continue? ').strip().lower()  
    
    
    
    
            
            
            
            
            
            
            
            
            
            
            
    
    
    