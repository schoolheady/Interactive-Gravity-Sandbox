import pygame
import pygame.gfxdraw
import math
import random 

G_CONSTANT = (6.6743 * 10 **-1)
class Planet:
    def __init__(self, position: pygame.Vector2) -> None:
        self.size = random.randint(4, 10)
        min_mass = self.size
        max_mass = 1000
        self.mass = random.randint(min_mass, max(max_mass, min_mass))
        self.position = pygame.Vector2(position)
        self.radius = round(self.size)
        self.velocity = pygame.Vector2(
            random.choice(list(range(-2, 0)) + list(range(1, 2))),
            random.choice(list(range(-2, 0)) + list(range(1, 2))),
        )
        self.gravitational_force = 0
        print("mass", self.mass)
        
        
    def update_position(self) -> None:
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y 
 

    def draw(self, screen):
        draw_x = round(self.position.x)
        draw_y = round(self.position.y)
        if not (-32_768 <= draw_x <= 32_767 and -32_768 <= draw_y <= 32_767):
            return
        pygame.gfxdraw.aacircle(screen, draw_x, draw_y, self.radius, (255, 0, 0))
        pygame.gfxdraw.filled_circle(screen, draw_x, draw_y, self.radius, (255, 0, 0))
        #pygame.draw.circle(screen, "black", (self.x, self.y), 1 )
    
    def calculate_pull(self, planet_mass, distance: float):
        self.gravitational_force = G_CONSTANT * self.mass * planet_mass / distance**2
        return self.gravitational_force

    def gravitational_pull(self, planet_mass, planet_radius_position: pygame.Vector2):
        dx = planet_radius_position.x - self.position.x
        dy = planet_radius_position.y - self.position.y
        distance = math.hypot(dx, dy)

        if distance == 0:
            return

        force = self.calculate_pull(planet_mass, distance)
        acceleration = G_CONSTANT * planet_mass / distance**2
        self.velocity.x += acceleration * (dx / distance)
        self.velocity.y += acceleration * (dy / distance)
        if acceleration > 1000:
            print("dx", dx, "distance:", distance )



        

        

    
