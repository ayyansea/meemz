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