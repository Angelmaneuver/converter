#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch
import pathlib

import sys
sys.path.append(str((pathlib.Path(__file__).resolve().parent.parent.parent.parent.parent).resolve()))

from src.task.util import absorber as testTarget


class TestAbsorber(unittest.TestCase):
    def test_normal_path(self):
        assumptions = pathlib.Path(__file__).resolve().parent.joinpath('yml', 'test_yaml.yml')

        self.assertEqual(assumptions, testTarget.resource(__file__, 'yml', 'test_yaml.yml'))


    @patch('src.task.util.absorber.sys')
    def test_MEIPASS(self, mock):
        base = pathlib.Path(__file__).parent.parent.parent.resolve()
        assumptions = base.joinpath('yml', 'test_yaml.yml')

        setattr(mock, 'frozen', True)
        mock._MEIPASS = str(base)

        self.assertEqual(assumptions, testTarget.resource(__file__, 'yml', 'test_yaml.yml'))


if __name__ == '__main__':
    unittest.main()
