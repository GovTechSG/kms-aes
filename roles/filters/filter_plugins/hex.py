import base64
import os

def base64_to_hex(encoded):
    """Convert base64 to hex"""
    return base64.b64decode(encoded).hex()

def random_bytes(length):
    """Return random bytes in hex"""
    return os.urandom(length).hex()

class FilterModule(object):
    """
    Custom module for hex operations
    """

    def filters(self):
        return {
            "base64_to_hex": base64_to_hex,
            "random_bytes": random_bytes
        }
