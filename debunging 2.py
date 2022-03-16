import random
# def play():
#     user=input("what's your choice? rock , pepar , scissors:-")
#     user=user.lower()
#     computer=random.choice(['rock','pepar','scissors'])
#     if user==computer:
#         return "you and the computer have both chose {}.Its a tie".format(computer)
#     if is_win(user,computer):  
#        return "you have chosen {} and the computer has chosen {}.you won!".format(user,computer)
#     return "you have chosen {} and the computer has chosen {}. you lost:(".format(user,computer)
# def is_win(players,opponent):
#     if (players=="rock" and opponent=="scissors") or (players=="scissors" and opponent=="pepar") or (players=="pepar" and opponent=="rock"):
#         return True
#     return False  

# print(play())



from random import randint

def win():
    print ('You win!')
def lose():
    print ('You lose!')
while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    moves = ['rock', 'paper', 'scissors']
    random_move = randint(0, 2)
    computer_choice = moves[random_move]
    print(computer_choice)
    if player_choice == computer_choice:
        print ('Draw!')
    elif moves == 'rock' and computer_choice == 'scissors':
        win()
    elif  player_choice== 'paper' and computer_choice == 'scissors':
        lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    elif player_choice=="rock"  and computer_choice == "pepar":
        lose()
    again = input('Do you want to play again? (y or n)').strip()
    if again == 'y':
        continue
    else:
        break

        