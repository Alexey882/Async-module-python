import pygame
pygame.init()
W = 400
H = 400
WHITE = (255, 255, 255)
class Roket(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 100))
sc = pygame.display.set_mode((W, H))
roket= Roket(100, 'rocet.png')
while True:
    sc.fill(WHITE)
    sc.blit(roket.image, roket.rect)
    pygame.display.update()
    pygame.time.delay(20)
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
            exit()
      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_LEFT]:
        roket.rect.x -= 5
      elif pressed[pygame.K_RIGHT]:
        roket.rect.x += 5
      if pressed[pygame.K_UP]:
        roket.rect.y -= 5
      elif pressed[pygame.K_DOWN]:
        roket.rect.y += 5
      sc.blit(roket.image, roket.rect)
      pygame.display.update()
      pygame.time.delay(20)