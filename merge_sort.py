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
  

screen = numbers_displayer(360, 480, random_numbers, 1, "merge-sort", sorted(random_numbers))


#from https://www.geeksforgeeks.org
def merge(arr, l, m, r, screen):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        screen.update_screen()
        clock.tick(30)

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        screen.update_screen()
        clock.tick(30)
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        screen.update_screen()
        clock.tick(30)

def mergeSort(arr, l, r, screen):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m, screen)
        mergeSort(arr, m + 1, r, screen)
        merge(arr, l, m, r, screen)
mergeSort(random_numbers, 0, len(random_numbers) - 1, screen)



while True:
    clock.tick(1)
