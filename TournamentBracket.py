
# Tournament Bracket

##Geneiva Ocampo
##CSCI

##In this project I created a list for the user to choose the teams
## The user will be allowed to choose half of the teams to move to the next round
## Then the user will be allowed to guess until the user guesses the winner
## Program will display a most likely-to-win winner on a random guess
## Program will be able to match the text file words to see what percentage of guesses were correct

import random


# Create bracket
def generate_bracket(teams, teams_list):
    bracket = []
    round_number = 1  # Start at round 1

    while len(teams) > 1:  # Will continue to run as long as there is more than one team

        # Begin to add to bracket
        bracket.append(f"Round {round_number}: ")

        # Storage
        next_round_teams = []
        formatted_teams = []
        formatted_results = []
        round_results = []

        half_teams = len(teams) // 2  # Half of the teams will go on to the next round

        # Each team will compete with the other half
        for i in range(half_teams):
            team1 = f"Team {teams[i]} ({teams_list[teams[i] - 1]})"
            team2 = f"Team {teams[i + half_teams]} ({teams_list[teams[i + half_teams] - 1]})"
            formatted_teams.append(f" {team1} vs {team2}")

        # Table setup
        max_team_length = max(len(team) for team in formatted_teams)
        for i in range(half_teams):
            team1, team2 = formatted_teams[i].split(' vs ')
            format_table = '{team1:<40}{sep:1}{team2:>43}'
            print(format_table.format(team1=team1, sep='vs', team2=team2))

        # Info to be added to final bracket
        bracket.extend(formatted_teams)

        # Ask user to guess what teams they believe will go to the next round
        for i in range(half_teams):
            while True:
                team = int(input(f"Enter the team number that will advance to the next round from Round {round_number}: "
                                 f"Team {teams[i]} ({teams_list[teams[i] - 1]}) vs Team {teams[i + half_teams]} "
                                 f"({teams_list[teams[i + half_teams] - 1]}) "))

                # Check if the team number is valid
                if teams[i] <= team <= teams[i + half_teams] and team not in next_round_teams:
                    break
                else:
                    print("Invalid team number or already guessed. Choose a different team.")

            next_round_teams.append(team)
            round_results.append(team)

        # Will title the next round's results
        print()
        bracket.append(" " * 15 + "Results:")
        bracket.append(f"You guessed the winner to be: Team {teams[0]} ({teams_list[teams[0] - 1]})")

        # Will make a fake real winner from the teams list
        teams = next_round_teams
        round_number += 1
        random_winner = random.choice(teams_list)
        # Shows a random winner to be the most guessed winner
        print(f"The Most Guessed Winner are the: {random_winner}")

    return bracket


def calculate_percentage_of_matching_words(round_info, file_content):
    # Split the round_info into individual words
    round_words = ' '.join(round_info).split()

    # Split the file content into words
    file_words = file_content.split()

    # Calculate the number of matching words
    matching_words = sum(1 for word in round_words if word in file_words)

    # Calculate the percentage of matching words
    percentage = (matching_words / len(round_words + file_words)) * 100
    return percentage


def main():
    # Repeats Program
    while True:
        # List of teams in tournament
        teams_list = ["Astros", "Orioles", "Dodgers", "Phillies", "Twins ",
                      "White Sox", "Red Sox", "Rangers", "Mariners", "Tigers",
                      "Athletics", "Diamondbacks", "Giants", "Yankees",
                      "Blue Jays", "Cardinals"]

        # Create teams with preset numbers
        teams = [i for i in range(1, 9)]  # Assuming 8 teams are selected initially

        print("\nWelcome to the Tournament Bracket!\n")
        print("List of Teams:")

        # Adds a letter of the position of the team and creates a vertical list
        for i, team in enumerate(teams_list, start=1):
            print(f"{i}. {team}")

        # Used to call the arguments
        tournament_bracket = generate_bracket(teams, teams_list)

        # Displays The full tournament information
        print("\nTournament Bracket:")
        for round_info in tournament_bracket:
            print(round_info)

        file_name = 'teams.txt' 

        try:
            with open(file_name, 'r') as file:
                file_content = file.read()

            # Calculate the percentage of matching words
            result = calculate_percentage_of_matching_words(tournament_bracket, file_content)
            print(f"Percentage of matching words in bracket info and file: {result:.2f}%")

        except FileNotFoundError:
            print(f"Error: {file_name} not found!")

        # Ask the user if they want to repeat program
        repeat = input("\nDo you want to run the program again? (yes/no): ")
        if repeat.lower() != "yes":
            break


if __name__ == "__main__":
    main()
