import pygame
import random
import os
from pathlib import Path

pygame.init()

fullscreen = False
width, height = WIDTH, HEIGHT = 1100, 600
suface_height = 18
font_size = 20

screen = pygame.display.set_mode((width, height))
font = pygame.font.Font(os.path.join(Path.home(),"Library", "Fonts", "simhei.ttf") if os.name == 'posix' else "simhei.ttf", font_size)

bg_suface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
pygame.Surface.convert(bg_suface)
bg_suface.fill(pygame.Color(0, 0, 0, 28))

screen.fill((0, 0, 0))

letter = "祝您2023年兔年快乐，阖家幸福！！！！"
texts = [font.render(i, True, (0, 255, 0)) for i in letter]

column = int(width / suface_height)
drops = [random.randint(0, height//suface_height) for i in range(column)]
text_position = [random.randint(0, len(letter)) for i in range(column)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                exit()
            elif event.key == pygame.K_F11 or event.key == pygame.K_m:
                fullscreen = not fullscreen
                if fullscreen:
                    width, height = pygame.display.list_modes()[0]
                    # The resolution on Mac OS should be set to half of the actual screen.
                    # os.name can be Mac/Linux/BSD but here with half resolution on linux will be fine,
                    # however macOS will behave strange. Thus, here I set it to half.
                    if os.name == 'posix':  width, height = width//2, height//2
                    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.HWSURFACE)
                else:
                    width, height = WIDTH, HEIGHT  # restore the origin resolution
                    screen = pygame.display.set_mode((width, height))

                bg_suface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
                pygame.Surface.convert(bg_suface)
                bg_suface.fill(pygame.Color(0,0,0,28))
                column = int(width/suface_height)
                drops = [random.randint(0, len(letter)) for i in range(column)]
                text_position = [random.randint(0, len(letter)) for i in range(column)]

    # code rain
    pygame.time.delay(30)
    screen.blit(bg_suface, (0, 0))
    for i in range(len(drops)):
        text = texts[text_position[i] % len(texts)]
        screen.blit(text, (i * suface_height, drops[i] * suface_height))
        drops[i] += 1
        text_position[i] += 1
        if drops[i] * suface_height > height or random.random() > 0.98:
            drops[i] = 0
    pygame.display.flip()
