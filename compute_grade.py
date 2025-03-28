# Collect valid input from user & handle exceptions.
try:
    score = input('Enter your score: ')
    scr = float(score)
except:
    print("Please enter a valid number.")
    scr = None

# Define computegrade function & handle exceptions.
def computegrade(scr):
    if scr >= 0.9 and scr <= 1.0:
        return "Your grade: A"
    elif scr >= 0.8 and scr <= 0.89:
        return "Your grade: B"
    elif scr >= 0.7 and scr <= 0.79:
        return "Your grade: C"
    elif scr >= 0.6 and scr <= 0.69:
        return "Your grade: D"
    elif scr <= 0.6 and scr >= 0.0:
        return "Your grade: F"
    else:
        return "Invalid score. Try again."

# Call computegrade function, print result, and handle exceptions.
if scr is not None:
    print(computegrade(scr))
else:
    print("We're unable to compute your grade.")
