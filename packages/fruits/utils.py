import os

from cytoolz import pipe

import pygame


def fix_path(path):
    return pipe(path
                , os.path.expanduser
                , os.path.abspath)


BASE_PATH = os.path.dirname(__file__)
IMAGE_DIR = fix_path(os.path.join(BASE_PATH, '../../sprites'))


def load_image(image: str) -> pygame.Surface:
    return pygame.image.load(fix_path(os.path.join(IMAGE_DIR, image)))
