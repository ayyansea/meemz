from PIL import Image, ImageDraw

"""
Generator steps:
* calculate size of all components
* create a canvas of a default/specified size
* generate components
* put components onto canvas
* return complete image
"""


class Generator:
    def __init__(self, config,
                size = (1100, 1100), deepfry = False,
                jpeg = False, source = None,
                output = None, theme = "dark"
                ):

        self.__config = config
        self.__size = size
        self.__color = config.get_colors()[theme]
        self.__jpeg = jpeg
        self.__deepfry = deepfry
        self.__source = source
        self.__output = output

        self.__image = self.__create_canvas()

        self.__components = self.__config.get_components()
        self.__sizes = self.__calculate()
        self.__gen_components = self.__generate_components()

    
    def __calculate(self):
        sizes = {}

        for component in self.__components:
            width = component.get_width() / 100
            height = component.get_height() / 100
            name = component.get_name()

            calc_width = int(self.__size[0] * width)
            calc_height = int(self.__size[1] * height)

            sizes[name] = (calc_width, calc_height)

        return sizes


    def __create_canvas(self):
        return Image.new("RGB", self.__size, self.__color)


    def __generate_components(self):
        images = []

        for component in self.__components:
            name = component.get_name()
            size = self.__sizes[name]
            color = component.get_local_color()

            current = Image.new("RGB", size, color)
            images.append(current)

        return images


    def __combine(self):
        coords = (0, 0)
        
        for component in self.__gen_components:
            self.__image.paste(component, coords)
            coords = (0, coords[1] + component.size[1])


    def save_canvas(self):
        self.__combine()
        self.__image.save("/home/ayya/Github/meemz/test.png")