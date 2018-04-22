from __future__ import unicode_literals


import string

# the standard slugify does't work very well with arabic so i made another slugify function


def slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str
