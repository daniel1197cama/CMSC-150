"""
Starting Template
"""
import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
BALL_RADIUS = 20


class MyApplication(arcade.Window):
    """
    Main application class.
    """
    def __init__(self, width, height):
        super().__init__(width, height)

        self.spaceship_x_position = BALL_RADIUS
        self.spaceship_x_pixels_per_second = 70

        arcade.set_background_color(arcade.color.WHITE)

        # Note:
        # You can change how often the animate() method is called by using the
        # set_update_rate() method in the parent class.
        # The default is once every 1/80 of a second.
        # self.set_update_rate(1/80)

    def on_draw(self):
        arcade.start_render()
        # Upload picture of spaceship used in Lab 03
        file_name = "spaceship1.png"
        texture = arcade.load_texture(file_name)
        scale = .4
        arcade.draw_texture_rectangle(self.spaceship_x_position, SCREEN_HEIGHT // 2 , scale * texture.width,
                                      scale * texture.height, texture)
        # Draw the text
        arcade.draw_text("This is a simple template to start your game.",
                         10, SCREEN_HEIGHT // 2, arcade.color.BLACK, 20)

    def animate(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # Move the ball
        self.spaceship_x_position += self.spaceship_x_pixels_per_second * delta_time

        # Did the ball hit the right side of the screen while moving right?
        if self.spaceship_x_position > SCREEN_WIDTH - BALL_RADIUS \
                and self.spaceship_x_pixels_per_second > 0:
            self.spaceship_x_pixels_per_second *= -1

        # Did the ball hit the left side of the screen while moving left?
        if self.spaceship_x_position < BALL_RADIUS \
                and self.spaceship_x_pixels_per_second < 0:
            self.spaceship_x_pixels_per_second *= -1

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://pythonhosted.org/arcade/arcade.key.html
        """

        # See if the user hit Shift-Space
        # (Key modifiers are in powers of two, so you can detect multiple
        # modifiers by using a bit-wise 'and'.)
        if key == arcade.key.SPACE and key_modifiers == arcade.key.MOD_SHIFT:
            print("You pressed shift-space")

        # See if the user just hit space.
        elif key == arcade.key.SPACE:
            print("You pressed the space bar.")

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.SPACE:
            print("You stopped pressing the space bar.")

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()