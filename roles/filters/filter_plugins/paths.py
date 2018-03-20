import os

def relative_from(subject, base):
    return os.path.relpath(subject, base)

def parent_directory(subject):
    return os.path.abspath(os.path.join(subject, os.pardir))

class FilterModule(object):
    """
    Custom module for paths related stuff
    """

    def filters(self):
        return {
            "relative_from": relative_from,
            "parent_directory": parent_directory
        }
