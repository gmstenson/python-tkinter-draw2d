# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from tkinter import X
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call all drawing functions
    # Draw the sky
    draw_sky(canvas, scene_width, scene_height)

    # Draw the stars
    draw_stars(canvas, scene_height, scene_width)

    # Draw big cloud 1
    center_x = 20
    cloud_bottom = 420
    for i in range(2):
        draw_cloud(canvas, center_x, cloud_bottom)
        center_x += 150

    # Draw the moon
    center_x = 320
    moon_bottom = 380
    draw_moon(canvas, center_x, moon_bottom)

    # Draw big cloud 2
    center_x = 400
    cloud_bottom = 400
    for i in range(2):
        draw_cloud(canvas, center_x, cloud_bottom)
        center_x += 150

    # Draw medium cloud
    center_x = 180
    cloud_bottom = 365
    draw_cloud(canvas, center_x, cloud_bottom)

    # Draw small clouds
    center_x = 80
    cloud_bottom = 365
    for i in range(2):
        draw_small_cloud(canvas, center_x, cloud_bottom)
        center_x += 400

    # Draw mountains
    draw_mountains(canvas)

    # Draw mountain foothills
    draw_foothills(canvas)

    # Draw Y on the mountain
    draw_Y(canvas)

    # Draw ground
    draw_ground(canvas, scene_width, scene_height)

    # Draw trees
    tree_center_x = 160
    tree_bottom = 25
    tree_height = 70
    for i in range(12):
        draw_trees(canvas, tree_center_x,
            tree_bottom, tree_height)
        tree_center_x += 28

    # Draw more trees
    tree_center_x = 600
    tree_bottom = 25
    tree_height = 70
    for i in range(2):
        draw_trees(canvas, tree_center_x,
            tree_bottom, tree_height)
        tree_center_x += 40

    # Draw small tree 1
    tree_center_x = 760
    tree_bottom = 70
    tree_height = 50
    draw_small_trees(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw small tree 2
    tree_center_x = 710
    tree_bottom = 75
    tree_height = 50
    draw_small_trees(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw small tree 3
    tree_center_x = 25
    tree_bottom = 68
    tree_height = 50
    draw_small_trees(canvas, tree_center_x, tree_bottom, tree_height)

    # Add a signature
    center_x = 775
    center_y = 485
    text = "GMS"
    draw_message(canvas, center_x, center_y, text)

    # Call the finish_drawing function
    finish_drawing(canvas)


# Define all functions here
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 100 / 3,
        scene_width, scene_height, width=0, fill="pink")

def draw_moon(canvas, center_x, moon_bottom):

    moon_width = center_x + 125
    moon_height = moon_bottom + 125
    draw_oval(canvas, center_x, moon_bottom, moon_width, 
            moon_height, outline="indianred2", fill="indianred2")

def draw_cloud(canvas, center_x, cloud_bottom):

    cloud_width = center_x + 200
    cloud_height = cloud_bottom + 40
    draw_oval(canvas, center_x, cloud_bottom, cloud_width, 
            cloud_height, outline="mistyrose1", fill="mistyrose1")

def draw_small_cloud(canvas, center_x, cloud_bottom):

    cloud_width = center_x + 80
    cloud_height = cloud_bottom + 20
    draw_oval(canvas, center_x, cloud_bottom, cloud_width, 
        cloud_height, outline="mistyrose2", fill="mistyrose2")

def draw_Y(canvas):
    draw_line(canvas, 580, 245, 585, 235, width=5, fill="lavenderblush1")
    draw_line(canvas, 576, 245, 585, 245, width=4, fill="lavenderblush1")
    draw_line(canvas, 585, 235, 592, 245, width=5, fill="lavenderblush1")
    draw_line(canvas, 587, 245, 596, 245, width=4, fill="lavenderblush1")
    draw_line(canvas, 585, 235, 584, 225, width=5, fill="lavenderblush1")
    draw_line(canvas, 580, 225, 589, 225, width=4, fill="lavenderblush1")

def draw_foothills(canvas):

    draw_polygon(canvas, -150, 0, 50, 180, 150, 160,
            250, 180, 350, 150, 450, 190, 550, 170, 650, 190, 1200, 0, 
            outline="firebrick2", width=1, fill="firebrick2")
    draw_polygon(canvas, -150, 0, 100, 150, 200, 130,
            300, 150, 450, 110, 600, 160, 1000, 0, 
            outline="firebrick3", width=1, fill="firebrick3")  
    draw_polygon(canvas, -150, 0, 50, 100, 150, 80,
            270, 120, 370, 80, 540, 110, 620, 90, 750, 100, 1000, 0, 
            outline="firebrick", width=1, fill="firebrick")

def draw_mountains(canvas):

    draw_polygon(canvas, -500, 0, 200, 340, 1000, 0, 
            outline="indianred1", width=1, fill="indianred1")
    draw_polygon(canvas, 0, 0, 600, 360, 615, 340, 630, 350, 1000, 0, 
            outline="indianred2", width=1, fill="indianred2")

def draw_ground(canvas, scene_width, scene_height):

    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 12, width=0, fill="firebrick4")
    draw_arc(canvas, 400, -70, 900, 80, extent=180, width=1,
        outline="firebrick4", fill="firebrick4")
    draw_arc(canvas, -100, -30, 200, 70, extent=180, width=1, 
        outline="firebrick4", fill="firebrick4")
    draw_arc(canvas, 0, -30, 800, 30, extent=180, width=1, 
        outline="gray22", fill="gray22")

def draw_small_trees(canvas, center_x, bottom, height):

    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="firebrick4", width=1, fill="firebrick4")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="firebrick4", width=1, fill="firebrick4")

def draw_trees(canvas, center_x, bottom, height):

    trunk_width = height / 12
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray22", width=1, fill="gray22")

    skirt_width = height / 3
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray22", width=1, fill="gray22")

def draw_stars(canvas, scene_height, scene_width):
    
    diameter = 1
    for i in range(300):
        x = random.randint(0, scene_width)
        y = random.randint(0, scene_height)
        draw_oval(canvas, x, y, x + diameter, y + diameter, 
                outline="lavenderblush1", fill="lavenderblush1")

def draw_message(canvas, center_x, center_y, text):
    draw_text(canvas, center_x, center_y, text, fill="gray22")

# Call the main function
main()