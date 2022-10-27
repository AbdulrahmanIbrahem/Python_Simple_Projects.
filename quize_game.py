

# from os import access


# print('Welcome to my computer quize!')

# play_game = input('Do You want to play? ').strip().lower()
# score = 0

# if play_game != 'yes' :
#     quit()

# print('okay! let play :)')

# answer = input('What does CPU stands for ? ').strip().title() 

# if answer == "Central Processing Unit" :
#     print('correct!') 
#     score += 1
# else :
#     print('Incorrect!')

# answer = input('What does GPU stands for ? ').strip().title() 

# if answer == 'Graphics Processing Unit' :
#     print('Correct!')
#     score += 1
# else :
#     print('Incorrect!')

# answer = input('What does RAM stands for ? ').strip().title() 

# if answer == 'Random Acess Memory' :
#     print('Correct!')
#     score += 1
# else :
#     print('Incorrect!')

# answer = input('What does PSU stands for ? ').strip().title() 

# if answer == 'Power Supply' :
#     print('Correct!')
#     score += 1
# else : 
#     print('incorrect!'.capitalize())
# print('You got ' + str(score) + f' {"questions" if score > 1 else "question"} Correct!')
# print('You got ' + str((score / 4) * 100) + '%')



# other way of doing the program using loop.
score = 0
questions = ['CPU', 'GPU', 'RAM', 'PSU', 'ROM']

def quize(score, questions) :

    print('Welcome to my computer quize!')

    play_guize = input('Do You want to stard playing ? ').strip().lower() 

    if play_guize != 'yes' : 
        quit()

    else :
        print('Okay! lets play :)')

        for question in questions :
            
            answer = input(f'What does {question} stands for ? ').strip().title() 
            if answer == 'Central Processing Unit' or answer == 'Graphics Processing Unit' or \
                    answer == 'Random Acess Memory' or answer == 'Power Supply' or answer == 'Read Only Memory' :
                        print('Correct!')
                        score += 1
            else :
                print('incoreect!'.capitalize())
        print('I got ' + str(score) + ' question correct')
        print('I got ' + str( (score / len(questions) * 100) ) + '%')

quize(score, questions)