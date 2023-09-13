from collections import namedtuple
from typing import Union

import pygame

Point = namedtuple("Point", ["x", "y"])


class Square:
    """
    A class representing a square in a game.

    Args:
        x (int, optional): The x-coordinate of the square. Defaults to 0.
        y (int, optional): The y-coordinate of the square. Defaults to 0.
        color (tuple | str, optional): The color of the square. Defaults to "black".
        center (Point, optional): The center of the square. Defaults to Point(0, 0).

    Attributes:
        SIDE_LENGTH (int): The length of each side of the square.
        BORDER_WIDTH (int): The width of the border around the square.
        TOTAL_LENGTH (int): The total length of the square including the border.
        DEFAULT_COLOR (str | tuple): The default color of the square.
    """
    SIDE_LENGTH = 10
    BORDER_WIDTH = 1
    TOTAL_LENGTH = BORDER_WIDTH * 2 + SIDE_LENGTH

    DEFAULT_COLOR = "black"

    def __init__(self,
                 x: int = None,
                 y: int = None,
                 color: tuple | str = DEFAULT_COLOR,
                 center: Point = Point(0, 0)):
        self.x = x or center.x
        self.y = y or center.y
        self.color = color

    @property
    def center(self) -> Point:
        """
        Returns:
             The center of the Square.
        """
        return Point(self.x, self.y)

    @center.setter
    def center(self, point: Union[Point, 'Square']):
        self.x = point.x
        self.y = point.y

    def draw(self, surface: pygame.Surface) -> None:
        """
        Args:
            surface (pygame.Surface): The surface on which to draw the Square.
        """
        surface.fill(self.color, (self.x * self.TOTAL_LENGTH,
                                  self.y * self.TOTAL_LENGTH,
                                  self.SIDE_LENGTH,
                                  self.SIDE_LENGTH))

    def copy(self, x=None, y=None, color=None, center=None):
        return Square(x=x,
                      y=y,
                      color=color or self.color,
                      center=center or self.center)

    def __add__(self, other: Union[Point, 'Square']):
        return Square(self.x + other.x, self.y + other.y, self.color)

    def __eq__(self, other: Union[Point, 'Square']):
        if not isinstance(other, (Square, Point)):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.center)

    def __repr__(self):
        return f"Square(x={self.x}, y={self.y}, color={self.color})"
