#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from converter.batch.controller.base import BatchControllerClass
from converter.batch.base.abc import BatchClass
from converter.util.yaml import read


class CLIHelperClass(object):
    """
        Command Line Interface Helper Class.
    """

    def __init__(self, batch: BatchClass):
        """
            Constructor.

            Args:
                batch : Target batch class to be executed.

            Returns:
                None.
        """

        self.__controller = BatchControllerClass(batch)

    def execute(self):
        """
            Batch Execute.

            Args:
                None.

            Returns:
                None.

            Raise:
                None.

        """

        self.__controller.execute()

    @classmethod
    def read_yaml(cls, path: str, encoding='utf-8'):
        """
            Constructor.

            Args:
                path : yaml file path.
                encoding (optional) : yaml file encoding.

            Returns:
                yaml data
        """

        return read(path, encoding)
