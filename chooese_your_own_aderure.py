


def adverture_game(username) :

    print('Welcome ' + username + ' to this adventure!')

    while True :

        try :

            answer = input('you are on the dirt a  road, it has to come to an end and you can go to the left or right. which way would you like to go (left/right) ? ').strip()

            if answer == 'left' :

                answer = input('You came to the river, you can walk around or swim accross? would you like to swim or walk around(walk/swim) ? ').strip().lower() 

                if answer == 'swim' : 
                    print('you swam accrpss and wear eaten by alligator.')

                elif answer == 'walk' : 
                    print('you walk for many miles, ran out of the water and you lost the game.')
                
                else :

                    print(' invalid optioin, you lost.')
            elif answer == 'right' :
                
                answer = input('you come to the bridgem, it looks wobbly, do you want to cross it or head back (cross/back) ? ').strip().lower()

                if answer == 'back' :
                    print(' you go back and you lost!')

                elif answer == 'cross' :
                    answer = input('you cross and you mate a stringor will you take to him(yes/no? ').strip().lower() 
                    if answer == 'yes' :
                        print('you took to the stringer and he gave you a gold!, you WON :).')
                    elif answer == 'no' :
                        print('you mate the stringer and you did not take to him, you lost the game:(.')
                    else :
                        print('invald option, you lost!')
            else : 
                print('invlaid option, you lost.')
        except :
            print('invalid input.')
        keep_play = input('Do you still want to play? ').strip().lower()

        if keep_play != 'yes' or keep_play != 'y' :
            break 


name = input('Enter Your Name ? ').strip().capitalize()

print(adverture_game(name))
    