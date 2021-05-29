#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pathlib


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
        return pathlib.Path(sys._MEIPASS).joinpath(*paths).resolve()

    else:
        path = pathlib.Path(path)
        base = path.resolve().parent if path.is_file() else path

        return pathlib.Path(base).joinpath(*paths).resolve()
