import pygame
import random

SCREEN_WIDTH = SCREEN_HEIGHT = 720

def draw_grid(screen, horizontals, verticals):
    x_dist = SCREEN_WIDTH / verticals
    y_dist = SCREEN_HEIGHT / horizontals

    # Horizontal Lines
    for y in range(0, SCREEN_HEIGHT, y_dist):
        pygame.draw.line(screen, "black", (0, y), (SCREEN_WIDTH, y))

    # Vertical Lines
    for x in range(0, SCREEN_WIDTH, x_dist):
        pygame.draw.line(screen, "black", (x, 0), (x, SCREEN_HEIGHT))

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        pass

if __name__ == "__main__":
    main()