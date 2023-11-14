import random, math

teams =["1. Astros", "2.Orioles", "3. Dodgers", "4. Phillies", "5. Twins ",\
        "6. White Sox", "7. Red Sox", "8. Rangers", "9. Mariners", "10. Tigers",\
        "11. Athletics", "12.Diamondbacks", "13.Giants", "14.Yankees",\
        "15. Blue Jays", "16. Cardinals"]
print(teams)

def format_brackets(teams):
  

# Prompt the user to enter their guesses
  print("Guess the teams that will go to the next round:")
  user_guesses = []
  for i in range(8):
    guess = int(input('Guess What number will go to next round? '))
    print(teams[guess-1])
    user_guesses.append(teams[guess-1])


# Compare the user's guesses with the correct teams
  correct_guesses = random.randint(0, len(user_guesses))
  for guess in user_guesses:
    if user_guesses == correct_guesses:
      correct_guesses += 1
      correct_guesses = min(correct_guesses, random_correct_guesses)
  print(f"You guessed {correct_guesses} out of {len(user_guesses)} teams correctly.")
  #  num_teams = len(teams)

### Check if the number of teams is a power of 2
##  if not num_teams or (num_teams & (num_teams - 1)):
##    print("Number of teams must be a power of 2.")
##  return
##
### Create an empty list to store the brackets
##  brackets = []
##
### Calculate the number of rounds needed
##  num_rounds = int(math.log2(num_teams))
##
### Initialize the brackets with the teams
##  for team in teams:
##    brackets.append([team])
##
### Generate the brackets for each round
##  for round_num in range(num_rounds):
##    next_round = []
##
##  for i in range(0, len(brackets), 2):
##    match = brackets[i] + brackets[i+1]
##    next_round.append(match)
##
##  brackets = next_round
##
### Print the formatted brackets
##  for i, match in enumerate(brackets, start=1):
##    print(f"Round {i}: {match}")

format_brackets(teams)


