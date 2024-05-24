# Challenge

Labirynth

# Description

If we will get nice rewards if we can get out of this labyrinth. This isn't any good old labyrinth. It changes after a couple of minutes, that means we will have to be fast; Maybe as fast as a computer....

# Solutions

The challenge tells you that you are stuck in a labyrinth. You can go up, down, left and right.
But depending on the possition you can see rooms and move to them. 

You start in the north west corner and have to move to the north east corner. Based of this knowledge we could make a graph to keep track of where we are in the labyrinth
and use depth first search algorithm to keep track of where we have been. 

In solution.py I have implemented a recursive depth search that colors nodes gray (visiting) and black if visited (no more routes to explore).
From there you can find where you are in the labyrinth and navigate through the maze. There is a time limit, but the program should be fast enough.

# Flag

ctf{just_follow_me_and_run_like_your_life_depends_on_it}
