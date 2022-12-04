import pygame

from pygame.sprite import Sprite

class GroundIce(Sprite):
    """Initialize everything for the ice block that is on the bottom"""

    def __init__(self, ice_penguin, y_pos):
        super().__init__()
        self.settings = ice_penguin.settings
        self.screen = ice_penguin.screen
        self.settings = ice_penguin.settings
        self.screen_rect = ice_penguin.screen.get_rect()

        self.image = pygame.image.load('images/ice.png')
        # Size of the ice block (width,height)
        self.image = pygame.transform.scale(self.image, (100, 100))
        # Dimensions of the rectangle are defined by the image
        self.rect = self.image.get_rect()

        self.groundice_speed = 1.5

        # Determine the x position to start
        self.start_x = self.settings.screen_width
        self.start_y = y_pos
        self.rect.x = self.start_x
        # Determines the height of the ice block from the top of the screen
        self.rect.y = self.start_y

    def update(self):
        """Update the position of the ice blocks"""
        # adjusting the position of the ice block corresponding to speed
        if self.rect.x + self.rect.width > 0:
            self.rect.x -= self.groundice_speed
            # 370
            self.rect.y = self.start_y
            print(f"x {self.rect.x} y: {self.rect.y}")
        else:
            # Used as a sprite method in order for the ice block to kill itself off at the end of the screen
            self.kill()
