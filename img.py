#!/usr/bin/env python
from PIL import Image,ImageDraw
from math import ceil, cos, sin, radians
MAX_LVL = 8

dim = (1000, 1000)
origin = (dim[0] / 2, dim[1] / 2)
angle_to_coor = lambda angle, radius: (origin[0] + radius * cos(radians(angle)), origin[1] + radius * sin(radians(angle)))
lvl_to_rad = lambda lvl: 50 + lvl * 40

def box(x, y, padding=10):
    return (x-padding, y-padding, x+padding, y+padding)

def drawing(draw, prior, o_x, o_y, begin_angle, rem_angle, lvl=0):
    radius = lvl_to_rad(lvl)

    left_angle  = begin_angle-rem_angle
    right_angle = begin_angle+rem_angle

    left = angle_to_coor(left_angle, radius)
    middle = angle_to_coor(begin_angle, radius)
    right = angle_to_coor(right_angle, radius)

    # int(255 * lvl / MAX_LVL)
    stroke_colour = (0, 255-(255 * lvl / (MAX_LVL+1)),255-(255 * lvl / (MAX_LVL+1)))

    draw.line(prior+middle, fill=stroke_colour)
    if lvl == MAX_LVL:
        return
    b = box(o_x, o_y, padding=radius)
    draw.arc(b, left_angle, right_angle, fill=stroke_colour)

    # draw circles
    # b = box(left[0], left[1], padding=2)
    # draw.ellipse(b, fill=stroke_colour)
    #draw.arc(b, 0, 360, fill=stroke_colour)
    # b = box(right[0], right[1], padding=2)
    # draw.ellipse(b, fill=stroke_colour)
    #draw.arc(b, 0, 360, fill=stroke_colour)

    remaining = int(ceil(rem_angle / 2.))

    drawing(draw, left, o_x, o_y, begin_angle-rem_angle, remaining, lvl+1)
    drawing(draw, right, o_x, o_y, begin_angle+rem_angle, remaining, lvl+1)

def create_shape(begin=0, degrees=90):
    img = Image.new('RGB', dim, 'black')
    draw = ImageDraw.Draw(img)

    drawing(draw, origin, origin[0], origin[1], begin, degrees)
    draw.arc(box(*origin, padding=lvl_to_rad(MAX_LVL)), 0 , 360, fill=(0xff,0xff,0xff))
    img.save("img-%03d.png" % degrees)
    return img

# img = create_shape(0, 90)
# img.show()
[create_shape(i, i) for i in range(0, 361, 2)]
