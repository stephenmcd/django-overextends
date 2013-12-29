#!/usr/bin/env python

import sys
import os

from django.core.management import execute_from_command_line


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    execute_from_command_line(sys.argv)
