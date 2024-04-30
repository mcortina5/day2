# Create a Python script that assigns a grade to a student based on their exam score.
# Ask the user to input a score. Assume the score is out of 100.

# A score below 60 is an "F".
# Ensure the score entered is within the valid range (0-100). If not, print an error message.

# functions allow me to wrap up code and reuse it
# functions are defined with the def keyword

def scoreMe():
    score = int(input("Enter your score: "))
    # Implement the logic to determine the grade based on the score:
    if score >= 90:
        print("A")
    # A score of 90 and above is an "A".
    elif score >= 80 and 89:
        print("B")
    # A score of 80 to 89 is a "B".
    elif score >= 70 and 79:
        print("C")
    # A score of 70 to 79 is a "C".
    elif score >= 60 and 69: 
        print("D")
    # A score of 60 to 69 is a "D".
    elif score < 60:
        print("F")
# call the function
scoreMe()
