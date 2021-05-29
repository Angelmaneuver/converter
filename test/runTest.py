#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib
from unittest import TestLoader
from unittest import TextTestRunner


def main():
    loader = TestLoader()
    test = loader.discover(str(pathlib.Path(__file__).resolve().parent / 'suite'))
    runner = TextTestRunner()
    runner.run(test)

if __name__ == '__main__':
    main()
