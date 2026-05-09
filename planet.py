import pygame
import pygame.gfxdraw
import math
import random 
import numpy as np

G_CONSTANT = (66.743)
class Planet:
    def __init__(
        self,
        position: pygame.Vector2,
        mass: float | None = None,
        radius: int | None = None,
        velocity: pygame.Vector2 | None = None,
        fixed: bool = False,
    ) -> None:
        self.size = radius if radius is not None else random.randint(4, 40)
        min_mass = self.size
        max_mass = 1000
        self.mass = mass if mass is not None else random.randint(min_mass, max(max_mass, min_mass))
        self.position = pygame.Vector2(position)
        self.radius = round(self.size)
        self.acceleration = 0
        self.velocity = (
            pygame.Vector2(velocity)
            if velocity is not None
            else pygame.Vector2(
                self.random_velocity_component(),
                self.random_velocity_component(),
            )
        )
        self.ax = 0
        self.ay = 0
        self.fixed = fixed

        self.color = self.get_random_color()

        
    def update_position(self, dt) -> None:
        if self.fixed:
            return
        self.velocity.x += self.ax  * dt
        self.velocity.y += self.ay  * dt
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
 
    def get_random_color(self):
        while True:
            color = np.random.randint(0, 256, size=3)
            if np.any(color > 10):
                    return color

    def random_velocity_component(self) -> float:
        sign = random.choice((-1.0, 1.0))
        magnitude = random.uniform(0, 5.0)
        return sign * magnitude
            
    def draw(self, screen) -> None:
        draw_x = round(self.position.x)
        draw_y = round(self.position.y)
        if not (-32_768 <= draw_x <= 32_767 and -32_768 <= draw_y <= 32_767):
            return
        
        pygame.gfxdraw.aacircle(screen, draw_x, draw_y, self.radius, self.color)
        pygame.gfxdraw.filled_circle(screen, draw_x, draw_y, self.radius, self.color)
        #pygame.draw.circle(screen, "black", (self.x, self.y), 1 )
    
    def reset_acceleration(self) -> None:
        self.ax = 0
        self.ay = 0

    def gravitational_pull(self, planet_mass, planet_radius_position: pygame.Vector2) -> None:
        dx = planet_radius_position.x - self.position.x
        dy = planet_radius_position.y - self.position.y
        distance = math.hypot(dx, dy)
        distance = max(distance, 20)
        nx = dx / distance
        ny = dy / distance

        self.acceleration = G_CONSTANT * planet_mass / distance**2
        
        ax = self.acceleration * nx
        ay = self.acceleration * ny

        self.ax += ax
        self.ay += ay





        

        

    
