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