# Download & unzip

![Download Archive](https://raw.githubusercontent.com/MrKekovich/Snake/master/images/download_zip.png "a title")

---
# Installation:
### 1. You need python: https://www.python.org/downloads/ (tick the "Add python.exe to PATH")

### 2. Open directory with console/terminal (replace "path/to/Snake" with an actual path):
```bash
cd "path/to/Snake"
```
### 3. install requirements:
```bash
pip install -r requirements.txt
```
---
# Setup:
open [settings.env](settings.env) and set settings as you like.
### default settings:
```dotenv
SIDE_LENGTH=10
BORDER_WIDTH=2

SNAKE_BODY_COLOR=(0,255,0)
SNAKE_HEAD_COLOR=(0,150,0)

SPEED=10
FOOD_AMOUNT=3
RANDOM_INITIAL_POSITION=True
RANDOM_INITIAL_DIRECTION=True
BACKGROUND_COLOR=(0,0,0)
FOOD_COLOR=(255,255,255)
WIDTH=40
HEIGHT=30
```
1. Side length: the length side of the single square
2. Border width: the width of the border
3. Snake body color: the color of the snake body (RGB format)
4. Snake head color: the color of the snake head (RGB format)
5. Speed: the game framerate. -1 for unlimited
6. Food amount: how much food to spawn.
7. Random initial position: if True, the snake will spawn in a random position. If False, the snake will spawn in the center of the screen.
8. Random initial direction: if True, the snake will spawn in a random direction. If False, the snake will spawn in the direction "up".
9. Background color: the color of the background (RGB format)
10. Food color: the color of the food (RGB format)
11. Width: the width of the screen (1 unit = `BORDER_WIDTH * 2 + SIDE_LENGTH`)
12. Height: the height of the screen (1 unit = `BORDER_WIDTH * 2 + SIDE_LENGTH`)

---
# Run the game:
for Windows:
```bash
python snake_game.py
```
for Linux/Mac:
```bash
python3 snake_game.py
```