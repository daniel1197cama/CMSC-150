"""
This drawing is an update of Lab 2. It includes functions and a animation of an astronaut floating in space.
"""
import arcade


# This function draws solar panels.
def draw_solar_panels(position_x, position_y):
    arcade.draw_rectangle_filled(position_x, position_y, 40, 120, (65, 88, 140))
    point_list = ((position_x - 10, position_y - 30,),
                  (position_x - 10, position_y + 30),
                  (position_x + 10, position_y - 30),
                  (position_x + 10, position_y + 30))
    arcade.draw_points(point_list, arcade.color.BLACK, 10)
    point_list = ((position_x + 27, position_y - 12),
                  (position_x - 27, position_y - 12))
    arcade.draw_points(point_list, (121, 123, 128), 10)
    point_list = ((position_x + 23, position_y + 60),
                  (position_x + 23, position_y - 60),
                  (position_x - 23, position_y + 60),
                  (position_x - 23, position_y - 60))
    arcade.draw_lines(point_list, (121, 123, 128), 5)


# This function draws the trunk of the spacecraft.
def draw_trunk(position_x, position_y):
    arcade.draw_rectangle_filled(position_x, position_y, 210, 150, (203, 214, 214))
    arcade.draw_rectangle_outline(position_x, position_y, 210, 150, (121, 123, 128), 5)


WIDTH = 80
HEIGHT = 65
BORDER_WIDTH = .5


def draw_table_rows(position_x, position_y):
    arcade.draw_rectangle_outline(position_x, position_y, WIDTH, HEIGHT, (121, 120, 120), BORDER_WIDTH)
    arcade.draw_rectangle_outline(position_x, position_y, WIDTH, HEIGHT - 30, (121, 120, 120), BORDER_WIDTH)
    arcade.draw_rectangle_outline(position_x, position_y, WIDTH, HEIGHT - 48.9, (121, 120, 120), BORDER_WIDTH)
    arcade.draw_rectangle_filled(position_x, position_y, WIDTH - 70, HEIGHT - 48.9, arcade.color.BLACK, BORDER_WIDTH)


# Details and touch-ups functions

def draw_details(position_x, position_y, tilt_angle):
    arcade.draw_ellipse_filled(position_x, position_y, 5, 10, (61, 59, 59), tilt_angle)
    arcade.draw_ellipse_filled(position_x, position_y - 30, 5, 10, (61, 59, 59), tilt_angle - 45)
    arcade.draw_ellipse_filled(position_x + 20, position_y - 15, 5, 10, (61, 59, 59), tilt_angle + 70)
    arcade.draw_arc_filled(position_x - 18, position_y - 88, 30, 40, (54, 51, 52), 90, 270, 180)


def draw_arcdetails(position_x, position_y, tilt_angle):
    arcade.draw_ellipse_filled(position_x, position_y, 5, 10, (61, 59, 59), tilt_angle - 30)
    arcade.draw_ellipse_filled(position_x, position_y - 30, 5, 10, (61, 59, 59), tilt_angle - 175)
    arcade.draw_ellipse_filled(position_x - 20, position_y - 15, 5, 10, (61, 59, 59), tilt_angle + 70)
    arcade.draw_arc_filled(position_x + 18, position_y - 88, 30, 40, (54, 51, 52), 90, 270)


WIDTH_1 = 40
HEIGHT_1 = 13
START_ANGLE = 0
END_ANGLE = 180


def draw_nose_cone(position_x, position_y):
    arcade.draw_ellipse_filled(position_x + 105, position_y - 3, WIDTH + 25, HEIGHT_1 - 5, (224, 188, 40))
    arcade.draw_ellipse_outline(position_x + 105, position_y - 3, WIDTH + 25, HEIGHT_1 - 5, (121, 123, 128), 2)
    point_list_1 = ((position_x, position_y),
                    (position_x + 35, position_y + 45),
                    (position_x + 185, position_y + 45),
                    (position_x + 215, position_y))
    arcade.draw_polygon_filled(point_list_1, (203, 214, 214))
    arcade.draw_polygon_outline(point_list_1, (121, 123, 128), 4)

    arcade.draw_arc_filled(position_x + 112, position_y + 92, WIDTH_1, HEIGHT_1, (203, 214, 214), START_ANGLE,
                           END_ANGLE)
    arcade.draw_arc_outline(position_x + 112, position_y + 92, WIDTH_1, HEIGHT_1, (121, 123, 128), START_ANGLE,
                            END_ANGLE, 4)


def draw_nose_cone_1(position_x, position_y):
    point_list = ((position_x, position_y),
                  (position_x + 35, position_y + 45),
                  (position_x + 120, position_y + 45),
                  (position_x + 150, position_y))
    arcade.draw_polygon_filled(point_list, (203, 214, 214))
    arcade.draw_polygon_outline(point_list, (121, 123, 128), 4)


WIDTH_2 = 30
HEIGHT_2 = 65
BORDER_WIDTH_2 = 3


def draw_door(position_x, position_y):
    arcade.draw_rectangle_outline(position_x, position_y, WIDTH_2, HEIGHT_2, (121, 120, 120), BORDER_WIDTH_2)
    arcade.draw_rectangle_outline(position_x, position_y - 15, WIDTH_2 - 15, HEIGHT_2 - 38, (121, 120, 120),
                                  BORDER_WIDTH_2 - 1)
    arcade.draw_rectangle_outline(position_x, position_y + 21, WIDTH_2 - 15, HEIGHT_2 - 55, (121, 120, 120),
                                  BORDER_WIDTH_2 - 1)
    arcade.draw_rectangle_outline(position_x, position_y + 22.7, WIDTH_2 - 15, HEIGHT_2 - 60, (121, 120, 120),
                                  BORDER_WIDTH_2 - 2)
    arcade.draw_rectangle_outline(position_x, position_y - 19.3, WIDTH_2 - 15, HEIGHT_2 - 60, (121, 120, 120),
                                  BORDER_WIDTH_2 - 2)


def draw_earth():
    # Draw earth below the spaceship
    # show diferent layers of colors in the atmosphere
    arcade.draw_arc_filled(300, 0, 600, 180,
                           (42, 108, 140), 0, 215, -10)
    arcade.draw_arc_filled(300, 0, 600, 165,
                           (58, 139, 166), 0, 215, -10)
    # Show body of land on earth
    point_list = ((0, 0),
                  (0, 100),
                  (40, 120),
                  (80, 130),
                  (110, 140),
                  (150, 150),
                  (180, 140),
                  (230, 150),
                  (300, 140),
                  (380, 135),
                  (430, 90),
                  (450, 70),
                  (600, 0))
    arcade.draw_polygon_filled(point_list, (117, 161, 125))

def on_draw(delta_time):
    arcade.start_render()
    # Draw the center and nose cone of spacecraft plus add details
    draw_trunk(350, 326)
    draw_table_rows(355, 350)
    draw_details(265, 380, 20)
    draw_arcdetails(435, 380, 20)
    draw_nose_cone(245, 405)
    draw_nose_cone_1(280, 450)

    # Left side, solar panels.
    draw_solar_panels(211, 310)
    draw_solar_panels(156, 310)
    draw_solar_panels(101, 310)
    draw_solar_panels(46, 310)
    # Right side, solar panels.
    draw_solar_panels(489, 310)
    draw_solar_panels(544, 310)
    draw_solar_panels(599, 310)
    draw_solar_panels(654, 310)

    # Load image of spacex and dragon
    file_name = "SpaceX-Logo.svg.png"
    texture = arcade.load_texture(file_name)
    scale = .05
    arcade.draw_texture_rectangle(365, 488, scale * texture.width,
                                  scale * texture.height, texture)

    file_name = "LOGO-MagicDragon.png"
    texture = arcade.load_texture(file_name)
    scale = .4
    arcade.draw_texture_rectangle(350, 280, scale * texture.width,
                                  scale * texture.height, texture)
    draw_door(355, 440)
    draw_earth()

    file_name = "How-to-Draw-Occupation-An-Astronaut-final-step-215x382.png"
    texture = arcade.load_texture(file_name)
    scale = .4
    arcade.draw_texture_rectangle(on_draw.center_x, on_draw.center_y, scale * texture.width,
                                  scale * texture.height, texture)

    on_draw.center_x += on_draw.delta_x * delta_time
    on_draw.center_y += on_draw.delta_y * delta_time

    if on_draw.center_x < 100:
        on_draw.delta_x = on_draw.delta_x * - 1
    if on_draw.center_x > 600:
        on_draw.delta_x = on_draw.delta_x * - 1

    if on_draw.center_y > 185:
        on_draw.delta_y = on_draw.delta_y * - 1
    if on_draw.center_y < 500:
        on_draw.delta_y = on_draw.delta_y * - 1


on_draw.center_x = 350
on_draw.center_y = 300
on_draw.delta_x = 50
on_draw.delta_y = 50


def main():
    arcade.open_window("SpaceX Dragon", 700, 600)
    arcade.set_background_color(1, 8, 8)
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()

if __name__ == "__main__":
    main()