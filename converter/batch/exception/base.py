#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BatchError(Exception):
    """
        Batch Exception Class.
    """
    def __init__(self, reason=0, message=None):
        """
            Constructor.

            Args:
                reason : reason code.
                message : error message.

            Returns:
                None.
        """

        self.__reason = reason
        self.__message = message

    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, reason):
        self.__reason = reason

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message


class PreProcessingError(BatchError):
    """
        Pre Processing Exception Class.
    """

    def __init__(self, reason=0, message=None):
        """
            Constructor.

            Args:
                reason : reason code.
                message : error message.

            Returns:
                None.
        """

        super().__init__(reason, message)
