import pygame
import random
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Ping pong game")
clock = pygame.time.Clock()
coll = pygame.mixer.Sound("ping.wav")
miss = pygame.mixer.Sound("miss.wav")
achive = pygame.mixer.Sound("achive.wav")
time = 120
main_time = 120
player_score = 0
ai_score = 0
font = pygame.font.SysFont("Arial", 50)
font2 = pygame.font.SysFont("Arial", 30)
green = (0, 255, 0)
red = (255, 0, 0)
none = (255, 255, 200)
ball_color = none
count = 0
finished = False
class character:
    def __init__(self, Width, Height, X, Y):
        self.width = Width
        self.height = Height
        self.x = X
        self.y = Y
player = character(7, 70, 5, 165)
ai = character(7, 70, 790, 165)
ball = character(5, 5, 400, 200)
speed = [6, 7]
ai_speed = random.randint(5, 7)
level = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    text1 = font.render(str(player_score), True, (150, 100, 150))
    text2 = font.render(str(ai_score), True, (150, 100, 150))
    text3 = font2.render(str(main_time), True, (150, 200, 250))
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 170), 5)
    pygame.draw.line(screen, (255, 255, 255), (400, 230), (400, 400), 5)
    pygame.draw.rect(screen, (100, 100, 200), (player.x, player.y, player.width, player.height))
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
    ai_rect = pygame.Rect(ai.x, ai.y, ai.width, ai.height)
    pygame.draw.rect(screen, (100, 100, 200), (ai.x, ai.y, ai.width, ai.height))
    pygame.draw.circle(screen, ball_color, (ball.x, ball.y), 5)
    screen.blit(text1, (190, 170))
    screen.blit(text2, (610, 170))
    ball_rect = pygame.Rect(ball.x - 5, ball.y - 5, 5 * 2, 5 * 2)
    rect1 = ball_rect.colliderect(player_rect)
    rect2 = ball_rect.colliderect(ai_rect)
    if main_time <= 0:
        finished = True
    
    print(ai_speed)
    if finished == False:
        time -= (1 / 60)
        main_time = int(time)
        if main_time >= 100:
            screen.blit(text3, (380, 180))
        
        elif main_time < 100:
            screen.blit(text3, (385, 180))
        elif main_time < 10:
            screen.blit(text3, (445, 180))
            
        if ball.y >= 400:
            speed[1] *= -1
            ai_speed = random.randint(5, 7)
        elif ball.y < 0:
            speed[1] = 7
            ai_speed = random.randint(5, 7)
        if ball.x < 0:
            speed[0] *= -1
            ai_score += 1
            miss.play()
            ball_y = random.randint(0, 400)
            ball.x, ball.y = 400, ball_y
            
        elif ball.x >= 800:
            speed[0] = 6
            player_score += 1
            miss.play()
            ball_y = random.randint(0, 400)
            ball.x, ball.y = 400, ball_y
        
        if ball. y < ai.y + ai.height // 2:
            ai.y -= ai_speed
        elif ball.y > ai.y + ai.height // 2:
            ai.y += ai_speed
        
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= 7
        if keys[pygame.K_DOWN] and player.y <= 400 - player.height:
            player.y += 7
            
#         if ball.x <= player.x + player.width and ball.y >= player.y - 5 and ball.y <= player.y + player.height + 5:
#             speed[0] *= -1
#             coll.play()
#         if ball.x >= ai.x - ai.width and ball.y >= ai.y and ball.y <= ai.y + ai.height:
#             speed[0] *= -1
#             coll.play()
        if rect1:
            speed[0] *= -1
            coll.play()
        if rect2:
            speed[0] *= -1
            coll.play()
        ball.x -= speed[0]
        ball.y += speed[1]
        if player_score > ai_score:
            ball_color = green
        elif player_score < ai_score:
            ball_color = red
        else:
            ball_color = none
        if player_score % 10 == 0 and player_score != 0:
            count += 1
            if count == 1:
                achive.play()
        else:
            count = 0
    if finished == True:
        if player_score > ai_score:
            text3 = font2.render("You Won!", True, (150, 200, 250))
            screen.blit(text3, (350, 180))
        elif ai_score > player_score:
            text3 = font2.render("You Lost!!", True, (150, 200, 250))
            screen.blit(text3, (350, 180))
        else:
            text3 = font2.render("It's a tie", True, (150, 200, 250))
            screen.blit(text3, (370, 180))
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
            
    pygame.display.update()
pygame.quit()
    