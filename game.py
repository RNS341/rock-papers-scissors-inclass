# game.py

print("Rock, Paper, Scissors, Shoot!") 

# Capture Inputs

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")
print("-------------")
print("User Choice: ",user_choice)

# Validate Inputs

if user_choice not in ["rock","paper","scissors"]:   
    print("invalid selection please try again")
    exit()

# Generate Computer Selection
print("Generating...")

# Display Final Outputs / Outcomes