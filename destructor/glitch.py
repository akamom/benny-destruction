import random

class Glitch:

    def __init__(self, glitch_height_factor, width_base_factor, glitch_width_factor, image):
        self.pixel_map = image.load()
        self.width, self.height = image.size
        self.shift_width = int(self.width * glitch_width_factor)
        self.shift_height = int(self.height * glitch_height_factor)
        self.base_width = int(self.width * width_base_factor)

    def __create_shift_width(self):
        glitch_width = []

        for i in range(self.shift_width):
            current_width = self.base_width+i
            if current_width >= self.width:
                break
            glitch_width.append(current_width)

        return glitch_width

    def randomise(self):
        self.shift_width = int(self.width * random.uniform(0.002, 0.1))
        self.shift_height = int(self.height * random.uniform(0.01, 0.03))
        self.base_width = random.randint(0, self.width)

    def execute(self):
        last_shifted_height = self.height - self.shift_height
        shift_width_array = self.__create_shift_width()
        
        # print(f"Width: {self.width}, base_width: {self.base_width}, shift_width: {self.shift_width} Shift_Width_last: {shift_width_array[-1]}")
        # print(f"Heigt: {self.height}, shift_height: {self.shift_height}, last_shift_pixel: {last_shifted_height}")

        for current_height in range(self.height):
            for current_width in shift_width_array:

                if current_height < last_shifted_height:
                    glitch_height = current_height + self.shift_height
                    glitch_width = current_width
                else:
                    glitch_height = current_height + self.shift_height - self.height
                    glitch_width = current_width + self.shift_width + 1
                    
                if glitch_width >= self.width:
                    new_pixel_value = (0, 0, 0)
                else:
                    new_pixel_value = self.pixel_map[glitch_width,glitch_height]

                self.pixel_map[current_width,current_height] = new_pixel_value