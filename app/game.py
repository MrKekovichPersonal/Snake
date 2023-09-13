import random

import pygame

from app.snake import Snake
from app.square import Square, Point


class Game:
    HEIGHT = 30
    WIDTH = 40

    DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]
    OPPOSITE_DIRECTIONS = {
        "UP": "DOWN",
        "DOWN": "UP",
        "LEFT": "RIGHT",
        "RIGHT": "LEFT"
    }
    KEY_MAPPING = {
        pygame.K_UP: "UP",
        pygame.K_DOWN: "DOWN",
        pygame.K_LEFT: "LEFT",
        pygame.K_RIGHT: "RIGHT",
    }

    BACKGROUND_COLOR = "black"
    FOOD_COLOR = "red"

    def __init__(self,
                 speed: int = 10,
                 food_amount: int = 3,
                 random_initial_position: bool = True,
                 random_initial_direction: bool = True,
                 snake_body_color: tuple = None,
                 snake_head_color: tuple = None,
                 background_color: tuple = BACKGROUND_COLOR,
                 food_color: tuple = FOOD_COLOR,
                 width: int = WIDTH,
                 height: int = HEIGHT):
        # Screen settings
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Color settings
        self.snake_body_color = snake_body_color
        self.snake_head_color = snake_head_color
        self.background_color = background_color
        self.food_color = food_color

        # Game settings
        self.speed = speed
        self._clock = pygame.time.Clock()
        self.food_amount = food_amount
        self.food_squares: list[Square] = []
        self.random_initial_position = random_initial_position
        self.random_initial_direction = random_initial_direction

        self._direction = None
        self.snake = None
        self.reset()

    @property
    def screen_width(self) -> int:
        return self.width * Square.TOTAL_LENGTH

    @property
    def screen_height(self) -> int:
        return self.height * Square.TOTAL_LENGTH

    @property
    def get_initial_position(self) -> Point:
        return (Point(random.randint(0, self.width - 1),
                      random.randint(0, self.height - 1)) if self.random_initial_position
                else Point(0, 0))

    @property
    def get_initial_direction(self) -> str:
        return (random.choice(self.DIRECTIONS)
                if self.random_initial_direction
                else self.DIRECTIONS[0])

    def run(self):
        while True:
            self.update()

    def update(self) -> None:
        self._clock.tick(self.speed)
        self._handle_events()
        self._handle_snake()
        self._draw()

    def _handle_snake(self):
        self.snake.move(self.direction)
        if (self.snake.head in self.snake.body
                or self.snake.head.x not in range(self.width)
                or self.snake.head.y not in range(self.height)):
            print(f"Game Over. Score: {self.snake.score}")
            self.reset()
        elif self.snake.head in self.food_squares:
            self.food_squares.remove(self.snake.head)
            self.generate_food()
            self.snake.score += 1
        else:
            self.snake.shrink()

    def reset(self):
        self.snake = Snake(initial_position=self.get_initial_position,
                           body_color=self.snake_body_color,
                           head_color=self.snake_head_color)
        self._direction = self.get_initial_direction
        self.food_squares = []
        self.generate_food(self.food_amount)

    @property
    def direction(self) -> str:
        """
        Returns:
            The current direction of the snake.
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str) -> None:
        assert direction in self.DIRECTIONS, f"Invalid direction: {direction}: {type(direction)}"
        if direction != self.OPPOSITE_DIRECTIONS[self._direction]:
            self._direction = direction

    def generate_food(self, amount: int = 1) -> None:
        for _ in range(amount):
            for _ in range(1000):
                # Try to generate a new food square for 1000 times
                new_food = (Square(random.randint(0, self.width - 1),
                                   random.randint(0, self.height - 1),
                                   self.food_color))

                if not (new_food in self.food_squares
                        or new_food == self.snake.head
                        or new_food == self.snake.body):
                    # If new is not inside any of above
                    self.food_squares.append(new_food)
                    break

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in self.KEY_MAPPING:
                    self.direction = self.KEY_MAPPING[event.key]

    def _draw(self) -> None:
        self.screen.fill(self.background_color)
        for square in self.food_squares:
            square.draw(self.screen)
        self.snake.draw(self.screen)
        pygame.display.update()
