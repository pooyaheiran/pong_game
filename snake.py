import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1360, 768))
clock = pygame.time.Clock()
dt = .5


def run_game():
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    direction = pygame.Vector2(5, 0)
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction.y == 0:
                    direction = pygame.Vector2(0, -5)
                elif event.key == pygame.K_DOWN and direction.y == 0:
                    direction = pygame.Vector2(0, 5)
                elif event.key == pygame.K_LEFT and direction.x == 0:
                    direction = pygame.Vector2(-5, 0)
                elif event.key == pygame.K_RIGHT and direction.x == 0:
                    direction = pygame.Vector2(5, 0)
                

        screen.fill((10,20,60))      
        player_pos += direction        

        
        pygame.draw.rect(screen, "red", (player_pos.x,player_pos.y, 20, 20))

       
    
        pygame.display.flip()
        clock.tick(20)

run_game()

pygame.quit()