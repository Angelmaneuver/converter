#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from csv import DictReader

from converter.batch.base.abc import BatchClass
from converter.batch.translator.abc import TranslatorClass
import converter.util.f2f.excel as excel


class Excel2TextBatchClass(BatchClass):
    """
        Excel To Text Batch Class.
    """

    def __init__(self, conversions, translator: TranslatorClass = None, encoding='utf-8'):
        """
            Constructor.

            Args:
                conversions : {excel2csv: [see also converter.util.f2f.excel.to_csv.],
                               csv2translation (optional) :
                                    header: What you want to output at the top of the file after translation.
                                    footer: What you want to output at the end of the file after translation.
                                    target: [sheet: Specify the sheets specified in excel2csv that you want to
                                                    translate.,
                                             out: Destination path for translation.],
                              }

                translator (optional) : If you want to do the translation after csv conversion,
                                        you can set a translation class.

            Returns:
                None.
        """

        self.__excel2csv = conversions['excel2csv']
        self.__csv2translation = conversions['csv2translation']
        self.__translator = translator
        self.__encoding = encoding

    def pre_processing(self):
        """
            Batch pre processing.

            Args:
                None.

            Returns:+　
                None.
        """

        self.__excel2csv = excel.to_csv_test(self.__excel2csv)

    def main_processing(self):
        """
            Batch main processing.

            Args:
                None.

            Returns:
                None.
        """

        excel.to_csv(self.__excel2csv)

        if self.__translator is not None:
            header = self.__csv2translation['header'] if self.__csv2translation['header'] is not None else ''
            footer = self.__csv2translation['footer'] if self.__csv2translation['footer'] is not None else ''

            for translation in self.__csv2translation['target']:
                sheet = translation['sheet'] if translation['sheet'] is not None else None

                source = None

                for source_excel in self.__excel2csv:
                    sources = list(filter(lambda x: x['sheet'] == sheet, source_excel['csv']))
                    source = sources[0]['path'] if sources[0]['path'] is not None else None

                destination = translation['out'] if translation['out'] is not None else None

                parameter = translation['parameter'] if translation['parameter'] is not None else None

                if all(v is not None for v in [sheet, source, destination]):
                    with open(source, 'rt', encoding=self.__encoding) as fr:
                        reader = DictReader(fr)

                        if os.path.dirname(destination) == '':
                            destination = os.path.join(os.path.dirname(source), destination)

                        with open(destination, 'wt', encoding=self.__encoding) as fw:
                            fw.write(header)

                            for row in reader:
                                fw.write(self.__translator.execute(row, parameter))

                            fw.write(footer)
