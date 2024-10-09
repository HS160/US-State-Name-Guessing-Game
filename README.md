# U.S. States Game

This project is a simple educational game designed to help users learn and test their knowledge of U.S. states' locations. Players are presented with a blank map of the United States and are challenged to name all 50 states.

## Features

- Interactive game interface using Python's turtle graphics
- Keeps track of correctly guessed states
- Allows players to exit the game at any time
- Generates a CSV file of missed states for further learning

## Requirements

- Python 3.x
- pandas library
- turtle library

## How to Play

1. Run the `main.py` script
2. A window will open with a blank map of the United States
3. Enter the names of U.S. states when prompted
4. Correctly guessed states will appear on the map
5. Continue until all 50 states are guessed or type 'Exit' to end the game

## Files

- `main.py`: The main script that runs the game
- `50_states.csv`: A CSV file containing the names and coordinates of all 50 U.S. states
- `blank_states_img.gif`: An image file of the blank U.S. map

## Output

After exiting the game, a `StatestoLearn.csv` file will be generated, containing a list of any states that were not guessed correctly.

## Author

HS160

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
