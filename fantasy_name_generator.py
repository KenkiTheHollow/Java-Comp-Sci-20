import random

# Read names from files into lists
with open("maleNames.txt", "r") as file:
    male_names = [line.strip() for line in file]

with open("femaleNames.txt", "r") as file:
    female_names = [line.strip() for line in file]

with open("lastNames.txt", "r") as file:
    last_names = [line.strip() for line in file]

# Generate 10 random fantasy character names
for _ in range(10):
    # Decide gender: 0 = male, 1 = female
    gender = random.randint(0, 1)
    
    # Pick a first name based on gender
    if gender == 0:
        first_name = random.choice(male_names)
    else:
        first_name = random.choice(female_names)
    
    # Pick a random last name
    last_name = random.choice(last_names)
    
    # Print the full fantasy name
    print(first_name, last_name)
