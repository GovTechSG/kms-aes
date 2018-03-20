import base64
import binascii
import os

def base64_to_hex(encoded):
    """Convert base64 to hex"""
    return binascii.hexlify(base64.b64decode(encoded))

def random_bytes(length):
    """Return random bytes in hex"""
    return binascii.hexlify(os.urandom(length))

class FilterModule(object):
    """
    Custom module for hex operations
    """

    def filters(self):
        return {
            "base64_to_hex": base64_to_hex,
            "random_bytes": random_bytes
        }
