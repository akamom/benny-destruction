import random

color_1=(255,0,0)
color_2=(0,255,0)
color_3=(0,0,255)
colors=[color_1,color_2,color_3]

def create_stripes(width, height, pixel_map, num_stripes):
    color = colors[random.randrange(0, 3)]
    random_orientation = random.randrange(0,2)

    for _ in range(num_stripes):
        create_stripe(random_orientation, width, height, pixel_map, color)

def create_stripe(random_orientation, width, height, pixel_map, color):
    if random_orientation == 0:
        random_height = random.randrange(1, height)
        for current_pixel in range(width):
            pixel_map[current_pixel,random_height] = color
    else:
        random_width = random.randrange(1, width)
        for current_pixel in range(height):
            pixel_map[random_width,current_pixel] = color