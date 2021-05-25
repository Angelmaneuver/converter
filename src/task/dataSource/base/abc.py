#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class AbstractDataSourceBaseClass(metaclass=ABCMeta):
    """
        Abstract Data Source Base Class.
    """

    @abstractmethod
    def fetch(self):
        """
            Abstract method for data retrieval.

            Args:
                None

            Returns:
                None
        """
        pass
