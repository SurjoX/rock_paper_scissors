import random
import time

moves = ['r', 'p', 's']
symbols = {
    'r': '🗿',
    'p': '📜',
    's': '✂️'
}
w_c = ['pr', 'sp', 'rs']
player_score = 0
computer_score = 0

while True:
    try:
        rounds = int(input('How many rounds do you wanna play? '))
        break
    except ValueError:
        print("Please enter a valid number.")

for _ in range(rounds):
    print(f"\nRound-{_ + 1}: You vs. Computer")
    print("Get ready!")
    time.sleep(0.5)
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Go!")
    computer = random.choice(moves)

    while True:
        move = input('\nRock, paper, or scissors? (r/p/s): ').lower()
        if move in moves:
            break
        else:
            print('Please enter a valid move.')
    print(f"\nYou chose {symbols[move]}")
    print(f'Computer chose {symbols[computer]}')
    if move == computer:
        print("😐It's a tie")
        time.sleep(1.75)
    elif (move + computer) in w_c:
        print("🎉You win!")
        player_score += 1
        time.sleep(1.75)
    else:
        print("💔You lose!")
        computer_score += 1
        time.sleep(1.75)

print(f'\nYour score: {player_score}')
print(f"Computer's score: {computer_score}")
if player_score > computer_score:
    print("Based on final scores, you win! 🏆")
elif player_score < computer_score:
    print("Based on final scores, you lose. 😞")
else:
    print("It's a tie! 😐")


