# fruits-pygame
Worms-like game developed for the first bimester project of the ITA's object oriented programming course CES-22.

## Dependencies
This project depends on:
- [python3.6](python.org)
- [pygame](pygame.org)
- [numpy](pypi.org/project/numpy/)
- [nuitka](nuitka.net) (for compiling the executable)

## How-to run the game
To run the game, simply use `make run` into the root of the repository, this will execute the
`fruits-game.py` script. Although is already available to run, this should be used only for development purposes,
because python is too slow a great experience. For play the game, first, build the executable with
`make full-build`, that will compile the game into a executable (using the [nuitka](nuitka.net) compiler).

## Commands
- Use the arrow keys to move the selected fruit.
- Use `X` to enter launching mode.
- Use `ESC` to exit launching mode.
- Use `Q` to switch teams.
- Use `TAB` to switch fruits.
- Use `W` to go to the main menu.

