import pygame
import random

# Basics of the game 

class Player(object):
  
  
  def __init__(self):
    self.image = pygame.image.load("img/crosshair2-600.png")
    self.rect = self.image.get_rect(center = (half_screen_width, half_screen_height))
  
  def aim(self):
    self.rect.center = pygame.mouse.get_pos()
    
    
class Target(object):
  
  
  def __init__(self):
    self.image = pick_one()
    self.rect = self.image.get_rect(center = (random_generator_x, random_generator_y))
    
def pick_one():
  
  # Rozhodovaci list ci bude target dobry alebo zly 1 good 0 bad
  choice_gen_list = [1,1,1,1,1,1,0]
  choice = random.choice(choice_gen_list)
  if choice == 1:
    return pygame.image.load("img/target1.png")
  else:
    return pygame.image.load("img/target2.png")

pygame.init()

fps = 60
clock = pygame.time.Clock()

# Mouse setings
pygame.mouse.set_visible(False)

# Window settings 

screen_width = 1200
screen_height = 700
half_screen_width = screen_width//2
half_screen_height = screen_height//2
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reaction Time")

# Game setup

random_generator_x = random.randint(70, (screen_width - 70))
random_generator_y = random.randint(70, (screen_height - 70))
print(random_generator_x, random_generator_y)

# Images

background_image = pygame.image.load("img/Jungle1.jpg")
background_image_rect = background_image.get_rect()
background_image_rect.center = (half_screen_width, half_screen_height)


# Creating player and targets objects

player = Player()
target = Target()

# Main loop

running_flag = True

while running_flag:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running_flag = False
      
    if event.type == pygame.MOUSEBUTTONDOWN:
      click_x = event.pos[0]
      click_y = event.pos[1]
      
      if target.rect.collidepoint(click_x, click_y):
        random_generator_x = random.randint(70, (screen_width - 70))
        random_generator_y = random.randint(70, (screen_height - 70))
        target = Target()
        

  # Aiming
  player.aim()
  
  # images
  screen.blit(background_image, background_image_rect)
  screen.blit(target.image, target.rect)
  screen.blit(player.image, player.rect)
  
  # Screen update
  pygame.display.update()

  # slowing cycle
  clock.tick(fps)
