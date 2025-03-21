import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1360, 768))
clock = pygame.time.Clock()



def run_game():
    rectwidth = 300
    rectheight = 20
    
    ball_pos = pygame.Vector2(500,350)
    player_pos = pygame.Vector2(550, 730)
    ball_speed = pygame.Vector2(4,-4)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
     
            
        screen.fill((0,0,0))  
        
        
        keys = pygame.key.get_pressed()
      
        if keys[pygame.K_RIGHT]:
            player_pos.x += 10
        if keys[pygame.K_LEFT]:
            player_pos.x -= 10   

            
        ball_pos += ball_speed

        if ball_pos.x <= 0 or  ball_pos.x >= screen.get_width():
            ball_speed.x *= -1  
        if ball_pos.y <= 0:
            ball_speed.y *= -1
        
        if ball_pos.y + 10 >= player_pos.y and ball_pos.y - 10 <= player_pos.y + rectheight:
            if player_pos.x <= ball_pos.x <= player_pos.x + rectwidth:
                ball_speed.y *= -1  
                ball_speed.x += 1
                ball_speed.y -= 1


        
        pygame.draw.rect(screen, "red", (player_pos.x,player_pos.y, rectwidth, rectheight))
        pygame.draw.circle(screen,"blue",ball_pos, 10)
       
    
        pygame.display.flip()
        clock.tick(60)

run_game()

pygame.quit()