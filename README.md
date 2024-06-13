# Sierpinski
This program generates Sierpinski graphs associated to the Tower of Hanoi game. **You can customize the amount of disks** (and the number of tower) **by calling the function ```generer``` with the two numbers as arguments respectively.** For example, you obtain a graph for 3 disks and 4 towers by calling ```generer(3, 4)```.

## Tower of Hanoi
Tower of Hanoi is a game mostly known as three disks, placed by ascendant sizes on a column, that you have to move to a third column by swapping them from column to column (three total columns available) *while always keeping heavier disks under lighter ones*.

## Two files
The main file is written recursively which makes it usable for any parameter. To use it, run the ```generer``` command (```generer(n: int = 3, colonnes: int = 3)```, n is the number of disks), it outputs a dictionary explained below.
The second file has a more understandable approach but much harder to generalize with more disks or columns. It outputs the same kind of object as the main function.

## Output
The output is a dictionary where each key is an object and each value is a list of every object it is linked to.

## Encoding on the graph
An object of the graph is a set of n letters, n being the number of disks. By ranking the disks by weight, **the #k letter corresponds to the column where the #k disk is**. A branch represents one (legal) move.
*The fastest solve is the shortest path from 'AA..A' to '&&..&' where '&' is the last column.*
