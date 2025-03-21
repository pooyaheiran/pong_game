import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1360, 768))
clock = pygame.time.Clock()
dt = .5
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((10,20,60))
        pygame.draw.rect(screen, "red", (player_pos.x,player_pos.y, 20, 20))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_pos.y -= 5 
        if keys[pygame.K_DOWN]:
            player_pos.y += 5 
        if keys[pygame.K_RIGHT]:
            player_pos.x += 5
        if keys[pygame.K_LEFT]:
            player_pos.x -= 5       
        
        
        pygame.display.flip()
        clock.tick(60)

run_game()

pygame.quit()