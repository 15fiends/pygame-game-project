# Snake Chaos

This is my snake game project made with Python and Pygame. I started with the basic idea of Snake and then added different fruit types to make the game more interesting and less predictable.

## How to play

The goal is to move the snake around the screen, eat fruit, and keep increasing your score without losing.

### Controls

- `W` moves up
- `A` moves left
- `S` moves down
- `D` moves right
- `R` restarts the game after game over

### Fruit types

- Red fruit is normal fruit and makes the snake grow
- Yellow fruit is speed fruit and makes the snake grow while also speeding up the game
- Purple fruit is danger fruit and makes the snake shrink
- If the snake is only length 1 and hits danger fruit, the game ends

The score is based on the snake's length.

## What makes this game different

The main twist in my game is that not every fruit helps the player in the same way. Some fruit is helpful, some makes the game more difficult, and some can actually hurt you. I wanted the game to feel a little less predictable than a normal snake game.

## Code organization

- `src/main.py` contains the main playable version of the game
- `Food` handles the fruit types, colors, and spawn positions
- `reset_game()` resets the snake, direction, foods, speed, and game over state
- The main loop handles player input, movement, collisions, score updates, drawing, and restarting
- `dist/main.py` is an extra file from earlier work in the project
- `.vscode/settings.json` keeps GitDoc enabled for the class requirement

## Assets

This version of the game does not use separate asset files like images, sprite sheets, or sound effects. The snake, fruit, border, and text are all drawn directly in Pygame using shapes, colors, and built-in text rendering.

## Problems I ran into

One of the biggest problems I had was with the scoring logic. At one point, every time I ate a fruit, the score went up by 2 instead of 1. I figured out that the snake length was being updated in the wrong order, so the game was basically counting extra length when it should not have.

I also had a problem where the danger fruit was not working correctly when the snake was very short. To figure these issues out, I went through the game loop step by step and checked when the snake head was added, when the tail was removed, and when the fruit collision was being processed. Once I fixed the order of those updates, the score and danger fruit started working the way they were supposed to.

## What I learned

This project helped me understand game loops, collision logic, and how small logic mistakes can create bigger gameplay problems. It also helped me practice using GitHub to track changes to my project.

## Next steps

If I keep working on this project, I would want to:

- improve the graphics
- add sound effects
- add a start screen
- add a high score system
- keep testing and polishing the gameplay

## How to run the game

Make sure Python and Pygame are installed, then run:

```bash
python3 src/main.py
```
