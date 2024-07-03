from PIL import Image
from glitch import Glitch

def load_image():
    input_image = Image.open('./test-3.jpg')
    return input_image.convert('RGB')

def create_new_images(input_image, num_new_images, manipulator):
    for i in range(num_new_images):
        print(f"Create Image: {i}")
        manipulator.randomise()
        manipulator.execute()

        if (i == num_new_images-1):
            input_image.save(f"./modified_image_{i}.jpg", 'JPEG')

if __name__ == "__main__":
    image = load_image()
    manipulator = Glitch(0.008, 0.3, 0.05, image)
    create_new_images(image, 10, manipulator)