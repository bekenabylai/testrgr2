import pygame, random

pygame.init()

# variables and constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
HEADER_HEIGHT = 80

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)

BUFFER_DISTANCE = 100
PLAYER_STARTING_SCORE = 0
PLAYER_STARTING_LIVE = 5
GHOSTPCK_STARTING_VELOCITY = 5
BLUEGHOSTPACMAN_STARTING_VELOCITY = 7
YELLOWGHOSTPACMAN_STARTING_VELOCITY = 9

player_score = PLAYER_STARTING_SCORE
player_live = PLAYER_STARTING_LIVE
packman_velocity = 5
ghostpck_velocity = GHOSTPCK_STARTING_VELOCITY
blueghostpacman_velocity = BLUEGHOSTPACMAN_STARTING_VELOCITY
yellowghostpacman_velocity = YELLOWGHOSTPACMAN_STARTING_VELOCITY
acceleration = 0.5

# main surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hungry Pacman")

# images
background = pygame.image.load('SPACE.jpg')

score_backround = pygame.image.load('score_background.png').convert_alpha()
score_background_rect = score_backround.get_rect()
score_background_rect.topleft = (10,10)

live_background = pygame.image.load('score_background.png').convert_alpha()
live_background_rect = live_background.get_rect()
live_background_rect.topleft = (WINDOW_WIDTH-(live_background_rect.width+10), 10)

packman_image = pygame.image.load('PACKMAN.png').convert_alpha()
packman_image = pygame.transform.scale(packman_image, (50, 80))  #pACKMAN umenshit
packman_rect = packman_image.get_rect()
packman_rect.center = (80, WINDOW_HEIGHT//2)

ghostpck_image = pygame.image.load('ghostpck.png').convert_alpha()
ghostpck_image = pygame.transform.scale(ghostpck_image, (40, 60)) #Ghost umenshit
ghostpck_image_rect = ghostpck_image.get_rect()
ghostpck_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))


#blueghost
blueghostpacman_image = pygame.image.load('blueghostpacman.png').convert_alpha()
blueghostpacman_image = pygame.transform.scale(blueghostpacman_image, (40, 60)) #blueghost umenshit
blueghostpacman_image_rect = blueghostpacman_image.get_rect()
blueghostpacman_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))

#yellowghost
yellowghostpacman_image = pygame.image.load('yellowghostpacman.png').convert_alpha()
yellowghostpacman_image = pygame.transform.scale(yellowghostpacman_image, (40, 60)) #yellowghost umenshit
yellowghostpacman_image_rect = yellowghostpacman_image.get_rect()
yellowghostpacman_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))



# fonts and texts
main_font = pygame.font.Font('AttackGraffiti.ttf', 32)

score_text = main_font.render("POINT: " + str(player_score), True, RED)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (20, 20)

game_name = main_font.render("HUNGRY PACMAN", True, RED, WHITE)
game_name_rect = game_name.get_rect()
game_name_rect.center = (WINDOW_WIDTH//2, HEADER_HEIGHT//2)

live_text = main_font.render("LIFE: " + str(player_live), True, RED)
live_text_rect = live_text.get_rect()
live_text_rect.topleft = (WINDOW_WIDTH-(live_background_rect.width), 20)

game_over_text = main_font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

game_continue_text = main_font.render("PRESS ANY KEY", True, GREEN)
game_continue_rect = game_continue_text.get_rect()
game_continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)

# sounds and musics
pygame.mixer.music.load('music.wav')
sound1 = pygame.mixer.Sound('sound_1.wav')
sound2 = pygame.mixer.Sound('sound_2.wav')
sound2.set_volume(0.1)

FPS = 60
clock = pygame.time.Clock()

pygame.mixer.music.play(-1, 0.0)
# main loop
fl_pause = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and packman_rect.top > HEADER_HEIGHT:
        packman_rect.y -= ghostpck_velocity
    elif keys[pygame.K_DOWN] and packman_rect.bottom < WINDOW_HEIGHT:
        packman_rect.y += ghostpck_velocity

    ghostpck_image_rect.centerx -= ghostpck_velocity
    blueghostpacman_image_rect.centerx -= blueghostpacman_velocity
    yellowghostpacman_image_rect.centerx -= yellowghostpacman_velocity


    if ghostpck_image_rect.centerx < 0:
        ghostpck_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        player_live -= 1
        sound2.play()
    if blueghostpacman_image_rect.centerx < 0:
        blueghostpacman_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        player_live -= 1
        sound2.play()
    if yellowghostpacman_image_rect.centerx < 0:
        yellowghostpacman_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        player_live -= 1
        sound2.play()




    if packman_rect.colliderect(ghostpck_image_rect):
        player_score += 1
        sound1.play()
        ghostpck_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        ghostpck_velocity += acceleration

    if packman_rect.colliderect(blueghostpacman_image_rect):
        player_score += 1
        player_live +=2
        sound1.play()
        blueghostpacman_image_rect.center = ((WINDOW_WIDTH-BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        blueghostpacman_velocity += acceleration
    
    if packman_rect.colliderect(yellowghostpacman_image_rect):
        player_score -= 1
        player_live -=1
        sound1.play()
        yellowghostpacman_image_rect.center = ((WINDOW_WIDTH-BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        yellowghostpacman_velocity += acceleration

        
    if player_live == 0 or player_score >15:
        fl_pause = True
        pygame.mixer.music.stop()
        live_text = main_font.render("LIFE: " + str(player_live), True, RED)
        display_surface.blit(live_text, live_text_rect)
        pygame.display.update()
        while fl_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fl_pause = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    player_score = PLAYER_STARTING_SCORE
                    player_live = PLAYER_STARTING_LIVE
                    ghostpck_velocity = GHOSTPCK_STARTING_VELOCITY
                    blueghostpacman_velocity = GHOSTPCK_STARTING_VELOCITY
                    yellowghostpacman_velocity = GHOSTPCK_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0) 
                    fl_pause = False

            display_surface.blit(game_over_text, game_over_rect)
            display_surface.blit(game_continue_text, game_continue_rect)
            pygame.display.update()


    display_surface.blit(background, (0,0))
    display_surface.blit(score_backround, score_background_rect)
    display_surface.blit(live_background, live_background_rect)
    pygame.draw.line(display_surface, WHITE, (0, HEADER_HEIGHT), (WINDOW_WIDTH, HEADER_HEIGHT), 5)
    display_surface.blit(packman_image, packman_rect)
    display_surface.blit(ghostpck_image, ghostpck_image_rect)
    display_surface.blit(blueghostpacman_image, blueghostpacman_image_rect)
    display_surface.blit(yellowghostpacman_image, yellowghostpacman_image_rect)
    
    score_text = main_font.render("POINT: " + str(player_score), True, RED)
    live_text = main_font.render("LIFE: " + str(player_live), True, RED)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(game_name, game_name_rect)
    display_surface.blit(live_text, live_text_rect)
    


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()