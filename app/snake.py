import pygame

from app.square import Point, Square


class Snake:
    """
    A class representing a snake in a game.

    Args:
        initial_position (Point, optional): The initial position of the snake. Defaults to Point(0, 0).
        body_color (tuple | str, optional): The color of the snake's body. Defaults to "green".
        head_color (tuple | str, optional): The color of the snake's head. Defaults to "darkgreen".

    Attributes:
        DIRECTIONS (dict): A dictionary mapping direction names to Point objects representing the direction vectors.
        BODY_COLOR (str | tuple): The color of the snake's body.
        HEAD_COLOR (str | tuple): The color of the snake's head.
    """

    DIRECTIONS = {
        "UP": Point(0, -1),
        "DOWN": Point(0, 1),
        "LEFT": Point(-1, 0),
        "RIGHT": Point(1, 0)
    }

    BODY_COLOR = "darkgreen"
    HEAD_COLOR = "green"

    def __init__(self,
                 initial_position: Point = Point(0, 0),
                 body_color: tuple | str = None,
                 head_color: tuple | str = None):
        self.body_color = body_color or self.BODY_COLOR
        self.head_color = head_color or self.HEAD_COLOR

        self.head = Square(center=initial_position, color=self.head_color)
        self.body: list[Square] = []

        self.score = 0

    def move(self, direction: str):
        self.body.append(self.head.copy(color=self.body_color))
        self.head += Snake.DIRECTIONS[direction]

    def shrink(self):
        if len(self.body) > 0:
            del self.body[0]

    def draw(self, surface: pygame.Surface):
        for square in self.body + [self.head]:
            square.draw(surface)

    def __repr__(self):
        return (f"Snake(head={self.head}, "
                f"body={self.body}, "
                f"score={self.score}, "
                f"body_color={self.body_color}, "
                f"head_color={self.head_color})")
