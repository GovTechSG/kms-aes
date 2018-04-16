import base64
import codecs
import os


# From https://stackoverflow.com/a/46878633
def base64_to_hex(encoded):
    """Convert base64 to hex"""
    decoded = base64.b64decode(encoded)
    b_string = codecs.encode(decoded, 'hex')
    return b_string.decode('utf-8').upper()


def random_bytes(length):
    """Return random bytes in hex"""
    bytes = os.urandom(length)
    b_string = codecs.encode(bytes, 'hex')
    return b_string.decode('utf-8').upper()


class FilterModule(object):
    """
    Custom module for hex operations
    """

    def filters(self):
        return {
            "base64_to_hex": base64_to_hex,
            "random_bytes": random_bytes
        }
