#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
from PIL import Image
import os

# decoration
print(stylize("\n---- | Manipulate colors of a picture | ----\n", fg("red")))

# class
class Manipulate:
    def __init__(self, filename, processes, path):
        self.filename = filename
        self.processes = processes
        self.path = path

    # output magic method
    def __repr__(self):
        self.manipulate_color(self.filename, self.processes, self.path)
        return stylize("\nProcess done >>> manipulated_image.png created\n", fg("red"))

    # methods
    def manipulate_color(self, filename, processes, path):
        for _ in range(processes):
            image = Image.open(filename)
            image = image.convert("RGB")
            pixel_data = image.load()

            color_to_change = tuple([int(i) for i in input("\nColor to change (in RGB notation): ").split(", ")])
            changed_color = tuple([int(i) for i in input("Color to change with (in RGB notation): ").split(", ")])
            for y in range(image.size[1]):
                for x in range(image.size[0]):
                    if pixel_data[x, y] == color_to_change:
                        pixel_data[x, y] = changed_color

        image.save(f"{path}/manipulated_image.png", quality=100, subsampling=0)

# main execution
if __name__ == "__main__":
    # user interaction
    path = input("Path of the file: ")
    os.system(f"cd {path}")
    f = input("Filename: ")
    p = int(input("How many colors to manipulate?\n"))

    print(Manipulate(f, p, path))
