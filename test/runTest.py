#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pathlib
from unittest import TestLoader
from unittest import TextTestRunner


def main():
    testResult = TextTestRunner().run(
        TestLoader().discover(
            str(pathlib.Path(__file__).resolve().parent / 'suite')
        )
    )

    sys.exit(0 if testResult.wasSuccessful() else 1 )


if __name__ == '__main__':
    main()
