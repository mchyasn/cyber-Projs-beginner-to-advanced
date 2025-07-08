import re

with open("data/output.txt", "r") as f:
    lines = f.readlines()

guesses = [line.strip() for line in lines if "[+]" in line]

print("Step-by-step password guessing:")
for i, guess in enumerate(guesses, 1):
    print(f"{i}. {guess}")
