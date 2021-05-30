#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import pathlib

import sys
sys.path.append(str((pathlib.Path(__file__).resolve().parent.parent.parent.parent).resolve()))

from src.task.util import yml as testTarget


class TestYaml(unittest.TestCase):
    def test_read(self):
        assumptions = {
            'inputs': [
                {
                    'path':       'path1',
                    'conditions': [
                        {
                            'sheet':            'sheet1',
                            'rarity':           'rarity1',
                            'additionalRarity': 'additionalRarity1',
                            'convertedName':    'convertedName1'
                        },
                        {
                            'sheet':            'sheet2',
                            'rarity':           'rarity2',
                            'additionalRarity': 'additionalRarity2',
                            'convertedName':    'convertedName2'
                        },
                    ]
                },
            ],
            'output': {
                'destination': 'destination1',
                'prefix':      'prefix1',
                'suffix':      'suffix1',
                'extension':   'extension1'
            }
        }

        data = testTarget.read(
            pathlib.Path(__file__).parent.joinpath('yml', 'test_yaml.yml')
        )

        self.assertEqual(assumptions, data)


if __name__ == '__main__':
    unittest.main()
