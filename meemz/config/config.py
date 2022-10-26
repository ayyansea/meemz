from yaml import safe_load, YAMLError
from os import getenv

HOME = getenv("HOME")
XDG_CONFIG_DIR = HOME + "/Github/meemz/meemz/templates"

class Config:
    """
    Holds the name of a template and a dict representation
    of it's .yaml specification.
    """

    def __init__(self, template_name: str):
        self.name: str = template_name
        self.config: dict = self.__parse()


    def __parse(self) -> dict:
        with open(f"{XDG_CONFIG_DIR}/{self.name}.yaml", "r") as config:
            try:
                return safe_load(config)
            except YAMLError as e:
                print(e)


    def get_config(self):
        return self.config