# Snake Game Project

This is my snake game made with Python and Pygame. I started with a basic snake game idea and then added different fruit types to make it more interesting.

## How the game works

The snake moves around the screen and eats fruit.

- Red fruit is normal fruit and makes the snake grow
- Yellow fruit is a speed fruit and makes the snake grow while also making the game faster
- Purple fruit is danger fruit and makes the snake shrink
- If the snake is only length 1 and hits danger fruit, the game ends

The score is based on the snake's length.

## Twist / originality

The main twist in my game is that not all fruit helps the player. Some fruit is good, some makes the game faster, and some actually hurts the player. I wanted it to feel less predictable than a normal snake game.

## Controls

- `W` = up
- `A` = left
- `S` = down
- `D` = right
- `R` = restart after game over

## Files in this project

- `src/main.py` - main game code
- `dist/main.py` - basic test file / extra file from earlier work
- `README.md` - project explanation

## What I learned

One thing I learned from this project is that small logic mistakes can cause weird problems in games. I had an issue where the score was jumping by 2 instead of 1, and the danger fruit was not working correctly when the snake was very short. Fixing that helped me understand game loops and collision logic better.

I also learned more about using GitHub to save and update my work.

## Next steps

If I keep working on this project, I would want to:

- add a start screen
- add sound effects
- improve the graphics
- maybe add levels or obstacles
- show a high score

## Demo / presentation notes

If I am showing this project, I should explain:

1. what the game is
2. how to control it
3. the different fruit types
4. what bug I fixed during development
5. what I would improve next

## How to run it

Make sure Python and Pygame are installed, then run:

```bash
python3 src/main.py
```
