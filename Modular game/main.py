from game import *

def main_menu():
    while True:
        selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")
        
        if selection.upper() == "A":
            selection_level = input("Would like to play or A) hard mode, B) easy mode? ")
            if selection_level.upper() == "B":
                score_list_easy = get_top_scores_easy()
                for score_dict in score_list_easy:
                    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
                play_game_easy()
            elif selection_level.upper() == "A":
                score_list_hard = get_top_scores_hard()
                for score_dict in score_list_hard:
                    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
                play_game_hard()
        elif selection.upper() == "B":
            selection_level_scores = input("Would like to see best scores of A) hard mode, B) easy mode? ")
            if selection_level_scores.upper() == "B":
                score_list_easy = get_top_scores_easy()
                for score_dict_easy in score_list_easy:
                    print(str(score_dict_easy["attempts"]) + " attempts, date: " + score_dict_easy.get("date"))
            elif selection_level_scores.upper() == "A":
                score_list_hard = get_top_scores_hard()
                for score_dict_hard in score_list_hard:
                    print(str(score_dict_hard["attempts"]) + " attempts, date: " + score_dict_hard.get("date"))
        elif selection.upper() == "C":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose A, B, or C.")

main_menu()