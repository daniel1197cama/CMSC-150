import arcade
arcade.open_window("Hubble Space Telescope", 600,600)

#Remember to change background color to space black.
arcade.set_background_color((75,166,196))
arcade.start_render()
arcade.draw_circle_filled(250,300,50,(165,170,173))
arcade.draw_circle_outline(250,300,50,(126,130,133))








arcade.finish_render()
arcade.run()