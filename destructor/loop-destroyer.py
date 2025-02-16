from PIL import Image, ImageEnhance
from glitch_this import ImageGlitcher
import time
import os
import random
import shutil
import uuid
import json

file_ending = '.jpg'
data_folder = '../not_destroyed_images'
destroyed_folder = '../destroyed_images'
image_path_destroyme = '../ui/src/data/destroyme.jpg'
image_path_original = '../ui/src/data/original.jpg'
state_json_folder = '../state.json'

sleep_initial = 1
sleep_loop = 0.2

glitch_start = 0
glitch_end = 20
glitch_amount = 2 #  A number between 0.1 to 10.0
glitch_color_offset = True
glitch_scan_lines = False

pigment_degregation_start = 0
pigment_degregation_end = 20
pigment_degregation_grayscale = 0.94 # Reduce saturation (0 = grayscale, 1 = original color)
pigment_degregation_brightness = 1.04  # Increase brightness (1 = original, >1 = brighter)

def load_image(path):
    image = Image.open(path)
    return image.convert('RGB')

def save_staged_image():
    image_id = uuid.uuid4()
    image_save_path = f"{destroyed_folder}/{image_id}.jpg"
    shutil.copy(image_path_destroyme, image_save_path)

def build_state(stage_new_image, iteration):
    return {
        "stageNewImage": stage_new_image,
        "iteration": iteration
    }

def load_state():
    if not os.path.exists(state_json_folder):
        return {}
    
    try:
        with open(state_json_folder, "r") as file:
            content = file.read()
            return json.loads(content) if content else {}
    except json.JSONDecodeError:
        return {}

def save_state(new_state):
    with open(state_json_folder, "w") as json_file:
        json.dump(new_state, json_file, indent=4)

def is_empty_state(loaded_state):
    return not bool(loaded_state)

def stage_image(loaded_state):
    print(f"Stage image with following state: {json.dumps(loaded_state, indent=4)}")
    if (is_empty_state(loaded_state)):
        print('There is no state. Stage new image.')
        return
    if (not loaded_state['stageNewImage']):
        print('The state tells me not to load a new image.')
        return
    
    print('Stage a new random image.')
    jpeg_files = [f for f in os.listdir(data_folder) if f.lower().endswith(file_ending)]
    if not jpeg_files:
        raise FileNotFoundError("No JPEG files found in the source directory.")
    random_file = random.choice(jpeg_files)
    source_file_path = os.path.join(data_folder, random_file)
    shutil.copy(source_file_path, image_path_original)
    shutil.move(source_file_path, image_path_destroyme)
    
    # New image staged so start from the beginning (iteration=0)
    new_state = build_state(False, 0)
    save_state(new_state)
    print(f"Save state. After loading new staged image: {json.dumps(new_state, indent=4)}")
    time.sleep(2)
    
def degredate_pigments(image):
    enhancer = ImageEnhance.Color(image)
    faded_image = enhancer.enhance(pigment_degregation_grayscale)

    brightness_enhancer = ImageEnhance.Brightness(faded_image)
    return brightness_enhancer.enhance(pigment_degregation_brightness)

def destroy_image(loaded_state):
    glitcher = ImageGlitcher()
    destroy_image = load_image(image_path_destroyme)
    max_iterations = max(pigment_degregation_end, glitch_end)
    save_point = int(max_iterations*0.1)
    print(f"New destroy loop started with max iterations: {max_iterations}")
    
    loaded_iteration = 0
    if(not is_empty_state(loaded_state) and loaded_state['iteration']):
        loaded_iteration = loaded_state['iteration']
        max_iterations = max_iterations - loaded_iteration
        print(f'Saved state.iteration was loaded: {loaded_state['iteration']} ')
        print(f'Max iterations was decreased to {max_iterations}')
    
    for iteration in range(max_iterations):
        if (pigment_degregation_start <= iteration <= pigment_degregation_end):
            destroy_image = degredate_pigments(destroy_image)

        if (glitch_start <= iteration <= glitch_end):
            destroy_image = glitcher.glitch_image(destroy_image, glitch_amount, color_offset=glitch_color_offset, scan_lines=glitch_scan_lines)

        is_save_point = iteration % save_point == 0
        if (is_save_point):
            new_iteration = loaded_iteration + iteration
            new_state = build_state(False, new_iteration)
            print(f'Save state. Savepoint reached: {json.dumps(new_state, indent=4)}')
            save_state(new_state)
        
        destroy_image.save(image_path_destroyme, 'JPEG')
        time.sleep(sleep_loop)

if __name__ == "__main__":
    while True:
        loaded_state = load_state()
        stage_image(loaded_state)
        destroy_image(loaded_state)
        save_staged_image()
        new_state = build_state(True, 0)
        print(f"Save state. Finished image destruction: {new_state}")
        save_state(new_state)
