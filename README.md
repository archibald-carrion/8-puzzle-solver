# 8-puzzle-solver
## Description
This project is a simple 8-puzzle solver that uses mutlitple algorithms to solve the 8-puzzle problem. Beside the solving algorithms, the project also includes a GUI that allow the user to choose for a few given puzzles and an option to verify if a given puzzle is solvable or not. The algorithms implemented are:
- Breadth First Search
- Greedy Search
- Depth First Search
- IDS* Search

## How to run
To run the project, you need to have python installed in your machine. The project was developed using python 3, and the GUI was made using Custom TKInter graphic library. To run the project, you need to run the following command in the root folder of the project:
```
./app.bat
```
or
```
python main.py
```
Note that the project was developed in a Windows machine, so the command to run the project may vary depending on the OS you are using.
The advantage of using the .bat file is that it will check if the necessary libraries and other dependencies are installed in your machine, and if not, it will install them for you.

## Code dependencies
The project uses the following libraries:
- psutil wich can be installed using the following command:
```
pip install psutil
```
- Custom TKInter wich can be installed using the following command:
```
pip install customtkinter==0.3
```

## Current implementation and future improvements
The project is still in development, and there are a few improvements that can be made. Here is a list of the current features and futures improvements:
- [x] Breadth First Search algorithm
- [x] Greedy Search algorithm
- [x] Depth First Search algorithm
- [x] IDS* Search algorithm
- [x] user friendly GUI
- [x] Allow user to input a custom puzzle and solve it
- [ ] Add a log to the UI to display the time and space complexity
- [ ] Display in the UI log the time taken to solve the puzzle
- [ ] Display in the UI log the quantity of memory used to solve the puzzle
- [ ] Implement A* Search algorithm
