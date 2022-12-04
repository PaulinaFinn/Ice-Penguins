import pygame


class Penguin:
    """A class to manage the penguin."""
    def __init__(self, ip_game):
        """Initialize the penguin and set its starting position."""
        self.screen = ip_game.screen
        self.settings = ip_game.settings
        self.screen_rect = ip_game.screen.get_rect()


        # Load the penguin image and get its rect.
        self.original_image = pygame.image.load('images/penguin.png')
        # Changing the penguin size if needed, the code below can change it, Note: if the penguins size is changed
        # Then the positioning of him also needs to change, aka his "rectangle", otherwise his position will be off
        #self.original_image = pygame.transform.scale(self.original_image, (600, 600))
        self.image = self.original_image

        self.rect = self.image.get_rect()

        #Start each new penguin at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft
        self.rect.x += 180

        self.y = float(self.rect.y)


        # Movement flag
        self.rotate_right = False
        # Gravity Flag
        self.gravity_active = True
        self.vertical_speed = 2.0
        self.jumping_up = False

        # Flag to see if penguin collided with ice
        self.penguin_ice_collision = False

    def check_penguin_ice_collision(self, groundice_group):
        """look if there is a collision and if there is delete the ice and return that the game should be stopped"""
        collision = pygame.sprite.spritecollide(self, groundice_group, True)
        # If there is a collision the ice block will be deleted and collision returns true
        # if there is a collison return true so that the game knows it should stop
        if collision:
            self.penguin_ice_collision = True


    def update(self, groundice_group):
        """Update the penguins position based on the movement flag."""
        # Check if the penguin has collided with the iceblock by calling the following function
        self.check_penguin_ice_collision(groundice_group)

        # Update the penguins y value, not the rect.
        if self.rotate_right:
            #self.y -= self.settings.penguin_speed
            # This is to rotate the image when the penguin needs to rotate and slide under the block
            self.image = pygame.transform.rotate(self.original_image,-45)
        else:
            self.image = self.original_image


        #self.rect = self.original_image.get_rect(center=self.rect.center)

        # If pengiun is going to fall through the ground, just set its y position equal to the ground.
        # This goes along with if we change the size of the penguin
        if self.rect.y >= 300:
            self.rect.y = 300
        # Keep the top of the penguin inside the screen by setting the lowest y value it can go to zero
        # This tells us where the head of the penguin will hit before the game is over
        if self.rect.y <= -55:
            self.rect.y = -55
        # Update rect object from self.y.
        # if this is true
        if self.gravity_active:
            self.rect.y += 1.5

        if self.jumping_up:
            self.rect.y -= self.vertical_speed



    def blitme(self):
        """Draw the penguin at its current location."""
        self.screen.blit(self.image, self.rect)
