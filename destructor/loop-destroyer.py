from PIL import Image, ImageEnhance
from glitch_this import ImageGlitcher
import time

image_path_original = '../ui/src/data/original.jpg'
image_path_destroyme = '../ui/src/data/destroyme.jpg'

sleep_initial = 1
sleep_loop = 1

glitch_start = 0
glitch_end = 100
glitch_amount = 2 #  A number between 0.1 to 10.0
glitch_color_offset = True
glitch_scan_lines = False

pigment_degredation_start = 0
pigment_degredation_end = 999999999
pigment_degredation_grayscale = 0.988 # Reduce saturation (0 = grayscale, 1 = original color)
pigment_degredation_brightness = 1.0122  # Increase brightness (1 = original, >1 = brighter)

delete_original = False

def load_image(path):
    image = Image.open(path)
    return image.convert('RGB')

def reset():
    original_image = load_image(image_path_original)
    original_image.save(image_path_destroyme, 'JPEG')
    time.sleep(sleep_initial)
    
def degredate_pigments(image):
    enhancer = ImageEnhance.Color(image)
    faded_image = enhancer.enhance(pigment_degregation_grayscale)

    brightness_enhancer = ImageEnhance.Brightness(faded_image)
    return brightness_enhancer.enhance(pigment_degregation_brightness)

if __name__ == "__main__":
    reset()

    iteration = 0
    glitcher = ImageGlitcher()
    destroy_image = load_image(image_path_destroyme)
    while True:
        iteration += 1
        if (iteration % 100 == 0):
            print(f'{iteration}/inf')

        if (pigment_degregation_start <= iteration <= pigment_degregation_end):
            destroy_image = degredate_pigments(destroy_image)

        if (glitch_start <= iteration <= glitch_end):
            destroy_image = glitcher.glitch_image(destroy_image, glitch_amount, color_offset=glitch_color_offset, scan_lines=glitch_scan_lines)

        destroy_image.save(image_path_destroyme, 'JPEG')
        time.sleep(sleep_loop)
