import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Block Runner')
clock = pygame.time.Clock()
score_font = pygame.font.Font('Pixeltype.ttf', 50)

sky = pygame.image.load('sky.png')
player = pygame.image.load('player.png').convert_alpha()
ground = pygame.image.load('ground.png')
ground2 = pygame.image.load('ground.png')
sun = pygame.image.load('sun.png')
cloud_2 = pygame.image.load('cloud_2.png')
cloud1_1 = pygame.image.load('cloud1_1.png')
cloud2_1 = pygame.image.load('cloud2_1.png')
small_obs = pygame.image.load('small_obs.png').convert_alpha()

x_small_obs = 800

x_cloud_2 = 390
x_cloud_22 = 1190

x_cloud1_1 = 100
x_cloud12_1 = 900

x_cloud2_1 = 550
x_cloud22_1 = 1350

xGround = 0
xGround2 = 800

score = 0

player_rect = player.get_rect(topleft=(100, 300))
small_obs_rect = small_obs.get_rect(topleft=(x_small_obs, 350))


def move_scene():
    global xGround, xGround2, x_cloud_2, x_cloud_22, x_cloud1_1, x_cloud12_1, x_cloud2_1, x_cloud22_1, x_small_obs

    if small_obs_rect.x < -50:
        small_obs_rect.x = 800

    small_obs_rect.x -= 4

    if int(x_cloud2_1) == -250:
        x_cloud2_1 = 550
        x_cloud22_1 = 1350

    x_cloud2_1 -= 0.29
    x_cloud22_1 -= 0.29

    if int(x_cloud1_1) == -700:
        x_cloud1_1 = 100
        x_cloud12_1 = 900

    x_cloud1_1 -= 0.3
    x_cloud12_1 -= 0.3

    if int(x_cloud_2) == -410:
        x_cloud_2 = 390
        x_cloud_22 = 1190

    x_cloud_2 -= 0.1
    x_cloud_22 -= 0.1

    if xGround == -800:
        xGround = 0
        xGround2 = 800

    xGround -= 4
    xGround2 -= 4


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    score += 0.05
    score_text = score_font.render('Score: ' + str(int(score)), False, 'White')

    move_scene()
    screen.blit(sky, (0, 0))
    screen.blit(sun, (600, 20))
    screen.blit(cloud_2, (x_cloud_2, 60))
    screen.blit(cloud_2, (x_cloud_22, 60))
    screen.blit(cloud1_1, (x_cloud1_1, 90))
    screen.blit(cloud1_1, (x_cloud12_1, 90))
    screen.blit(cloud2_1, (x_cloud2_1, 120))
    screen.blit(cloud2_1, (x_cloud22_1, 120))
    screen.blit(ground, (xGround, 400))
    screen.blit(ground2, (xGround2, 400))
    screen.blit(score_text, (25, 25))
    screen.blit(small_obs, small_obs_rect)
    screen.blit(player, player_rect)

    if player_rect.colliderect(small_obs_rect):
        print('yessss')

    pygame.display.update()
    clock.tick(60)
