import arcade

arcade.open_window("SpaceX Dragon", 600, 600)

# Set background color to space black and create the trunk.


arcade.start_render()
arcade.draw_lrtb_rectangle_filled(190, 400, 400, 250, (203, 214, 214))
arcade.draw_lrtb_rectangle_outline(190, 400, 400, 250, (121, 123, 128), 5)

# little squares 1
arcade.draw_lrtb_rectangle_filled(180, 190, 300, 290, (121, 123, 128))
arcade.draw_lrtb_rectangle_filled(400, 410, 300, 290, (121, 123, 128))

# First lateral Panels(left,right)
arcade.draw_lrtb_rectangle_filled(140, 180, 370, 250, (65, 88, 140))
arcade.draw_lrtb_rectangle_filled(410, 450, 370, 250, (65, 88, 140))
point_list = ((160, 280),
              (160, 340),
              (430, 280),
              (430, 340))
arcade.draw_points(point_list, (0, 0, 0), 10)
# little squares 2
arcade.draw_lrtb_rectangle_filled(130, 140, 300, 290, (121, 123, 128))
arcade.draw_lrtb_rectangle_filled(450, 460, 300, 290, (121, 123, 128))

# Second lateral panels
arcade.draw_lrtb_rectangle_filled(90, 130, 370, 250, (65, 88, 140))
arcade.draw_lrtb_rectangle_filled(460, 500, 370, 250, (65, 88, 140))
point_list = ((100, 280),
              (100, 340),
              (120, 280),
              (120, 340),
              (470, 280),
              (470, 340),
              (490, 280),
              (490, 340))
arcade.draw_points(point_list, (0, 0, 0), 10)
# little squares 3
point_list = ((85, 295),
              (505, 295))
arcade.draw_points(point_list, (121, 123, 128), 10)
# Third lateral panels
arcade.draw_lrtb_rectangle_filled(45, 85, 370, 250, (65, 88, 140))
arcade.draw_lrtb_rectangle_filled(505, 550, 370, 250, (65, 88, 140))
point_list = ((55, 280),
              (55, 340),
              (75, 280),
              (75, 340),
              (515, 280),
              (515, 340),
              (535, 280),
              (535, 340))
arcade.draw_points(point_list, (0, 0, 0), 10)
# little squares 4
point_list = ((40, 295),
              (555, 295))
arcade.draw_points(point_list, (121, 123, 128), 10)
# draw lines (Left side of solar panels)
arcade.draw_line(41, 370, 41, 295, (121, 123, 128), 8)
arcade.draw_line(41, 295, 41, 250, (121, 123, 128), 8)

arcade.draw_line(139, 370, 139, 295, (121, 123, 128), 8)
arcade.draw_line(139, 295, 139, 250, (121, 123, 128), 8)

arcade.draw_line(85, 370, 85, 295, (121, 123, 128), 5)
arcade.draw_line(85, 295, 85, 250, (121, 123, 128), 5)

# draw lines (right side of solar panels)
arcade.draw_line(554, 370, 554, 295, (121, 123, 128), 8)
arcade.draw_line(554, 295, 554, 250, (121, 123, 128), 8)

arcade.draw_line(451, 370, 451, 295, (121, 123, 128), 8)
arcade.draw_line(451, 295, 451, 250, (121, 123, 128), 8)

arcade.draw_line(505, 370, 505, 295, (121, 123, 128), 5)
arcade.draw_line(505, 295, 505, 250, (121, 123, 128), 5)
# Draw a yellow ellipse
arcade.draw_ellipse_filled(295, 402, 7, 105,
                           (224, 188, 40), 90)
arcade.draw_ellipse_outline(295, 402, 7, 105,
                           (121, 123, 128), 1, 90)
# draw spacecraft nose cone
point_list = ((195, 405),
              (225, 450),
              (370, 450),
              (400, 405))
arcade.draw_polygon_filled(point_list, (203, 214, 214))

point_list = ((195, 405),
              (225, 450),
              (370, 450),
              (400, 405))
arcade.draw_polygon_outline(point_list, (121, 123, 128), 4)

point_list = ((225, 450),
              (260, 495),
              (340, 495),
              (370, 450))
arcade.draw_polygon_filled(point_list, (203, 214, 214))

point_list = ((225, 450),
              (260, 495),
              (340, 495),
              (370, 450))
arcade.draw_polygon_outline(point_list, (121, 123, 128), 4)

# Load image of spacex and dragon
file_name = "C:\\Users\\Daniel Camacho\\Documents\\CMSC 150\\Lab 02-Draw a Picture\\SpaceX-Logo.svg.png"
texture = arcade.load_texture(file_name)
scale = .05
arcade.draw_texture_rectangle(310, 488, scale *texture.width,
                              scale * texture.height, texture)

file_name = "C:\\Users\\Daniel Camacho\\Documents\\CMSC 150\\Lab 02-Draw a Picture\\LOGO-MagicDragon.png"
texture = arcade.load_texture(file_name)
scale = .4
arcade.draw_texture_rectangle(300, 280, scale * texture.width,
                              scale * texture.height, texture)

# Draw tip of spaceship
arcade.draw_arc_filled(300, 497, 40, 13,
                       (203, 214, 214), 0, 180)
arcade.draw_arc_outline(300, 497, 40, 13,
                       (121, 123, 128), 0, 180,4)
# Draw the door and details with rectangles and arc commands
arcade.draw_rectangle_outline(300, 440, 30, 65, (121, 120, 120), 3)
arcade.draw_rectangle_outline(300, 430, 15, 30, (121, 120, 120), 2)
arcade.draw_rectangle_outline(300, 461, 15, 10, (121, 120, 120), 2)
arcade.draw_rectangle_outline(300, 462.70, 15, 5, (121, 120, 120), 1)
arcade.draw_rectangle_outline(300, 420.70, 15, 5, (121, 120, 120), 1)
arcade.draw_rectangle_outline(300, 350, 80, 65, (171, 171, 171), 1)
arcade.draw_rectangle_outline(300, 350, 80, 32.5, (171, 171, 171), 1)
arcade.draw_rectangle_outline(300, 350, 80, 15.5, (171, 171, 171), 1)
arcade.draw_rectangle_filled(300, 350, 10, 15.5, (30, 30, 30))

arcade.draw_arc_filled(398, 292, 30, 40,
                       (54, 51, 52), 90, 270)
arcade.draw_arc_filled(192, 292, 30, 40,
                       (54, 51, 52), 90, 270, 180)
# Right side ellipses
arcade.draw_ellipse_filled(380, 380, 5, 10, (61, 59, 59), 20)
arcade.draw_ellipse_filled(365, 365, 5, 10, (61, 59, 59), 90)
arcade.draw_ellipse_filled(380, 350, 5, 10, (61, 59, 59), 170)
# Left side ellipses
arcade.draw_ellipse_filled(210, 380, 5, 10, (61, 59, 59), 20)
arcade.draw_ellipse_filled(230, 365, 5, 10, (61, 59, 59), 90)
arcade.draw_ellipse_filled(210, 350, 5, 10, (61, 59, 59), 170)

# Draw earth below the spaceship
# show diferent layers of colors in the atmosphere
arcade.draw_arc_filled(300, 0, 600, 180,
                       (42, 108, 140), 0, 215, -10)
arcade.draw_arc_filled(300, 0, 600, 165,
                       (58, 139, 166), 0, 215, -10)
arcade.draw_arc_filled(300, 0, 600, 155,
                       (64, 137, 173), 0, 215, -10)
arcade.draw_arc_filled(300, 0, 600, 130,
                       (77, 134, 163), 0, 215, -10)
arcade.draw_arc_filled(300, 0, 600, 118,
                       (58, 139, 166), 0, 215, -10)
arcade.draw_arc_filled(300, 0, 600, 110,
                       (64, 137, 173), 0, 215, -10)

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

point_list = ((0, 0),
              (0, 90),
              (40, 110),
              (80, 120),
              (110, 130),
              (150, 140),
              (180, 130),
              (230, 140),
              (300, 130),
              (380, 125),
              (430, 80),
              (450, 60),
              (600, 0))
arcade.draw_polygon_filled(point_list, (107, 151, 115))

# Draw the amazon river and its branches
point_list = ((300, 0),
              (280, 50),
              (270, 70),
              (290, 100),
              (310, 120),
              (300, 140))
arcade.draw_line_strip(point_list, (126, 207, 205), 5)

point_list = ((280, 50),
              (270, 70),
              (260, 90),
              (255, 100),
              (240, 120),
              (210, 145))
arcade.draw_line_strip(point_list, (126, 207, 205), 5)

point_list = ((280, 50),
              (270, 70),
              (280, 90),
              (275, 100),
              (280, 120),
              (270, 145))
arcade.draw_line_strip(point_list, (126, 207, 205), 5)

point_list = ((280, 50),
              (240, 70),
              (230, 90),
              (220, 100),
              (200, 120),
              (190, 140))
arcade.draw_line_strip(point_list, (126, 207, 205), 5)

# Robotic arm in ISS
arcade.draw_rectangle_filled(550, 570, 20, 150, arcade.color.WHITE, 110)
arcade.draw_rectangle_filled(487, 500, 20, 100, arcade.color.WHITE, 180)
arcade.draw_rectangle_filled(472, 450, 10, 30, arcade.color.WHITE, 180)
arcade.draw_rectangle_filled(502, 450, 10, 30, arcade.color.WHITE, 180)


arcade.finish_render()
arcade.run()
