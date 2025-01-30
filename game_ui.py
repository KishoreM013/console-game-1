from utilities import *
import pygame


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Jump Game")

background = pygame.image.load("background.jpg")
player_image = pygame.image.load(player_image_path)
obstacle_image = pygame.image.load(obstacle_image_path)


clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player_jump:
                player_vel_y = -15
                player_jump = True

    player_y += player_vel_y
    player_vel_y += 1  

    if player_y >= SCREEN_HEIGHT - player_height - 10:
        player_y = SCREEN_HEIGHT - player_height - 10
        player_jump = False

    obstacle_x -= obstacle_speed
    if obstacle_x < 0:
        obstacle_x = SCREEN_WIDTH
        obstacle_y = SCREEN_HEIGHT - obstacle_height - 10

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if player_rect.colliderect(obstacle_rect):
        print("Oh no the game is over ...... aaaaaah!")
        running = False

    screen.blit(background, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))
    
    pygame.display.update()
    # fps
    clock.tick(50)

pygame.quit()