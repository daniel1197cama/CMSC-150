import arcade
arcade.open_window("Hubble Space Telescope", 600,600)

#Remember to change background color to space black.
arcade.set_background_color((1,8,8))
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(190,400,400,250,(203,214,214))
arcade.draw_lrtb_rectangle_filled(180,190,300,290,(203,214,214))
arcade.draw_lrtb_rectangle_filled(400,410,300,290,(203,214,214))

#Solar panels
arcade.draw_lrtb_rectangle_filled(00,190,300,290,(203,214,214))



arcade.draw_circle_filled(250,100,50,(165,170,173))
arcade.draw_circle_outline(250,100,50,(126,130,133))








arcade.finish_render()
arcade.run()