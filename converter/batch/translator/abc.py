#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from converter.util.yaml import read


class TranslatorClass(metaclass=ABCMeta):
    """
        Abstract Translator Class.
    """

    def __init__(self, path=None, encoding='utf-8'):
        """
            Constructor.

            Args:
                path (optional) : yaml file path.
                encoding (optional) : yaml file encoding.

            Returns:
                None.
        """

        if path is not None:
            self.__config = read(path, encoding)
        else:
            self.__config = None

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, config):
        self.__config = config

    @abstractmethod
    def execute(self, data, parameter):
        """
            Data translation execute method.

            Args:
                data : Translation target data.
                parameter : Translation parameter.

            Returns:
                Translated data.
        """

        pass
