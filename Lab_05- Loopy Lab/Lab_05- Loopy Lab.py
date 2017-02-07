import arcade

# Create a window
arcade.open_window("Lab 05 - Loopy Lab", 1200, 600)

arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

arcade.start_render()

# Draw squares on bottom
arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

# Draw squares on top
arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)

# Section 1
for row in range(30):
    for column in range(30):
        x = 5 + (10 * row)  # Instead of zero, calculate the proper x location using row
        y = 5 + (10 * column) # Instead of zero, calculate the proper y location using column
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


# Section 2
# Use the modulus operator and an if statement to select the color
for row in range(30):
    for column in range(30):
        x = 305 + (10 * row)
        y = 5 + (10 * column)
        if row % 2 == 0:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
        else:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

# Section 3
# Use the modulus operator and an if statement to select the color
for column in range(30):
    for row in range(30):
        x = 605 + (10 * row)
        y = 5 + (10 * column)
        if column % 2 == 0:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
        else:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

# Section 4
# Use the modulus operator and an if statement to select the color
for column in range(30):
    for row in range(30):
        x = 905 + (10 * row)
        y = 5 + (10 * column)
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
        if column % 2 == 0 and row % 2 == 0:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
        else:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

# Section 5
for column in range(30):
    for row in range(column + 1):
        x = 5 + (10 * column)
        y = 305 + (10 * row)
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 6
for row in range(30):
    for column in range(row + 1):
        x = 305 + (10 * column)
        y = 595 - (10 * row)
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 7
for row in range(30):
    for column in range(row + 1):
        x = 605 + (10 * column)
        y = 305 + (10 * row)
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 8
for row in range(30):
    for column in range(row + 1):
        x = 905 + (10 * row)
        y = 595 - (10 * column)
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
        if column % 2 == 0:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
arcade.finish_render()

arcade.run()