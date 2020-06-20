#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta


class BatchClass(metaclass=ABCMeta):
    """
        Abstract Base Batch Class.
    """

    def pre_processing(self):
        """
            Batch pre processing.

            Args:
                None.

            Returns:
                None.
        """
        pass

    def main_processing(self):
        """
            Batch main processing.

            Args:
                None.

            Returns:
                None.
        """
        pass

    def after_processing(self):
        """
            Batch after processing.

            Args:
                None.

            Returns:
                None.
        """
        pass
