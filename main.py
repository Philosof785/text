import pygame

W = 800
H = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 100)
OUTSIDE_BG = (0, -100)

pygame.init()
pygame.display.set_caption("Текст")
screen = pygame.display.set_mode((W, H))
screen.fill(BLUE)
pugame.display.update()
def dialogs(text, pos, text):
    screen.blit(dialog, pos)
    screen.blit(font.render(text, True, WHITE)
    pygame.display.update()
    pygame.time.wait(2000)

text = dialogs.get_rect(center=(210, 70))
pygame.display.update()