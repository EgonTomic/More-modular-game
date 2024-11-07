import datetime
import json
import random

# Easy part
def get_top_scores_easy():
    with open("score_list_easy.json", "r") as score_file_easy:
        return json.loads(score_file_easy.read())

def save_scores_easy(score_list_easy):
    with open("score_list_easy.json", "w") as score_file_easy:
        score_file_easy.write(json.dumps(score_list_easy))

# Hard part
def get_top_scores_hard():
    with open("score_list_hard.json", "r") as score_file_hard:
        return json.loads(score_file_hard.read())
    
def save_scores_hard(score_list_hard):
    with open("score_list_hard.json", "w") as score_file_hard:
        score_file_hard.write(json.dumps(score_list_hard))

def play_game_easy():
    secret = random.randint(1, 30)
    attempts = 0
    score_list_easy = get_top_scores_easy()

    print("Top scores of easy mode: " + str(score_list_easy))
    for score_dict in score_list_easy:
        print(str(score_dict["attempts"]) + " attempts, date: " + score_dict["date"])
    while True:
        guess = int(input("Guess the secret number between 1 and 30: "))
        attempts = attempts + 1
    
        if guess == secret:
            score_list_easy.append({"attempts": attempts, "date": str(datetime.datetime.now())})

            with open("score_list_easy.json", "w") as score_file:
                score_file.write(json.dumps(score_list_easy))

            print("You have past it. It is number: " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct. Try something smaller")
        elif guess < secret:
            print("Your guess is not correct. Try something bigger")

def play_game_hard():
    secret = random.randint(1, 30)
    attempts = 0
    score_list_hard = get_top_scores_hard()

    print("Top scores of hard mode: " + str(score_list_hard))
    for score_dict in score_list_hard:
        print(str(score_dict["attempts"]) + " attempts, date: " + score_dict["date"])
    while True:
        guess = int(input("Guess the secret number between 1 and 30: "))
        attempts = attempts + 1
    
        if guess == secret:
            score_list_hard.append({"attempts": attempts, "date": str(datetime.datetime.now())})

            with open("score_list_hard.json", "w") as score_file:
                score_file.write(json.dumps(score_list_hard))

            print("You have past it. It is number: " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess != secret:
            print("Your guess is not correct. Try again")