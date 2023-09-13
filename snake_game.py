import os

from dotenv import load_dotenv

from app.game import Game

if __name__ == '__main__':
    # Load environment variables
    load_dotenv("settings.env")
    try:
        speed = int(os.getenv('SPEED', '10'))
        food_amount = int(os.getenv('FOOD_AMOUNT', '3'))
        random_initial_position = bool(os.getenv('RANDOM_INITIAL_POSITION', 'True'))
        random_initial_direction = bool(os.getenv('RANDOM_INITIAL_DIRECTION', 'True'))
        snake_body_color = tuple(map(int,
                                     os.getenv('SNAKE_BODY_COLOR', '0,255,0').split(',')))
        snake_head_color = tuple(map(int,
                                     os.getenv('SNAKE_HEAD_COLOR', '0,150,0').split(',')))
        background_color = tuple(map(int,
                                     os.getenv('BACKGROUND_COLOR', '0,0,0').split(',')))
        food_color = tuple(map(int,
                               os.getenv('FOOD_COLOR', '255,0,0').split(',')))
        width = int(os.getenv('WIDTH', '40'))
        height = int(os.getenv('HEIGHT', '30'))
        game = Game(speed=speed,
                    food_amount=food_amount,
                    random_initial_position=random_initial_position,
                    random_initial_direction=random_initial_direction,
                    snake_body_color=snake_body_color,
                    snake_head_color=snake_head_color,
                    background_color=background_color,
                    food_color=food_color,
                    width=width,
                    height=height)
    except ValueError as e:
        print(f"Invalid environment variables:\n {e}")
        print("Using default values")
        game = Game()

    game.run()
