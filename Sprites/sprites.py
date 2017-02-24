import random
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# I will need to inherit the parent class so I can add new features to the original coins


class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super(). __init__(filename, sprite_scaling)
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

        """
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0 and self.change_y < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT and self.change_y < SCREEN_HEIGHT:
            self.change_y *= -1

        if self.top < 0:
            self.center_x = random.randrange(SCREEN_WIDTH)
            self.center_y = random.randrange(SCREEN_HEIGHT + 20 , SCREEN_HEIGHT + 20)
        """


class MyApplication(arcade.Window):
    def __init__(self, width, height):
        # --- Class methods will go here
        super().__init__(width, height)

        self.all_sprites_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING)

        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.all_sprites_list.append(self.player_sprite)

        for i in range(50):
            coin = Coin("coin_01.png", SPRITE_SCALING * 0.5)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()
        arcade.draw_text("Score: " + str(self.score), 10, 20, arcade.color.WHITE, 20)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def animate(self, delta_time):
        self.all_sprites_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list:
            coin.kill()
            self.score += 1
        """
        if len(self.coin_list) == 0:
            for i in range(50):
                coin = arcade.Sprite("coin_01.png", SPRITE_SCALING * 0.5)
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)
                self.all_sprites_list.append(coin)
                self.coin_list.append(coin)
            print("EMPTY!!")
        """


def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()

    arcade.run()

main()
