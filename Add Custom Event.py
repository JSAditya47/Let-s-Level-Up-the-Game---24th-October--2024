import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400

MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

img = pygame.image.load("img.webp")
background_image = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, color, height, width):
        
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        
        self.image.fill(pygame.Color('dodgerblue'))
        
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        
        self.rect = self.image.get_rect()
        
    def move(self, x_change, y_change):
        
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)
        
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()


sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, SCREEN_WIDTH - sprite1.rect.width), random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)
        
sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, SCREEN_WIDTH - sprite2.rect.width), random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

sprite3 = Sprite(pygame.Color('green'), 20, 30)
sprite3.rect.x, sprite3.rect.y = random.randint(0, SCREEN_WIDTH - sprite3.rect.width), random.randint(0, SCREEN_HEIGHT - sprite3.rect.height)
all_sprites.add(sprite3)

sprite4 = Sprite(pygame.Color('yellow'), 20, 30)
sprite4.rect.x, sprite4.rect.y = random.randint(0, SCREEN_WIDTH - sprite4.rect.width), random.randint(0, SCREEN_HEIGHT - sprite4.rect.height)
all_sprites.add(sprite4)

sprite5 = Sprite(pygame.Color('white'), 20, 30)
sprite5.rect.x, sprite5.rect.y = random.randint(0, SCREEN_WIDTH - sprite5.rect.width), random.randint(0, SCREEN_HEIGHT - sprite5.rect.height)
all_sprites.add(sprite5)

running, won = True, False
clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
            
    if not won:
        keys = pygame.key.get_pressed()
        
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        
        sprite1.move(x_change, y_change)
        
        if sprite1.rect.colliderect(sprite3.rect): all_sprites.remove(sprite3)
        if sprite1.rect.colliderect(sprite4.rect): all_sprites.remove(sprite4)
        if sprite1.rect.colliderect(sprite2.rect): all_sprites.remove(sprite5)
        
        
        
        
        if sprite1.rect.colliderect(sprite2.rect):
            
            all_sprites.remove(sprite2)
            won = True
            
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)
    
    if won:
        
        win_text = font.render("You Win!", True, pygame.Color("black"))
        
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2, (SCREEN_HEIGHT - win_text.get_height()) // 2))
        
    pygame.display.flip()
    clock.tick(90)
    
pygame.quit()