import arcade
import random
import math
SPRITE_SCALING = .4
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Star(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.angle = 0
        self.radius = 0
        self.speed = 0.008

        self.circle_center_x = 0
        self.circle_center_y = 0

        def update(self):
            self.center_x = self.radius * math.sin(self.angle) \
                            + self.circle_center_x
            self.center_y = self.radius * math.cos(self.angle) \
                            + self.circle_center_y
            self.angle += self.speed


class MyApplication(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        # Sprite lists
        self.all_sprites_list = None
        self.star_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

    def setup(self):
        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        # Image from clipart fest, clipartfest.com
        self.player_sprite = arcade.Sprite("spaceship.png",
                                           SPRITE_SCALING / 2.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.all_sprites_list.append(self.player_sprite)

        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.BLACK)

        for i in range(30):
            # Image from clker, clker.com
            star = Star("star.png", SPRITE_SCALING / 5)
            star.circle_center_x = random.randrange(SCREEN_WIDTH)
            star.circle_center_y = random.randrange(SCREEN_HEIGHT)

            star.radius = random.randrange(10, 200)
            star.angle = random.random() * 2 * math.pi

            self.all_sprites_list.append(star)
            self.star_list.append(star)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def animate(self, delta_time):
        self.all_sprites_list.update()

        # Check for collision with "good sprites" and and 1 to the score.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.star_list)
        for star in hit_list:
            self.score += 1
            star.kill()


def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()