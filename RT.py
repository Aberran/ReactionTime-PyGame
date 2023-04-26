import pygame
import random

# Initiate game 

pygame.init()

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

last_hit_time = 0
current_hit_time = 0

bullets_counter = 15
time_since_last_hit = 0

# Colors

whitec = pygame.Color("#938f0c")

# Fonts

font_big = pygame.font.Font("fonts/FFF_Tusj.ttf", 50)
font_middle = pygame.font.Font("fonts/FFF_Tusj.ttf", 30)

# Texts

bullet_counter_text = font_big.render(f"Bullets left: {bullets_counter}", True, "white")
bullet_counter_text_rect = bullet_counter_text.get_rect()
bullet_counter_text_rect.topleft = (20,screen_height - 70)

time_since_last_hit_text = font_big.render(f"ReactionTime: {time_since_last_hit} ms", True, "white")
time_since_last_hit_text_rect = time_since_last_hit_text.get_rect()
time_since_last_hit_text_rect.center = (half_screen_width, 40)
    
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
  # Event hendler
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running_flag = False
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        click_x = event.pos[0]
        click_y = event.pos[1]
        bullets_counter -= 1
        
        # Hit check
        if target.rect.collidepoint(click_x, click_y):
          random_generator_x = random.randint(70, (screen_width - 70))
          random_generator_y = random.randint(70, (screen_height - 70))
          current_hit_time = pygame.time.get_ticks()
          target = Target()  

          # Time between hits calculator
          if last_hit_time != 0:
            time_since_last_hit = current_hit_time - last_hit_time
            print(time_since_last_hit)
          
          # update last click time
          last_hit_time = current_hit_time
          
  # Update bullets counter text 
  bullet_counter_text = font_big.render(f"Bullets left: {bullets_counter}", True, "white")
  time_since_last_hit_text = font_big.render(f"ReactionTime: {time_since_last_hit} ms", True, "white")
  
  # Aiming
  player.aim()
  
  # draw images
  screen.blit(background_image, background_image_rect)
  screen.blit(target.image, target.rect)
  screen.blit(player.image, player.rect)
  screen.blit(time_since_last_hit_text, time_since_last_hit_text_rect)
  screen.blit(bullet_counter_text, bullet_counter_text_rect)
  
  # Screen update
  pygame.display.update()

  # slowing cycle
  clock.tick(fps)
  
  # functions from main loop - will be clean up someday :D
  def event_checker():
    pass

pygame.quit()

