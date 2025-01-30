SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# Player properties

player_width = 50
player_height = 50
player_x = 100
player_y = SCREEN_HEIGHT - player_height - 10
player_vel_y = 0
player_jump = False
player_image_path = "player.png"



# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - obstacle_height - 10
obstacle_speed = 10
obstacle_image_path = "obstacle.png"