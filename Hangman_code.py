import random
from hangman_words import word_list
from HangManArt import stages, logo

print(logo)
game_end = False
lives = 6
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
# Testing the random choice .
print(chosen_word)

display = []
for _ in range(word_lenght):
    display += "_"

#Looping with while to iterate every aspect of the game.
while not game_end:
    guess = input(f"Please choose your letter: ").lower()

    if guess in display:
        print(f"You already guessed this letter {guess}.")

#Check guessed letter        
    for position in range(word_lenght):
        letter = chosen_word[position]
#        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        
        if letter == guess:
            display[position] = letter  

# Check if user is wrong
    if guess not in chosen_word:          
        print(f"You guessed wrong, you have {lives} guesses left.")
        lives -= 1
        if lives == 0:
            game_end = True
            print(f"Game ended, you lose!!!")

# Joining everything together as string .
    print(' '.join(display))

# Check if user guessed the word right and won.
    if '_' not in display:
        game_end = True
        print(f"Congratulations, you win!!!")

# Printing the the hang man status acording to the lives remaining, the stages\n 
# list must be in a decending order of his death.
    print(stages[lives])

    
