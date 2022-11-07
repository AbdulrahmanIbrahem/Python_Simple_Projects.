



import random
user_wins_points = 0
computer_wins_points = 0
opetion = ['rock', 'paper', 'scissor']

while True :

    try :
        user_pick = input('Type Rock/Paper/Scissor or Q to quit ? ').strip().lower() 
    
    except ValueError : 
        continue 

    else :
        if user_pick == 'q' :
            break

        if user_pick not in opetion :
            continue 

        random_number = random.randint(0,2) 
        computer_pick = opetion[random_number] 

        print('computer pick', computer_pick)
        if user_pick == 'rock' and computer_pick == 'scissor' :
            print('You won!.')
            user_wins_points += 1

        elif user_pick == 'paper' and computer_pick == 'rock'  :
             
            print('You won!') 
            user_wins_points += 1
        
        elif user_pick == 'scissor' and computer_pick == 'paper' :
            
            print('you won!')
            user_wins_points += 1
        else :
            
            print('computer win!') 
            computer_wins_points += 1
        


print('You Won', user_wins_points, 'times')
print('Computer Won', computer_wins_points, 'times') 
print('Goodbye.')
