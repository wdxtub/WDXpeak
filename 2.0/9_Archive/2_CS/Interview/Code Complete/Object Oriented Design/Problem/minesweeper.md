# Minesweeper

Design and implement a text-based Minesweeper game. Minesweeper is the classic single-player computer game where an NxN grid has B mines (or bombs) hidden across the grid. The remaining cells are either blank or have a number behind them. The numbers reflect the number of bombs in the surrounding eight cells. The user then uncovers a cell. If it is a bomb, the player loses. If it is a number, the number is exposed. If it is a blank cell, this cell and all adjacent blank cells (up to and including the surrounding numeric cells) are exposed. The player wins when all non0bomb cells are exposed. The player can also flag certain places as potential bombs. This doesn't affect game play, other than to block the user from accidentally clicking a cell that is thought to have a bomb.

## Solution

Generating the grid is simple. There are a couple simple algorithms that you need when executing the player's move, to determine which squares to open up and whether they have lost or won. 

Generating the grid 

The simplest algorithm is to place all of the mines randomly. (ensure you don't overlap them) 

Problem: The player's first click might be a mine. 

Improvement: Delay the generation of the grid until the user clicks on the first square, and don't put any mines in that square. 

Problem: The player's first click might reveal a non-zero number, and they will be forced to click randomly until something opens up. 

Improvement: Don't generate any mines in the (up to) eight squares around the first click, either. 

Problem: The player might be forced to guess at some point, making this a sad excuse for a logic puzzle.

Improvement: Run the solver alongside the generator, making sure that the puzzle has a unique solution. This takes some cleverness, and isn't done in most variants. 

Another, less common way to resolve ambiguities is to detect when the player knows they are choosing between equally likely possibilities and "collapse the waveform" into the position they decided on. I have never seen this in action, but it would be kind of fun. 

Playing the game 

Besides marking flags, the player can make two kinds of moves to attempt to uncover squares: 

Single guess: The player clicks on a square with unknown state and no flag. Reveal the square, see if the player died, and put a number in it. If the square contains a 0, repeat this recursively for all the surrounding squares. This should be in a dedicated function, to separate it from the GUI's event handler, to make the recursion easy, and because it's reused in the multiguess. 

Multiguess: The player clicks on a square that is uncovered and known to be safe. If the number of flags surrounding equals the number in this square, we open up the unflagged squares using the same procedure as above. 

Winning the game 

If the number of squares that are covered up is the same as the number of mines, then the player has won, even if they haven't placed a flag on every square. 

When the player loses, it is customary to mark any incorrect guesses that they made, the remaining mines, and the mine that they stepped on.

---

In a minesweeper game, if we want to think of the game from the OOP point of view, we can consider each region as an object. We will call this object a 'zone', and all of the game zones will be in a container object that we will call the 'board'.

For every zone object, there is a bunch of properties like:

+ state: whether it contains a mine or not.
+ revealed: if it's revealed, the user has opened the zone.
+ marked: whether the user has marked the zone as containing a mine.
+ zoneValue: the number written inside the zone representing the number of mines in the surrounding zones.
+ xcor: the horizontal position of the zone in the board.
+ ycor: the vertical position of the zone in the board.

And that's how we will build the game. there will be a Zone class linked with a zone movie clip in the library, and we will instantiate the amount of zones we need from our main class to make the game board.

