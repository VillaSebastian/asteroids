import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.line_width = 2

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen,"white", self.triangle(), self.line_width)

    def update(self, dt):
        # sub-classes must override
        pass
