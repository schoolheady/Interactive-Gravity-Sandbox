# Example file showing a circle moving on screen
import math
import pygame
import pygame.gfxdraw
import planet

planets: list[planet.Planet] = []
STAR_MASS = 200_000
STAR_RADIUS = 18
PLANET_MASS = 25
PLANET_RADIUS = 6

def draw_planets(planets: list[planet.Planet], dt) -> None:
    for body in planets:
        body.reset_acceleration()

    for i in range(len(planets)):
        for b in range(len(planets)):
            if b != i:
                planets[i].gravitational_pull(planets[b].mass, planets[b].position)

    for body in planets:
        body.update_position(dt)
        body.draw(screen)


def create_orbiting_planet(position: pygame.Vector2) -> planet.Planet:
    if not planets:
        return planet.Planet(position, mass=STAR_MASS, radius=STAR_RADIUS, velocity=pygame.Vector2(), fixed=True)

    center_body = planets[0]
    offset = position - center_body.position
    distance = offset.length()
    distance = max(distance, center_body.radius + 20)
    radial = offset.normalize()
    tangent = pygame.Vector2(-radial.y, radial.x)
    orbit_speed = math.sqrt(planet.G_CONSTANT * center_body.mass / distance)
    velocity = tangent * orbit_speed
    return planet.Planet(position, mass=PLANET_MASS, radius=PLANET_RADIUS, velocity=velocity)

    
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
        planets.append(create_orbiting_planet(position))

    draw_planets(planets, dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
