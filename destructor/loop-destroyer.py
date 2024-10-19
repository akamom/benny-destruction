from PIL import Image
from glitch import Glitch
from glitch_this import ImageGlitcher
import time
from random import randrange

def load_image(path):
    image = Image.open(path)
    return image.convert('RGB')

def reset():
    original_image = load_image('../ui/src/data/original.jpg')
    original_image.save('../ui/src/data/destroyme.jpg', 'JPEG')

if __name__ == "__main__":
    reset()
    glitcher = ImageGlitcher()
    original_image = load_image('../ui/src/data/frida.jpg')
    destroy_image = load_image('../ui/src/data/frida.jpg')
    manipulator = Glitch(0.008, 0.3, 0.05, destroy_image)

    glitch_img = destroy_image
    max_iterations = 3000
    for i in range(max_iterations):
        if (i % 100 == 0):
            print(f'{i}/{max_iterations}')
        # manipulator.randomise()
        # manipulator.execute()
        glitch_img = glitcher.glitch_image(glitch_img, 2, color_offset=True, scan_lines=False)

        glitch_img.save('../ui/src/data/test.jpg', 'JPEG')
        time.sleep(5)