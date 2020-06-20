#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from converter.batch.base.abc import BatchClass


class BatchControllerClass(object):
    """
        Batch Controller Class.
    """

    def __init__(self, batch: BatchClass):
        """
            Constructor.

            Args:
                batch : Target batch class to be executed.

            Returns:
                None.
        """

        self.__batch = batch

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

        self.__batch.pre_processing()
        self.__batch.main_processing()
        self.__batch.after_processing()
