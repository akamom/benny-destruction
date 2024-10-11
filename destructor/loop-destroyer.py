from PIL import Image
from glitch import Glitch
from difference import Differencer
from compression import Compressor

def load_image(path):
    image = Image.open(path)
    return image.convert('RGB')

def reset():
    original_image = load_image('../ui/src/data/original.jpg')
    original_image.save('../ui/src/data/destroyme.jpg', 'JPEG')

if __name__ == "__main__":
    reset()
    original_image = load_image('../ui/src/data/original.jpg')
    destroy_image = load_image('../ui/src/data/destroyme.jpg')
    manipulator = Glitch(0.008, 0.3, 0.05, destroy_image)
    compressor = Compressor(20, 20)
    
    compressed_original_image = compressor.execute(original_image)
    compressed_destroy_image = compressor.execute(destroy_image)

    for i in range(30000):
        manipulator.randomise()
        manipulator.execute()
        
        compressed_image_new = compressor.execute(destroy_image)
        differencer = Differencer(compressed_original_image, compressed_image_new)
        diff = differencer.execute()
        
        with open("../ui/public/myfile.txt", "w") as file:
            for hex_string in diff:
                file.write(hex_string + '\n')
        destroy_image.save('../ui/src/data/destroyme.jpg', 'JPEG')
    
#     ^CTraceback (most recent call last):
#   File "/home/moritz/programming/repositories/image-manipulator/destructor/loop-destroyer.py", line 26, in <module>
#     manipulator.execute()
#   File "/home/moritz/programming/repositories/image-manipulator/destructor/glitch.py", line 50, in execute
#     self.pixel_map[current_width,current_height] = new_pixel_value
#     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# KeyboardInterrupt