# bad-AI-game-solver
A badly made AI to find an optimal solution to a idle type game

needed the matplotlib library

i define a class and it has a weight and it picks a random number every tick between 0-1, if its above the weight it buys the most expensive thing
(increasting money earned per tick) if its below it will save its money for next turn.

it runs the 1000 Ai's untill they all have completed the game, then sort them by the lowest number of ticks (fastest to complete game)
then kills any that have a position > 1000.

it then randomly kicks out 1/2 and the probabliity of being kicked is (1 - ((position-1) / 1000)).

this means that it roughly splits the Ai's in 1/2 and then for each of them creates a copy with slighty adjusted weights then re-runs the AI's
