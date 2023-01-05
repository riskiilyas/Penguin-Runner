import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Penguin Runner')
clock = pygame.time.Clock()
score_font = pygame.font.Font('assets/Pixeltype.ttf', 50)
game_font = pygame.font.Font('assets/Pixeltype.ttf', 80)

play_btn = pygame.image.load('assets/play_btn.png')
sky = pygame.image.load('assets/sky.png')
player = pygame.image.load('assets/player_walk_1.png').convert_alpha()
ground = pygame.image.load('assets/ground.png')
ground2 = pygame.image.load('assets/ground.png')
sun = pygame.image.load('assets/sun.png')
cloud_2 = pygame.image.load('assets/cloud_2.png')
cloud1_1 = pygame.image.load('assets/cloud1_1.png')
cloud2_1 = pygame.image.load('assets/cloud2_1.png')
small_obs = pygame.image.load('assets/small_obs.png').convert_alpha()

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

player_rect = player.get_rect(topleft=(50, 320))
small_obs_rect = small_obs.get_rect(topleft=(x_small_obs, 350))

is_sliding = False

# 1 = INITIAL
# 2 = PLAYING
# 3 = GAME OVER
GAME_STATE = 1


def move_scene():
    global xGround, xGround2, x_cloud_2, x_cloud_22, x_cloud1_1, x_cloud12_1, x_cloud2_1, x_cloud22_1, x_small_obs

    if small_obs_rect.x < -50:
        small_obs_rect.x = 800

    if GAME_STATE == 2:
        small_obs_rect.x -= 10

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

    if xGround <= -800:
        xGround = 0
        xGround2 = 800

    xGround -= 10
    xGround2 -= 10


def start_play():
    global jump_count, gravity, jump_speed, delay_double_jump, delay_run, run_index, score, player_rect
    jump_count = 0
    gravity = 0
    jump_speed = 10
    delay_double_jump = 100
    delay_run = 6
    run_index = 0
    score = 0
    small_obs_rect.x = 800
    player_rect = player.get_rect(topleft=(50, 320))


jump_count = 0
gravity = 0
jump_speed = 10
delay_double_jump = 100
delay_run = 6
run_index = 0

while True:
    if GAME_STATE < 3:
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
    screen.blit(player, player_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and GAME_STATE == 2:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if jump_count < 2 and not is_sliding:
                    jump_count += 1
                    jump_speed = 10
                    gravity = 0
                    if jump_count == 2:
                        delay_double_jump = 50
                        player = pygame.image.load('assets/player_double_jump.png').convert_alpha()
                    else:
                        player = pygame.image.load('assets/player_jump.png').convert_alpha()

            if event.key == pygame.K_DOWN:
                is_sliding = True
                player = pygame.image.load('assets/player_slide.png').convert_alpha()
                player_rect = player.get_rect(topleft=(50, 350 if jump_count == 0 else player_rect.y))

        if event.type == pygame.KEYUP and GAME_STATE == 2:
            if is_sliding:
                player = pygame.image.load('assets/player_walk_1.png').convert_alpha()
                player_rect = player.get_rect(topleft=(50, 350 if jump_count == 0 else player_rect.y))
                is_sliding = False

    if GAME_STATE == 2:
        if jump_count > 0 & jump_count <= 2:
            gravity += 0.05
            if is_sliding:
                gravity += 0.25
            jump_speed -= gravity
            player_rect.y -= jump_speed

            if jump_speed < 0 and not is_sliding:
                player = pygame.image.load('assets/player_fall.png').convert_alpha()

        if player_rect.y > 320 and not is_sliding:
            player_rect.y = 320
            jump_speed = 0
            gravity = 0
            jump_count = 0
            player = pygame.image.load('assets/player_walk_1.png').convert_alpha()

        if player_rect.y > 350 and is_sliding:
            player_rect.y = 350
            jump_speed = 0
            gravity = 0
            jump_count = 0

        score += 0.1
        score_text = score_font.render('Score: ' + str(int(score)), False, 'White')

        if delay_double_jump != 0 and jump_count == 2:
            delay_double_jump -= 1
            if delay_double_jump == 0:
                player = pygame.image.load('assets/player_jump.png').convert_alpha()

        if player_rect.colliderect(small_obs_rect):
            GAME_STATE = 3
            player = pygame.image.load('assets/player_over.png').convert_alpha()
            is_sliding = False
            jump_count = 0

        screen.blit(score_text, (25, 25))

    if GAME_STATE != 1:
        screen.blit(small_obs, small_obs_rect)

    if GAME_STATE < 3:
        if not is_sliding and jump_count == 0:
            delay_run -= 1
        if delay_run == 0:
            player = pygame.image.load('assets/player_walk_' + str((run_index % 4) + 1) + '.png').convert_alpha()
            run_index += 1
            delay_run = 6

    if GAME_STATE == 1:
        play_text = score_font.render('Click to Start', False, 'White')
        play_text_rect = play_text.get_rect(midtop=(400, 250))

        play_text2 = game_font.render('Penguin Runner', False, 'White')
        play_text_rect2 = play_text2.get_rect(midtop=(400, 50))

        play_text3 = score_font.render('by Riski :)', False, 'White')
        play_text_rect3 = play_text3.get_rect(midtop=(400, 100))
        play_btn_rect = play_btn.get_rect(midtop=(400, 180))

        if play_btn_rect.collidepoint(pygame.mouse.get_pos()):
            play_btn_rect = play_btn.get_rect(midtop=(400, 170))
            if pygame.mouse.get_pressed()[0]:
                start_play()
                GAME_STATE = 2

        screen.blit(play_text, play_text_rect)
        screen.blit(play_text2, play_text_rect2)
        screen.blit(play_text3, play_text_rect3)
        screen.blit(play_btn, play_btn_rect)

    if GAME_STATE == 3:
        play_text = score_font.render('Click to Restart', False, 'White')
        play_text_rect = play_text.get_rect(midtop=(400, 250))

        play_text2 = game_font.render('Game Over', False, 'White')
        play_text_rect2 = play_text2.get_rect(midtop=(400, 50))

        play_text3 = score_font.render('Score: ' + str(int(score)), False, 'White')
        play_text_rect3 = play_text3.get_rect(midtop=(400, 100))
        play_btn_rect = play_btn.get_rect(midtop=(400, 180))

        if play_btn_rect.collidepoint(pygame.mouse.get_pos()):
            play_btn_rect = play_btn.get_rect(midtop=(400, 170))
            if pygame.mouse.get_pressed()[0]:
                start_play()
                GAME_STATE = 2

        screen.blit(play_text, play_text_rect)
        screen.blit(play_text2, play_text_rect2)
        screen.blit(play_text3, play_text_rect3)
        screen.blit(play_btn, play_btn_rect)

    pygame.display.update()
    clock.tick(60)
