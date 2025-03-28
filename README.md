# Grade Calculator
This Python script collects a user's score, validates the input, and computes their grade based on predefined score ranges. It handles exceptions to ensure only valid numerical input is processed.

## Features
- Prompts the user to input their score.
- Validates the input to ensure it's a number.
- Computes and returns a grade based on the score:
  - A: 90% - 100%
  - B: 80% - 89%
  - C: 70% - 79%
  - D: 60% - 69%
  - F: Below 60%
- Displays a message if the input is invalid or outside the accepted range.

## How to Run
1. Clone or download the repository.
2. Open the terminal and navigate to the project folder.
3. Run the script with `python compute_grade.py` (or use the appropriate Python command for your environment).
4. Enter a score when prompted to see your grade.

## Example
```
Enter your score: 0.85
Your grade: B
```
If an invalid input is provided, the user will be asked to enter a valid number.
