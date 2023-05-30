# Grid Paths

Consider an n×n grid whose squares may have traps. It is not allowed to move to a square with a trap.

Your task is to calculate the number of paths from the upper-left square to the lower-right square. You can only move right or down.

Input

The first input line has an integer n : the size of the grid.

After this, there are n lines that describe the grid. Each line has n characters: "." denotes an empty cell, and * denotes a trap.

Output

Print the number of paths modulo 109+7


Constraints
1≤n≤1000

Example

Input:
4
....
.*..
...*
*...

Output:
3