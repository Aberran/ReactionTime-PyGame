import pygame 
import sys

# Basics of game 

pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reaction Time")

# Main loop

lets_continue = True

while lets_continue:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      lets_continue = False
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        click_x = event.pos[0]
        click_y = event.pos[1]
        
        