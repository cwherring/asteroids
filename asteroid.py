from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
 
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta):    
        self.position += self.velocity * delta    
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(new_angle)
            new_vector2 = self.velocity.rotate(-new_angle)
            new_radius1 = self.radius - ASTEROID_MIN_RADIUS
            new_radius2 = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius1)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius2)
            new_asteroid1.velocity = (new_vector1 * 1.2)
            new_asteroid2.velocity = (new_vector2 * 1.2)

            
