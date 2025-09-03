# main.py
from RPS import player
from RPS_game import play, quincy, abbey, kris, mrugesh

# Test against each bot
print("Testing against Quincy")
play(player, quincy, 1000, verbose=False)

print("\nTesting against Abbey")
play(player, abbey, 1000, verbose=False)

print("\nTesting against Kris")
play(player, kris, 1000, verbose=False)

print("\nTesting against Mrugesh")
play(player, mrugesh, 1000, verbose=False)
