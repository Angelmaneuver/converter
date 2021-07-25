#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import pathlib

import sys
sys.path.append(str((pathlib.Path(__file__).resolve().parent.parent.parent.parent).resolve()))

from src.task.util import image as testTarget


class TestConvertWebp(unittest.TestCase):
    def test_convert(self):
        src = pathlib.Path(__file__).parent.joinpath('image', 'convert_target.png')
        dst = pathlib.Path(__file__).parent.joinpath('image', 'convert_target.webp')

        if dst.exists():
            dst.unlink()

        testTarget.convertWebp(src=src, dst=dst, lossless=False, quality=70)

        self.assertEqual(True, dst.exists())


if __name__ == '__main__':
    unittest.main()
