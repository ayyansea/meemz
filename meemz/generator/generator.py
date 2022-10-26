from PIL import Image
from abc import ABC, abstractmethod

"""
Generator steps:
* calculate size of all components
* create a canvas of a default/specified size
* generate components
* put components onto canvas
* return complete image
"""

class Generator(ABC):

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def create_canvas(self):
        pass

    @abstractmethod
    def generate_components(self):
        pass

    @abstractmethod
    def compile_canvas(self):
        pass

    @abstractmethod
    def return_canvas(self):
        pass