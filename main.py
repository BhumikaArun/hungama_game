import random

word_list = ["aardvark", "baboon", "camel"]
lives = 6
choose_word = random.choice(word_list)
print(choose_word)  # for testing purposes
placeholder = ""
word_length = len(choose_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

# Function to display the hangman figure based on remaining lives
def display_hangman(lives):
    stages = [
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |   
          ---
        ''',  # 0 lives
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  / 
           |   
          ---
        ''',  # 1 life
        '''
           -----
           |   |
           |   O
           |  /|\\
           |   
           |   
          ---
        ''',  # 2 lives
        '''
           -----
           |   |
           |   O
           |  /|
           |   
           |   
          ---
        ''',  # 3 lives
        '''
           -----
           |   |
           |   O
           |   |
           |   
           |   
          ---
        ''',  # 4 lives
        '''
           -----
           |   |
           |   O
           |   
           |   
           |   
          ---
        ''',  # 5 lives
        '''
           -----
           |   |
           |   
           |   
           |   
           |   
          ---
        '''  # 6 lives (initial stage)
    ]
    print(stages[lives])

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in choose_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in choose_word:
        lives -= 1
        display_hangman(lives)  # Call the hangman display function
        if lives == 0:
            game_over = True
            print("You lose. The word was:", choose_word)

    if "_" not in display:
        game_over = True
        print("You win!")

    print(f"Lives remaining: {lives}")
