Tournament Bracket Generator and Analyzer

Description
This Python program allows users to create and simulate a tournament bracket for a given set of teams. It prompts the user to select teams that advance through rounds and makes random selections for the simulated tournament. Additionally, it calculates the percentage of matching words between the tournament bracket information and a text file.

Features
Bracket Generation: Generates a tournament bracket based on the selected teams.
User Interaction: Allows users to make selections for advancing teams in each round.
Randomized Simulation: Simulates tournament results with random team selections.
Matching Word Percentage Calculation: Compares the tournament bracket info with a text file to calculate matching word percentages.

How to Use
Run the Python program.
Follow the on-screen instructions to select teams for each round.
The program will display the tournament bracket and a simulated winner based on random selection.
Provide a text file (named teams.txt) with relevant words for comparison.
The program will calculate the percentage of matching words between the bracket info and the file.

Usage Instructions
Team Selection: Choose teams for each round until a final winner is determined.
File Input: Ensure a file named teams.txt exists in the same directory as the program.
Repeat Program: The program prompts if you want to rerun; respond with "yes" to repeat the process.

Requirements
Python 3
A text file named teams.txt with relevant words for comparison

Files
tournament_bracket.py: Main Python script for generating the tournament bracket.
teams.txt: Text file for word comparison (to be placed in the same directory as the script).

Example

Welcome to the Tournament Bracket!
List of Teams:
1. Astros
2. Orioles
3. Dodgers
...

...

Percentage of matching words in bracket info and file: 25.00%

Do you want to run the program again? (yes/no): no

Notes
Ensure the teams' list in teams_list corresponds accurately to the teams selected in the bracket.
Make sure to provide a teams.txt file for accurate word-matching analysis.