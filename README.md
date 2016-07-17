# python_oops_rover_problem
Implementation of famous mars rover problem in python

Mars Rovers puzzle

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth. A rover's position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North. In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

INPUT:

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau. The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

OUTPUT:

The output for each rover should be its final co-ordinates and heading.

INPUT AND OUTPUT:

Test Input:

5 5

1 2 N

LMLMLMLMM

3 3 E

MMRMMRMRRM

Expected Output:

1 3 N

5 1 E

# How to use this file?

Clone this repository and run >>python robot_problem.py

You will be getting command prompt like
**INPUT**

>> Enter the grid length **5**

>> Enter the grid breadth **5**

>> Grid is created

>> Enter how many rovers u need **2**

>> Enter the x coordinates of Rover **1**

>> Enter the y coordinates of Rover **2**

>> Enter the facing direction of Rover **N**

>> Enter the x coordinates of Rover **3** 

>> Enter the y coordinates of Rover **3**

>> Enter the facing direction of Rover **E**

>> Enter the input_string for rover 1 to go **LMLMLMLMM**

**RESPONSE**

>> Rover x coordinate is 1, y_coordinate is 2,facing is west

>> Rover x coordinate is 0, y_coordinate is 2,facing is west

>> Rover x coordinate is 0, y_coordinate is 2,facing is south

>> Rover x coordinate is 0, y_coordinate is 1,facing is south

>> Rover x coordinate is 0, y_coordinate is 1,facing is east

>> Rover x coordinate is 1, y_coordinate is 1,facing is east

>> Rover x coordinate is 1, y_coordinate is 1,facing is north

>> Rover x coordinate is 1, y_coordinate is 2,facing is north

>> Rover x coordinate is 1, y_coordinate is 3,facing is north

>> Enter the input_string for rover 2 to go **MMRMMRMRRM**

**RESPONSE**

Rover x coordinate is 4, y_coordinate is 3,facing is east

Rover x coordinate is 5, y_coordinate is 3,facing is east

Rover x coordinate is 5, y_coordinate is 3,facing is south

Rover x coordinate is 5, y_coordinate is 2,facing is south

Rover x coordinate is 5, y_coordinate is 1,facing is south

Rover x coordinate is 5, y_coordinate is 1,facing is west

Rover x coordinate is 4, y_coordinate is 1,facing is west

Rover x coordinate is 4, y_coordinate is 1,facing is north

Rover x coordinate is 4, y_coordinate is 1,facing is east

Rover x coordinate is 5, y_coordinate is 1,facing is east
