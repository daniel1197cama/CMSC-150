import arcade

def draw_basketball():
    arcade.draw_circle_filled(250, 100, 50, (165, 170, 173))
    arcade.draw_circle_outline(250, 100, 50, (126, 130, 133))

arcade.open_window("Hubble Space Telescope", 600, 600)

# Remember to change background color to space black.
arcade.set_background_color((1, 8, 8))
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(190, 400, 400, 250, (203, 214, 214))

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
# Draw eclipse filled
arcade.draw_ellipse_filled(295, 402, 7, 105,
                           (224, 188, 40), 90)
# draw spaceship upper part
point_list = ((198, 405),
              (250, 440),
              (254, 440),
              (300, 440),
              (350, 440),
              (400, 405))
arcade.draw_polygon_filled(point_list, (203, 214, 214))

point_list = ((198, 405),
              (250, 440),
              (254, 440),
              (300, 440),
              (350, 440),
              (400, 405))
arcade.draw_polygon_outline(point_list, (121, 123, 128), 5)

draw_basketball()



arcade.finish_render()
arcade.run()
