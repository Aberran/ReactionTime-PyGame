import pygame

# Basics of the game 

class Player(object):
  
  
  def __init__(self):
    self.image = pygame.image.load("img/crosshair2-600.png")
    self.rect = self.image.get_rect(center = (screen_width/2, screen_height/2))
  
  def aim(self):
    self.rect.center = pygame.mouse.get_pos()

pygame.init()

fps = 60
clock = pygame.time.Clock()

# Window settings 

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reaction Time")

# Images

target_image = pygame.image.load("img/target1.png")
target_image_rect = target_image.get_rect()
target_image_rect.center = (screen_width//2, screen_height//2)

background_image = pygame.image.load("img/Jungle1.jpg")
background_image_rect = background_image.get_rect()
background_image_rect.center = (screen_width//2, screen_height//2)

# Creating player object

player = Player()

# Main loop

running_flag = True

while running_flag:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running_flag = False
      
    if event.type == pygame.MOUSEBUTTONDOWN:
      # click_x = event.pos[0]
      # click_y = event.pos[1]
      print("Something")

  # Aiming
  player.aim()
  
  # images
  screen.blit(background_image, background_image_rect)
  screen.blit(target_image, target_image_rect)
  screen.blit(player.image, player.rect)
  
  # Screen update
  pygame.display.update()

  # slowing cycle
  clock.tick(fps)
