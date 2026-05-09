# Example file showing a circle moving on screen
import math
import pygame
import pygame.gfxdraw
import planet

planets: list[planet.Planet] = []

def draw_planets(planets: list[planet.Planet]) -> None:
    for i in range(len(planets)):
        
        for b in range(len(planets)):
            if b != i: 
                planets[i].gravitational_pull(planets[b].mass, planets[b].position)
        planets[i].update_position()
        planets[i].draw(screen)

    
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0


x,y = 0,0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    


    if click:
        x, y = pygame.mouse.get_pos()
        print("mouse clicked on", x, y)
        position = pygame.Vector2(x,y)
        planets.append(planet.Planet(position))

    draw_planets(planets)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
