import numpy as np

def main():
    p1_score = 0
    p2_score = 0
    print('Description:')
    print('You and your opponent each roll a die (1 to 6).')
    print('The player who guesses a number closer to the actual sum')
    print('of both dice wins the round.')
    print('')
    
    difficulty = int(input('Difficulty 1 (lowest) to 3 (highest): '))

    for _ in range(100):
        p1_roll = np.random.randint(1, 7)
        p2_roll = np.random.randint(1, 7)
        sum = p1_roll + p2_roll
        
        print('You rolled a', str(p1_roll) + str('!'))
        
        reroll = True
        while reroll:
            p1_guess = input('Guess sum: ' + str(p1_roll + 1) + '-' + str(p1_roll + 6) + ': ')
            if difficulty == 1:
                p2_guess = p2_roll + np.random.randint(0, 2) * 4 + np.random.randint(1, 3)
            elif difficulty == 2:
                choice = np.random.randint(0, 4)
                if choice == 0:
                    p2_guess = 7
                else:
                    p2_guess = p2_roll + np.random.randint(1, 7)
            else:
                choice = np.random.randint(0,3)
                p2_guess = p2_roll + np.random.randint(3, 5)
                if choice == 0:
                    p2_guess = p2_roll + np.random.randint(2, 6)
            
            if p1_guess != '':
                p1_guess = int(p1_guess)
                if (p1_guess >= p1_roll + 1) and (p1_guess < p1_roll + 7):
                    reroll = False
        
        print('\nThe actual sum is', sum)
        print('Opponent: Rolled:', str(p2_roll) + ', Guess:', p2_guess)
        
        if abs(p1_guess - sum) < abs(p2_guess - sum):
            p1_score += 1
            print('You win!')
        elif abs(p1_guess - sum) == abs(p2_guess - sum):
            print('Tie')
        else:
            p2_score += 1
            print('You lose')
        
        print('Score:', p1_score, '-', p2_score)
        wait = input('\nPress \'Enter\' to play again.\n')

if __name__ == "__main__":
    main()