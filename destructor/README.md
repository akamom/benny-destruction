# Destructor
Destroyes a given JPEG in several iterations.

## Requirements
- Python 3
- Pip 3

## Setup
1. First create a Python virtual environment in the project (Destructor) root:
    ```bash
    python -m venv <PATH_TO_REPOSITORY>/destructor/.venv
    ```
2. Start the virtual environment:
    ```bash
    source <PATH_TO_REPOSITORY>/destructor/.venv/bin/activate
    ```
    If you are using a non UNIX OS please check out, [this page](https://docs.python.org/3/library/venv.html).
3. Install dependencies:
    ```bash
    pip install -r <PATH_TO_REPOSITORY>/destructor/requirements.txt 
    ```

You can stop the virtual environment at any point with the `deactivate` command.

## Run a script
Please first activate the virtual environment:
```bash
source <PATH_TO_REPOSITORY>/destructor/.venv/bin/activate
```

The main entry point of the project is the `jpeg-destroyer.py` script. To execute it, please run:
```
python <PATH_TO_REPOSITORY>/destructor/jpeg-destroyer.py
```

## Prepare run
1. Set the following state [here](../state.json) to:
```json
{
    "stageNewImage": true,
    "iteration": 0
}
```
    - stageNewImage: If true a new image is staged for destruction, if false, the current staged images is used
    - iteration: The iteration which was saved. The destruction begins from this iteration instead from the beginning.
2. Add JPEG files to the following folder: `PROJECT_ROOT/not_destroyed_images/`
3. Configure your run on the [loop-destroyer.py](./loop-destroyer.py).
```python
file_ending = '.jpg' # The ending of the JPEG files inside the not_destroyed_images folder
data_folder = '../not_destroyed_images' # Images in this folder are randomly destroyed
destroyed_folder = '../destroyed_images' # Fully destroyed images are stored here
image_path_destroyme = '../ui/src/data/destroyme.jpg' # Image which is currently getting destroyed
image_path_original = '../ui/src/data/original.jpg' # Original image for calculating the diff
state_json_folder = '../state.json' # Used for loading and saving the current state

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
```