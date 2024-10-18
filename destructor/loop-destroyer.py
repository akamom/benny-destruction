from PIL import Image
from glitch import Glitch
import time

def load_image(path):
    image = Image.open(path)
    return image.convert('RGB')

def reset():
    original_image = load_image('../ui/src/data/original.jpg')
    original_image.save('../ui/src/data/destroyme.jpg', 'JPEG')

if __name__ == "__main__":
    reset()
    original_image = load_image('../ui/src/data/frida.jpg')
    destroy_image = load_image('../ui/src/data/frida.jpg')
    manipulator = Glitch(0.008, 0.3, 0.05, destroy_image)

    for i in range(30000):
        manipulator.randomise()
        manipulator.execute()

        destroy_image.save('../ui/src/data/test.jpg', 'JPEG')
        time.sleep(3)