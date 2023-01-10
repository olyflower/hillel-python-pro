"""Create a function that converts a given ASCII string to its hexadecimal SHA-256 hash.

sha256("Hello World!") => "7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"""
import hashlib


def to_sha256(lst):
    return hashlib.sha256(lst.encode('utf-8')).hexdigest()


print(to_sha256("Hello World!"))
