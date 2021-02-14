import os
from uuid import uuid4

import random
import re
import string

DEFAULT_CHAR_STRING = string.ascii_lowercase + string.digits


def generate_random_string(chars=DEFAULT_CHAR_STRING, size=6):
    return ''.join(random.choice(chars) for _ in range(size))


def get_links(string=None):
    # findall() has been used
    # with valid conditions for urls in string
    # urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] | [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+', string)
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return urls


def get_mentions(string=None):
    results = re.findall('/@[a-zA-Z0-9_]+/', string)
    return results


def get_hashtags(string=None):
    results = re.findall('/@[a-zA-Z0-9_]+/', string)
    return results


def get_symbols(string=None):
    results = re.findall('/@[a-zA-Z0-9_]+/', string)
    return results


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)

    return wrapper
