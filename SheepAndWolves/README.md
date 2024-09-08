# Sheep and Wolves Problem Solver

This Python program implements an agent using breadth-first search (BFS) to solve the classic Sheep and Wolves problem.

# Overview

The Sheep and Wolves problem involves safely transporting a group of sheep and wolves across a river using a boat that can only carry a limited number of animals at a time. Wolves cannot outnumber sheep on either side of the river.

**Key **Components****

**SemanticNetsAgent.py:** This file contains the core logic for solving the Sheep and Wolves problem.

**SemanticNetsAgent:** Class that implements the BFS algorithm to find a solution.

**__init__(self): **Initializes the agent.

**solve(self, initial_sheep, initial_wolves):** Solves the problem and returns a list of moves as the solution, or an empty list if no solution exists.

**test_SemanticNetsAgent.py**: This file contains unit tests to ensure the functionality of the SemanticNetsAgent class.

**main.py:** This file provides an interface for users to interact with the solver.
Running the Unit Tests

**HOW TO EXECUTE**

Save the files (SemanticNetsAgent.py, test_SemanticNetsAgent.py, and main.py) in the same directory.

Open a terminal and navigate to the directory where you saved the files.

# Run the unit tests 

Use the following command:


```
python test_SemanticNetsAgent.py
```

This will execute the unit tests and report the results.



# Running the Solver

Make sure you have Python installed on your system.

Navigate to the directory where you saved the files.

Run the solver using the following command:

```

python main.py
```


The script will prompt you to enter the initial number of sheep and wolves.

The script will attempt to find a solution and print the steps, or display a message indicating no solution exists.

# Additional Notes

This implementation uses breadth-first search (BFS) to explore all possible states to find the shortest solution.

The code includes comments to explain the logic behind the SemanticNetsAgent class and its methods.

Unit tests provide a safety net to ensure the solver works as expected.