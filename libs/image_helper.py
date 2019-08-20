import os
import re
from werkzeug.datastructures import FileStorage

from flask_uploads import UploadSet, IMAGES

IMAGE_SET = UploadSet("images", IMAGES) ## set of allowed extensions

def save_image(image: FileStorage, folder: str=None, name: str=None):
    """Takes FileStorage, name of the folder & file and save it"""
    return IMAGE_SET.save(image, folder, name)


def get_path(filename: str = None,folder: str = None):
    """Returns image file path"""
    return IMAGE_SET.path(filename, folder)


def find_image_any_format(filename: str,folder: str):
    """Takes a filename an returns image of any of the accepted formats"""
    for _format in IMAGES:
        image = f"{filename}.{_format}"
        image_path = IMAGE_SET.path(filename=image, folder=folder)
        # Check if file exists with .isfile
        if os.path.isfile(image_path):
            return image_path
    return None

def _retrieve_filename(file):
    """Check if file is instance of FileStorage, allows functions to use both filenames and FileStorages in order to
    retrieve a file name"""
    if isinstance(file, FileStorage):
        return file.filename
    return file

def is_filename_safe(file):
    """Regex check if string matches"""
    filename = _retrieve_filename(file)

    allowed_format = "|".join(IMAGES)  # png|svg|jpeg|jpg|jpe - pipe stands for or in regex
    regex = f"^[a-zA-Z0-9][a-zA-Z0-9_()-\.]*\.({allowed_format})$"  # first char, sec char, any other char, dot, allowed extension, end of the string $
    return re.match(regex, filename) is not None


def get_basename(file):
    """Returns full image file name"""
    filename = _retrieve_filename(file)
    return os.path.split(filename)[1]


def get_extension(file):
    """Returns file extension"""
    filename = _retrieve_filename(file)
    return os.path.splitext(filename)[1]