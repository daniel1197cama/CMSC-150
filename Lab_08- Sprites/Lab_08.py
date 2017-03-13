import arcade
import random
import math
SPRITE_SCALING = .4
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Asteroid(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


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
        self.asteroid_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

    def setup(self):
        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        # Image from clipart fest, clipartfest.com
        self.player_sprite = arcade.Sprite("spaceship.png",
                                           SPRITE_SCALING / 2.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.all_sprites_list.append(self.player_sprite)

        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.BLACK)

        for i in range(50):
            # Image from clker, clker.com
            star = Star("star.png", SPRITE_SCALING / 5)
            star.circle_center_x = random.randrange(SCREEN_WIDTH - 200)
            star.circle_center_y = random.randrange(SCREEN_HEIGHT - 200)

            star.radius = random.randrange(10, 200)
            star.angle = random.random() * 2 * math.pi

            self.all_sprites_list.append(star)
            self.star_list.append(star)

        for i in range(10):
            asteroid = Asteroid("asteroid.png", SPRITE_SCALING / 5)

            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            asteroid.change_x = random.randrange(-3, 4)
            asteroid.change_y = random.randrange(-3, 4)

            self.all_sprites_list.append(asteroid)
            self.asteroid_list.append(asteroid)

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
        # Check for collision with "good sprites" and add 1 to the score.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.star_list)
        for star in hit_list:
            self.score += 1
            star.kill()
            if len(self.star_list) == 0:
                arcade.draw_text("Game Over", 400, 300, arcade.color.WHITE, 100)

        # Check for collision with "bad sprites" and subtract 1 to the score.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.asteroid_list)
        for asteroid in hit_list:
            self.score -= 1
            asteroid.kill()



def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
