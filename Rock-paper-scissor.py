import random

choices=['rock', 'paper', 'scissors']
score_user =0
score_computer=0



def lets_play():
    global score_user, score_computer

    print("--WELCOME TO ROCK,PAPER AND SCISSORS GAME--")
    print(choices)
    print("-"*50)
    user_choice=input("Enter your choice: ").lower()
    print("-"*50)

    computer_choice=random.choice(choices)
    print(f"computer choice: {computer_choice}")
    print("-"*50)


    if user_choice==computer_choice:
        print("Draw")
        print("-"*50)

    elif (user_choice=='rock' and computer_choice=='paper') or \
        (user_choice == 'scissors' and computer_choice=='rock') or \
        (user_choice == 'paper' and computer_choice=='scissors'):
        print("You Lose, Computer Win ")
        score_computer+=1
        print("-"*50)

    elif (user_choice=='rock' and computer_choice=='scissors') or \
         (user_choice == 'scissors' and computer_choice=='paper') or \
         (user_choice == 'paper' and computer_choice=='rock')  :
         print("You Win , computer Lose")
         score_user+=1
         print("-"*50)
        
    else:
        print("INVALID INPUT")
        print("-"*50)


        #Their scores
    print(f"computer's score: {score_computer}\n User's score: {score_user}")
    print("-"*50)



# Asking user if they want to play multiple rounds

while True:
    lets_play()
    play_again=input("Do you want to play again(YES/NO): ").upper()
    print("##**##"*17)

    if play_again !="YES":
        break
print("GAME OVER")
print("-"*20)

print(f"Your final score: {score_user} \ncomputer's final score: {score_computer}")

print("-"*50)

if score_user > score_computer:
    print ("YOU WON")

elif score_user < score_computer:
    print("COMPUTER WON")

else:
    print("Tie")
print("-"*20)
print("-"*20)


