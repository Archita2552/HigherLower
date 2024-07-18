import art
from game_data import data
import random

print(art.logo)

score = 0
account_b=random.choice(data)
def get_choice(a_follower_count, b_follower_count, user_choice):
    if user_choice == 'a':
        return a_follower_count > b_follower_count
    else:
        return b_follower_count > a_follower_count

Game_is_over = True

while Game_is_over:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    
    a_name = account_a["name"]
    a_description = account_a["description"]
    a_country = account_a["country"]
    
    b_name = account_b["name"]
    b_description = account_b["description"]
    b_country = account_b["country"]
    
    print(f"Compare A: {a_name}, {a_description}, from {a_country}")
    print(art.vs)
    print(f"Against B: {b_name}, {b_description}, from {b_country}")
    
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    user_choice = input("Type 'A' OR 'B' which has more followers: ").lower()
    is_correct = get_choice(a_follower_count, b_follower_count, user_choice)
    
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        Game_is_over = False
        print(f"You are wrong! Your score is: {score}")
