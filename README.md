# Sudoku Console Application game.

As part of my continuous growth as a software engineer, I developed a Sudoku solver using Python to practice algorithm design, problem-solving, and software testing. The goal of this project was to build a robust, efficient solution to solve standard 9x9 Sudoku puzzles, leveraging the backtracking algorithm—a depth-first search technique commonly used in constraint satisfaction problems. 

Additionally, I wanted to integrate the ability to load Sudoku puzzles from a JSON file and output solutions in a similar format, making it easier for users to interact with the software. The project also includes a test suite to ensure the correctness of the solver.

The project demonstrates my ability to design a solution, manage input/output with JSON, and apply testing principles to validate my software.


# Development Environment

This software was developed using the following tools and technologies:

- **Programming Language**: Python 3.x
  - The main language used to implement the backtracking algorithm and solve Sudoku puzzles.
  
- **Libraries**:
  - **unittest**: Used to write unit tests for validating the functionality of the Sudoku solver.
  - **json**: The built-in Python library for reading and writing JSON files, enabling the program to load Sudoku puzzles and save solutions in a standardized format.
  
# Key Features

- **Sudoku Solver**: Implements the backtracking algorithm to solve Sudoku puzzles.
- **JSON Support**: Load Sudoku puzzles from a JSON file and output solved puzzles back into a JSON file format.
- **Testing**: A comprehensive test suite built with Python’s `unittest` framework to verify the solver’s correctness under various conditions.

# Useful Websites

Here are some resources that were helpful in the development of this project:

- [Python Documentation](https://docs.python.org/3/)
- [GeeksforGeeks - Backtracking Algorithm](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [StackOverflow - Sudoku Solver Techniques](https://stackoverflow.com/questions/ask)
- [JSON Documentation](https://www.json.org/json-en.html)

# Future Work

While the Sudoku solver is functional, there are several improvements and features I plan to add in the future:

- **Performance Optimization**: Improve the backtracking algorithm for larger Sudoku puzzles (e.g., 16x16 boards).
- **GUI Integration**: Create a graphical user interface (GUI) for a more user-friendly experience.
- **AI Integration**: Explore the possibility of integrating AI to predict and assist in solving puzzles with hints or guidance.

