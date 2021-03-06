"""
City Scape Generator

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.shape_list_skylines
"""
import random
import arcade
import os

SPRITE_SCALING = 3
SPRITE_SCALE = 2
SPRITE_SCALING_LASER = 0.8
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 600
SPRITE_SCALING_LASER = 0.15
BULLET_SPEED = 10
VIEWPORT_MARGIN = 40

BULLET_SPEED = 30
MOVEMENT_SPEED = 5
JUMP_SPEED = 8
GRAVITY = 0.5


class Dog(arcade.Sprite):
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

        # song atribute
        self.main_sound = arcade.load_sound("Sound/main_song.mp3")
        self.mute = 0

        self.bullet_list = None

        # la list complete des sprites
        self.all_sprites_list = None

        #initialisation des sprites et outils pour le joueur
        self.player = None
        self.player_sprite = None
        self.player_laser = None

        self.robot = None
        self.robot_sprite = None
        self.robot_laser = None

        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0
        self.count_y = 0
        self.bloc_list = None


        self.lazer_sound = arcade.sound.load_sound("Sound/lazer.mp3")
        self.hitmarker_sound = arcade.sound.load_sound("Sound/hitmarker.mp3")
        
    def setup(self):
        """ Set up the game and initialize the variables. """

        self.all_sprites_list = arcade.SpriteList()
        self.player_sprite = arcade.SpriteList()
        self.bloc_list = arcade.SpriteList()
        self.robot_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        for i in range(1500):
            bloc = arcade.Sprite('Image/textures/ground.png', SPRITE_SCALE)
            bloc.center_x = i * SPRITE_SCALE * 16
            bloc.center_y = 16
            self.bloc_list.append(bloc)

        self.player = arcade.AnimatedWalkingSprite()
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                             self.bloc_list,
                                                             gravity_constant=GRAVITY)
        robot_scale = 0.15

        for i in range(50):
            robot = arcade.AnimatedWalkingSprite()
             
            robot.walk_right_textures = []
            robot.walk_right_textures.append(arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_000.png",
                                                                      scale = robot_scale, mirrored= True))
            robot.stand_right_textures = []

            robot.stand_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_000.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_001.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_002.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_003.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_004.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_005.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_006.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_007.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_008.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_009.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_010.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_011.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_012.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_013.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_014.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_015.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_016.png",
                                    scale=robot_scale, mirrored= True))
            robot.walk_right_textures.append(
                arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_017.png",
                                    scale=robot_scale, mirrored= True))

            robot.center_x = i * SPRITE_SCALE * 1000
            robot.center_y = 115
            self.robot_list.append(robot)

            
        character_scale = 2
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("Image/Sprite/Dog/Chien_stand.png",
                                                                    scale=character_scale))

        # Gestion des Sprites des robots
        self.robot = arcade.AnimatedWalkingSprite()
        self.robot.walk_right_textures = []
        self.robot.walk_right_textures.append(arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_000.png",
                                                                  scale = robot_scale, mirrored= True))
        self.robot.stand_right_textures = []

        self.robot.stand_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_000.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_001.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_002.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_003.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_004.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_005.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_006.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_007.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_008.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_009.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_010.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_011.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_012.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_013.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_014.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_015.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_016.png",
                                scale=robot_scale, mirrored= True))
        self.robot.walk_right_textures.append(
            arcade.load_texture("Image/Sprite/Robot_PNG/PNG_Animations/Robot1/06_Attack/Attack_017.png",
                                scale=robot_scale, mirrored= True))
        

        # Gestion des Sprites de mouvement du joueur
        self.player.walk_right_textures = []
        self.player.laser_strike_texture = []

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

        self.player.laser_strike_texture.append(arcade.load_texture("Image/Sprite/Dog_laser/Laser_Dog1.png",
                                                                    scale=character_scale))
        self.player.laser_strike_texture.append(arcade.load_texture("Image/Sprite/Dog_laser/Laser_Dog2.png",
                                                                    scale=character_scale))
        self.player.laser_strike_texture.append(arcade.load_texture("Image/Sprite/Dog_laser/Laser_Dog3.png",
                                                                    scale=character_scale))
        # Défini la vitesse d'afficahge des sprites joueurs
        self.player.texture_change_distance = 15
        self.robot.texture_change_distance = 0.5

        self.player.center_x = SCREEN_WIDTH // 8
        self.player.center_y = SCREEN_HEIGHT // 12
        self.robot.center_x = SCREEN_WIDTH // 2
        self.robot.center_y = SCREEN_HEIGHT// 5

        self.player.scale = 2

        self.all_sprites_list.append(self.player)
        self.all_sprites_list.append(self.robot)

        # Routage de l'image background
        self.background = arcade.load_texture("Image/Background/cyberpunk-street-files/PNG/cyberpunk-street.png")

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH * 50 , SCREEN_HEIGHT, self.background, repeat_count_x=50)
        self.bullet_list.draw()
        self.all_sprites_list.draw()
        self.bloc_list.draw()
        self.robot_list.draw()

    def update(self, delta_time):
        """ Movement and game logic """
        self.bullet_list.update()
        self.bloc_list.update()
        self.all_sprites_list.update()
        self.all_sprites_list.update_animation()
        self.physics_engine.update()
        self.robot_list.update()
        self.robot_list.update_animation()
        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        self.view_left += MOVEMENT_SPEED
        arcade.set_viewport(self.view_left,
                            SCREEN_WIDTH + self.view_left,
                            self.view_bottom,
                            SCREEN_HEIGHT + self.view_bottom)

        self.player.change_x = 2.5
        self.robot.change_x = 0.1
        for robot in self.robot_list:
            robot.texture_change_distance = 0.5
            robot.change_x = 0.1

        for bullet in self.bullet_list:
             # Check this bullet to see if it hit a coin
             hit_list = arcade.check_for_collision_with_list(bullet, self.robot_list)

             # If it did, get rid of the bullet
             if len(hit_list) > 0:
                bullet.kill()

             for robot in hit_list:
                 robot.kill()
                 arcade.sound.play_sound(self.hitmarker_sound)

             if bullet.right > SCREEN_WIDTH+self.view_left:
                 bullet.kill()

    # Song activation
        if self.mute == 0:
            arcade.play_sound(self.main_sound)
            self.mute = 1

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.SPACE:
            self.player.change_y = JUMP_SPEED
            self.count_y += self.player.change_y
        if key == arcade.key.V:
            arcade.sound.play_sound(self.lazer_sound)
            bullet = arcade.Sprite("Image/Sprite/Laser.png", SPRITE_SCALING_LASER)
            bullet.center_x = self.player.center_x + 130
            bullet.center_y = self.player.center_y + 20
            bullet.change_x = BULLET_SPEED


            self.bullet_list.append(bullet)
            
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.SPACE:
            self.player.change_y = -MOVEMENT_SPEED


def main():
    window = Cyberbot()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
