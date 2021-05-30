#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import abstractmethod
from .abc import AbstractDataSourceBaseClass


class FileDataSourceBaseClass(AbstractDataSourceBaseClass):
    """
        File Data Source Base Class.
    """

    def __init__(self, io):
        """
            Constructor.

            Args:
                io: Source file path.

            Returns:
                None
        """
        self._io = io

    @abstractmethod
    def fetch(self):
        """
            Abstract method for data retrieval.

            Args:
                None

            Returns:
                None
        """

    @property
    def io(self):
        return self._io
