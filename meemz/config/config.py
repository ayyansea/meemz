from yaml import safe_load, YAMLError
from os import getenv
from enum import Enum

HOME = getenv("HOME")
XDG_CONFIG_DIR = HOME + "/Github/meemz/meemz/templates"


"""
Main config components:

@color [list]: background/theme variants (light, dark)
    @variant [str]

@font [str]: font to use globally or inside components

@components [dict]: parts of the image with sizes, alignment and fonts
    @component [dict]
        @width  [num]: %
        @height [num]: %
        @font   [str]
        @align  [str]: right, left, center

Font size is calculated automatically.
"""


class Component:
    """
    Holds information about a template component.
    """

    def __init__(self, component_name: str, props: dict):
        self.__name: str = component_name
        self.__props: dict = props


    def get_name(self) -> str:
        return self.__name


    def get_width(self) -> int:
        try:
            return self.__props["width"]
        except KeyError:
            return 100

    
    def get_height(self) -> int:
        try:
            return self.__props["height"]
        except KeyError:
            return 100


    def get_local_font(self) -> str:
        try:
            return self.__props["font"]
        except KeyError:
            return ""


    def get_align(self) -> str:
        try:
            return self.__props["align"]
        except KeyError:
            return "center"
        

class Config:
    """
    Holds the name of a template, dict representation
    of it's .yaml specification and distinct fields.
    """

    def __init__(self, template_name: str):
        self.name: str = template_name
        self.config: dict = self.__parse()
        self.__colors: dict = self.__parse_colors()
        self.__global_font: str = self.__parse_global_font()
        self.__components: list = self.__parse_components()


    # TODO: Assert everything!


    def __parse(self) -> dict:
        with open(f"{XDG_CONFIG_DIR}/{self.name}.yaml", "r") as config:
            try:
                return safe_load(config)
            except YAMLError as e:
                print(e)


    def get_config(self):
        return self.config


    def __parse_colors(self):
        colors = {}

        for variant in self.config["colors"]:
            for name, value in variant.items():
                colors[name] = value

        return colors

    
    def __parse_global_font(self):
        return self.config["font"]


    def __parse_components(self):
        components = []

        for component in self.config["components"]:
            current = Component(component, self.config["components"][component])
            components.append(current)

        return components

    
    def get_colors(self):
        return self.__colors

    
    def get_global_font(self):
        return self.__global_font


    def get_components(self):
        return self.__components