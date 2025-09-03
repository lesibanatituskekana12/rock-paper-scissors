# RPS.py
import random

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # If we don’t have enough history, play random
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    # --- Strategy for Quincy ---
    quincy_pattern = ["R", "P", "S"]
    if opponent_history[-3:] == quincy_pattern[:3]:
        next_move = quincy_pattern[len(opponent_history) % 3]
        return counter_move(next_move)

    # --- Strategy for Abbey ---
    if len(opponent_history) > 1:
        abbey_prediction = counter_move(opponent_history[-1])
        return counter_move(abbey_prediction)

    # --- Strategy for Kris ---
    if len(opponent_history) > 1:
        my_last_move = predict_my_last_move(opponent_history)
        return counter_move(my_last_move)

    # --- Strategy for Mrugesh ---
    counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        counts[move] += 1
    most_common = max(counts, key=counts.get)
    return counter_move(most_common)

def counter_move(move):
    if move == "R":
        return "P"
    if move == "P":
        return "S"
    if move == "S":
        return "R"

def predict_my_last_move(opponent_history):
    if len(opponent_history) < 2:
        return "R"
    return counter_move(opponent_history[-2])
