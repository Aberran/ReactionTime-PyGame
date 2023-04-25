import pygame
import random

# Basics of the game 

class Player(object):
  
  
  def __init__(self):
    self.image = player_image
    self.rect = make_rect(player_image, half_screen_width, half_screen_height)
  
  def aim(self):
    self.rect.center = pygame.mouse.get_pos()
    
    
class Target(object):
  
  
  def __init__(self):
    self.image = pick_one()
    self.rect = make_rect(self.image, random_generator_x, random_generator_y)

# Window settings 

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reaction Time")  

# VARIABLES

player_image = pygame.image.load("img/crosshair2-600.png")
background_image = pygame.image.load("img/Jungle1.jpg")
half_screen_width = screen_width//2
half_screen_height = screen_height//2  
    
# function which will pick target picture
def pick_one():
  
  # Rozhodovaci list ci bude target dobry alebo zly 1 good 0 bad
  choice_gen_list = [1,1,1,1,1,1,0]
  choice = random.choice(choice_gen_list)
  if choice == 1:
    return pygame.image.load("img/target1.png")
  else:
    return pygame.image.load("img/target2.png")

# Rect crefting funcion

def make_rect(image, x, y):
  img_rect = image.get_rect()
  img_rect.center = (x, y)
  return img_rect

# Background image 

background_image_rect = make_rect(background_image, half_screen_width, half_screen_height)

# Initiate game 

pygame.init()

fps = 60
clock = pygame.time.Clock()

# Mouse setings

pygame.mouse.set_visible(False)

# Game setup

random_generator_x = random.randint(70, (screen_width - 70))
random_generator_y = random.randint(70, (screen_height - 70))
print(random_generator_x, random_generator_y)

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
  
  # draw images
  screen.blit(background_image, background_image_rect)
  screen.blit(target.image, target.rect)
  screen.blit(player.image, player.rect)
  
  # Screen update
  pygame.display.update()

  # slowing cycle
  clock.tick(fps)
