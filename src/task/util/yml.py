#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Union
from pathlib import Path

import yaml


def read(path: Union[str, Path], encoding='utf-8'):
    """
        Yaml read method.

        Args:
            path:                yaml file path.
            encoding (optional): yaml file encoding.

        Returns:
            yaml data
    """

    with open(path, 'r', encoding=encoding) as file:
        data = yaml.safe_load(file.read())

    return data
