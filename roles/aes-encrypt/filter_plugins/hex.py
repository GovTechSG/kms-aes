import base64
import binascii
import os

def random_bytes(length):
    """Return random bytes in hex"""
    return binascii.hexlify(os.urandom(length))

class FilterModule(object):
    """
    Custom module for hex operations
    """

    def filters(self):
        return {
            "random_bytes": random_bytes
        }
