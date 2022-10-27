import argparse
from config import Config

parser = argparse.ArgumentParser(description='meemz options')

def main():
    """
    Running meemz without arguments should launch an interactive
    version of this application.

    Meemz can also be used as a standalone application for
    scripting, so it has following available arguments:
    
    @arg -t / --template: specify the meme template ("twitter", etc)
        default: twitter
    @arg -s / --size: size of the resulting image (format: w,h)
        default: 1100,1100
    @arg -D / --deep-fry: apply deep-frying to the resulting image
        default: none (false)
    @arg -J / --jpeg: has nothing to do with file format, just
                      makes the meme look very poor
        default: none (false)
    @arg -i / --image: specify source image (absolute/relative path)
        default: none
    @arg -o / --output: specify output file (absolute/relative path)
        default: ./meemz_out.jpg
    @arg -O / --opt: a specific option for chosen template (--opt k=v)
        default: none
        global:
        * variant ()
    @arg -c / --color: meme color scheme (light, dark); if supported
        default: dark

    ...more to come?
    """
    pass


def calculate_canvas(config):
    pass


if __name__ == "__main__":
    config = Config("twitter")
    calculate_canvas(config)