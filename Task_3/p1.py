import random

def pick_winner(names_list):
    if len(names_list) == 0:
        return "The list is empty!"
    
    winner = random.choice(names_list)
    return f"Congratulations {winner}! You are the winner!"