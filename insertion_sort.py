import random
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
clock = pygame.time.Clock() 

class numbers_displayer:
  def __init__(self, WIDTH, HEIGHT, numbers, scale, line_width, window_name, matching_list):
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.numbers = numbers
    self.scale = scale
    self.line_width = line_width
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.numbers_length = len(numbers)
    self.matching_list = matching_list
    pygame.display.set_caption(window_name)
 
  def update_screen(self):
         self.screen.fill(BLACK)    
         for i in range(self.numbers_length):
             current_x = int(i * self.WIDTH / self.numbers_length)
             next_x = int((i + 1) * self.WIDTH / self.numbers_length)
             width = next_x - current_x 
             if not self.matching_list:
                 color = WHITE
             else:
                 color = GREEN if self.matching_list[i] == self.numbers[i] else RED
             pygame.draw.rect(
                 self.screen, 
                 color, 
                 (
                     current_x, 
                     self.HEIGHT - (self.numbers[i] * self.scale), 
                     width, 
                     self.numbers[i] * self.scale
                 )
             )
         pygame.display.flip()

random_numbers = []
for i in range(50):
    random_numbers.append(random.randint(0,410))
  

screen = numbers_displayer(360, 480, random_numbers, 1, 5, "insertion-sort", sorted(random_numbers))


n = len(random_numbers)
#from https://www.geeksforgeeks.org
for i in range(1, n):
    key = random_numbers[i]         
    j = i - 1
    while j >= 0 and key < random_numbers[j]: 
        random_numbers[j + 1] = random_numbers[j]
        j -= 1
        screen.update_screen()
        clock.tick(30)
    random_numbers[j + 1] = key      
    screen.update_screen()
while True:
    clock.tick(1)
