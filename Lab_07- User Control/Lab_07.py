import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def draw_cloud(position_x, position_y):
    arcade.draw_circle_filled(position_x, position_y, 35, arcade.color.WHITE)
    arcade.draw_circle_filled(position_x - 35, position_y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(position_x + 35, position_y, 25, arcade.color.WHITE)


class Cloud:
    def __init__(self, position_x, position_y, change_x, change_y):

        self. position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        draw_cloud(self.position_x, self.position_y)

    def animate(self):
        self.position_x += self.change_x
        if self.position_x < 50:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - 60:
            self.change_x *= -1


class Spaceship:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        # Upload picture of spaceship used in Lab 03
        file_name = "spaceship1.png"
        texture = arcade.load_texture(file_name)
        scale = .4
        arcade.draw_texture_rectangle(self.position_x, self.position_y, scale * texture.width,
                                      scale * texture.height, texture)


class Parachutist:
    def __init__(self, position_x, position_y, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.jump_sound = arcade.load_sound("jump3.ogg")

    def draw(self):
        file_name = "parachutist.png"
        texture = arcade.load_texture(file_name)
        scale = .4
        arcade.draw_texture_rectangle(self.position_x, self.position_y, scale * texture.width,
                                      scale * texture.height, texture)

    def animate(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < 45:
            self.position_x = 45
            arcade.play_sound(self.jump_sound)

        if self.position_x > SCREEN_WIDTH - 35:
            self.position_x = SCREEN_WIDTH - 35
            arcade.play_sound(self.jump_sound)

        if self.position_y < 70:
            self.position_y = 70
            arcade.play_sound(self.jump_sound)

        if self.position_y > SCREEN_HEIGHT - 70:
            self.position_y = SCREEN_HEIGHT - 70
            arcade.play_sound(self.jump_sound)


class MyApplication(arcade.Window):
    """
    Main application class.
    """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color((67, 194, 232))
        # Make the mouse disappear when it is over the window.
        self.set_mouse_visible(False)
        # Load the sound when the application starts
        self.upgrade_sound = arcade.load_sound("upgrade1.ogg")

        self.parachutist = Parachutist(300, 400, 0, 0)
        # Add two clouds to the list
        self.cloud_list = []
        cloud = Cloud(100, 150, 3, 3)

        self.cloud_list.append(cloud)

        cloud = Cloud(150, 500, 2, 3)
        self.cloud_list.append(cloud)

        cloud = Cloud(400, 350, -3, -1)
        self.cloud_list.append(cloud)

        self.spaceship = Spaceship(150, 100)

    def on_draw(self):
        arcade.start_render()
        for cloud in self.cloud_list:
            cloud.draw()
        self.spaceship.draw()
        self.parachutist.draw()

    def animate(self, delta_time):
        self.parachutist.animate()
        for cloud in self.cloud_list:
            cloud.animate()

    def on_mouse_motion(self, x, y, dx, dy):
        self.spaceship.position_x = x
        self.spaceship.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.upgrade_sound)

    def on_key_press(self, key, modifiers):
        # Called whenever the user presses a key.
        if key == arcade.key.LEFT:
            self.parachutist.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.parachutist.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.parachutist.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.parachutist.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        # Called whenever a user releases a key.
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.parachutist.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.parachutist.change_y = 0

window = MyApplication(500, 600, "Spaceship Flying")
arcade.run()
