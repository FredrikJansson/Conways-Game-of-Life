# Conways-Game-of-Life
<h1 align="center">
	<br>
		<kbd>
  			<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif" alt="A gif demonstrating Gospers glider gun in Cellular Automata" width="250"/>
		</kbd>
  	<br>
</h1>
John-Horton Conways Game of Life is a zero-player game and a cellular automaton.

A cellular automaton consists of a regular grid of cells, each in one of a finite number of states, such as on and off (in contrast to a coupled map lattice). The grid can be in any finite number of dimensions. For each cell, a set of cells called its neighborhood is defined relative to the specified cell. An initial state (time t = 0) is selected by assigning a state for each cell. A new generation is created (advancing t by 1), according to some fixed rule (generally, a mathematical function)[3] that determines the new state of each cell in terms of the current state of the cell and the states of the cells in its neighborhood. Typically, the rule for updating the state of cells is the same for each cell and does not change over time, and is applied to the whole grid simultaneously.  
[*source*](https://en.wikipedia.org/wiki/Cellular_automaton)

## Running the application.

### Step 1. Clone or download the repository.
Clone this repository using the following commands in a terminal.
```shell
git clone https://github.com/FredrikJansson/Conways-Game-of-Life.git
```

or download the repository as a zip and extract. 

### Step 2. Run main.py using Python
Considering this is a Python file it will be ran using the prefix python/python3, however the script can be ran using two different methods.

#### Step 2.1. Ran with arguments
The script can be ran using arguments, this is done using the following format.
```shell
python main.py [width/rows] [height/columns]
```

#### Step 2.2. Ran with input
Just running the script regularly, i.e.
```
python main.py
```
will result in needing to enter the width/height (rows/columns) now.
Simply enter the number you want, and press enter.

### Step 3. Advancing generations.
Once in the game, pressing 'q' will result in the game quitting, while pressing 'enter' will advance one generation at a time.
It can be held for rapidly advancing generations.

The script will not detect when it's in a loop. So if the game is at its end and repeating, you will manually have to quit. 
