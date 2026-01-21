import random
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
clock = pygame.time.Clock() 

class numbers_displayer:
  def __init__(self, WIDTH, HEIGHT, numbers, scale, window_name, matching_list):
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.numbers = numbers
    self.scale = scale
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
  

screen = numbers_displayer(360, 480, random_numbers, 1, "horrible-sort", sorted(random_numbers))

for i in range(screen.numbers_length):
    for u in range(screen.numbers_length-i-1):
        clock.tick(240)
        if random_numbers[u] > random_numbers[u+1]:
            temp = random_numbers[u]
            random_numbers[u] = random_numbers[u+1]
            random_numbers[u+1] = temp
        screen.update_screen()

while True:
    clock.tick(1)
