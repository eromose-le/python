# A program to guess the correct word (A word game)

# 1. Define the secret word
secret_word = "apple"

# 2. Ask the user to provide/guess a word
guess_word = input("Guess the name of the fruit: ")

# 3. Check if the word guessed by the user matches your secret word
if (guess_word == secret_word):
  # 4. Tell the user if he/she is correct or not
  print("You are correct")
else:
  # 4. Tell the user if he/she is correct or not
  print("You are wrong")