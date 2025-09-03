# RPS_game.py
import random

# Bot definitions
def quincy(prev_play, opponent_history=[]):
    # Cycles R -> P -> S
    if prev_play == "":
        return "R"
    cycle = ["R", "P", "S"]
    return cycle[(cycle.index(prev_play) + 1) % 3]

def abbey(prev_play, opponent_history=[]):
    # Counters opponent's last move
    if prev_play == "":
        return "R"
    return counter_move(prev_play)

def kris(prev_play, opponent_history=[]):
    # Mimics opponent's last move
    if prev_play == "":
        return "R"
    return prev_play

def mrugesh(prev_play, opponent_history=[]):
    # Plays what opponent played most frequently
    if prev_play == "":
        return "R"
    counts = {"R":0, "P":0, "S":0}
    for move in opponent_history:
        counts[move] += 1
    most_common = max(counts, key=counts.get)
    return counter_move(most_common)

# Helper to counter moves
def counter_move(move):
    if move == "R": return "P"
    if move == "P": return "S"
    if move == "S": return "R"

# Game logic
def play(player1, player2, num_games=1000, verbose=False):
    history1 = []
    history2 = []
    score1 = 0
    score2 = 0
    for _ in range(num_games):
        move1 = player1(history2[-1] if history2 else "")
        move2 = player2(history1[-1] if history1 else "")
        history1.append(move1)
        history2.append(move2)

        # Determine winner
        if move1 == move2:
            winner = 0
        elif (move1=="R" and move2=="S") or (move1=="P" and move2=="R") or (move1=="S" and move2=="P"):
            score1 += 1
            winner = 1
        else:
            score2 += 1
            winner = 2

        if verbose:
            print(f"{move1} vs {move2} -> Winner: {winner}")

    print(f"Final Score -> Player1: {score1} | Player2: {score2} | Draws: {num_games - score1 - score2}")
    win_rate = score1 / num_games * 100
    print(f"Player1 Win Rate: {win_rate:.2f}%")
    return score1, score2
