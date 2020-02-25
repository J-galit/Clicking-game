import arcade
import math
import random

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.BLACK)

# Initialize your variables here
circle_x = WIDTH//2
circle_y = HEIGHT//2
circle_radius = 100
Area = circle_radius * circle_radius * 3.14
y = 0
x = 0
r = 13
DE = math.sqrt((circle_x - x)**2 + (circle_y - y)**2)
c = 0
colour = arcade.color.RED
color_toggle = False
t = c + 2





@window.event("on_draw")
def game_loop():
    # import global variables here.
    global circle_radius, color, color_toggle
    global r, colour
    # update your variables here.
    if color_toggle:
        colour = arcade.color.RED
        color_toggle = False
    # Draw things here.
    arcade.start_render()
    
    arcade.draw_circle_filled(x, y, r, arcade.color.RED)
    arcade.draw_circle_filled(circle_x, circle_y, circle_radius, colour)
    arcade.draw_text(f"{c}", 100, 10, arcade.color.WHITE, 24)
       
    r = r + 0.1
   
@window.event
def on_mouse_press(mouse_x, mouse_y, button, modifiers):

    global circle_radius, circle_x, circle_y
    global r, x, y, c, colour, t
    
    
    if button == arcade.MOUSE_BUTTON_LEFT:
        d = math.sqrt((mouse_x - circle_x)**2 + (mouse_y - circle_y)**2)
        color_toggle = True
        
        if d < circle_radius:
            colour = arcade.color.BLUE
            circle_x = random.randint(0, 750)
            circle_y = random.randint(0,580)
            print(c)
            c = c + 1
            if circle_radius <= 1:
                circle_radius = 100
            if c % 2 == 0:
                colour = arcade.color.RED
       
arcade.run()