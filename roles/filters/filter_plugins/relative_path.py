from os import path

def relative_from(subject, base):
    return path.relpath(subject, base)

class FilterModule(object):
    """
    Custom module to calculate relative paths
    """

    def filters(self):
        return {
            "relative_from": relative_from
        }
