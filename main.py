"""
City Scape Generator

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.shape_list_skylines
"""
import random
import arcade
import os

SPRITE_SCALING = 3

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

MOVEMENT_SPEED = 5

class Dog(arcade.Sprite):
  #  sprite = arcade.sprite("Image/Sprite/Dog/chien1.png")

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Cyberbot(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Cyberbot")

        #la list complete des sprites
        self.all_sprites_list = None
        self.player = None
      #  self.player_list = None

      #  self.player_sprite = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        self.all_sprites_list = arcade.SpriteList()

        self.player = arcade.AnimatedWalkingSprite()

        character_scale = 2
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("Image/Sprite/Dog/chien1.png",
                                                                    scale=character_scale))

        self.player.walk_right_textures = []

        self.player.walk_right_textures.append(arcade.load_texture("Image/Sprite/Dog/chien1.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("Image/Sprite/Dog/chien2.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("Image/Sprite/Dog/chien3.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("Image/Sprite/Dog/chien4.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("Image/Sprite/Dog/chien5.png",
                                                                   scale=character_scale))
        #What the fuck is that carp
        self.player.texture_change_distance = 20

        self.player.center_x = SCREEN_HEIGHT // 2
        self.player.center_y = SCREEN_WIDTH // 2

        self.player.scale = 2

        self.all_sprites_list.append(self.player)

        self.background = arcade.load_texture("Image/Background/cyberpunk-street-files/PNG/cyberpunk-street.png")

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH * 3 , SCREEN_HEIGHT, self.background, repeat_count_x=3)
        self.all_sprites_list.draw()



      #  arcade.draw_texture_rectangle(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4,
      #                                  SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

    def update(self, delta_time):
        """ Movement and game logic """
        self.all_sprites_list.update()
        self.all_sprites_list.update_animation()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.Z:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.Q:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.Z or key == arcade.key.S:
            self.player.change_y = 0
        elif key == arcade.key.Q or key == arcade.key.D:
            self.player.change_x = 0
def main():
    window = Cyberbot()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
