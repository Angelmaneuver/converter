#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from converter.cli.helper import CLIHelperClass
from converter.batch.translator.kamipro import Csv2KaMiProTableListTranslatorClass
from converter.batch.excel2text import Excel2TextBatchClass


def main():
    """
        Entry Point.

        Convert an Excel file to a Csv file and generate an Html file.

        Args:
            None.

        Returns:
            None.
    """

    CLIHelperClass(
        Excel2TextBatchClass(
            CLIHelperClass.read_yaml(os.path.join('config', 'kamipro.yaml')),
            Csv2KaMiProTableListTranslatorClass()
        )
    ).execute()


if __name__ == '__main__':
    main()
