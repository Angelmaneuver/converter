#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os


def resource(path, *paths):
    """
        Absorb differences in file paths between the Python and Windows
        executables.

        Args:
            path:   The relative path of the calling file.
            *paths: joined paths.

        Returns:
            path string.
    """

    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, *paths)

    else:
        return os.path.join(os.path.abspath(os.path.dirname(path)), *paths)
