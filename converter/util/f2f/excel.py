#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas


def to_csv(conversions: list):
    """
        Excel to Csv batch convert method.

        Args:
            conversions : Convert list.
                          [{excel: excel file path,
                            csv: [{sheet: convert target sheet name,
                                     path (optional) : converted file path,
                                     option (optional) : { not use now, reservation dictionary }}, ...]
                           },
                          ...]
                          If you don't specify the path, use the excel file path and sheet name as the csv path.

        Returns:
            None.

        Raise:
            to_csv_test method's raise exception
    """

    checked_conversions = to_csv_test(conversions)

    for index, conversion in enumerate(checked_conversions):
        for csv in conversion['csv']:
            df = pandas.read_excel(conversion['excel'], sheet_name=csv['sheet'])
            df.to_csv(csv['path'], index=False)


def to_csv_test(conversions: list):
    """
        to_csv method's parameter check.

        The to_csv method uses this method internally.
        Therefore, there is no need to pass the return value of this method when calling the to_csv method.

        Args:
            conversions : same as to_csv method.

        Returns:
            checked conversions : after checking.

        Raise:
            FileNotFoundError
    """

    for i, conversion in enumerate(conversions):
        if 'excel' not in conversion:
            conversions.pop(i)
            continue
        else:
            excel = conversion['excel']
            directory = os.path.dirname(excel)

        if not os.path.isfile(excel):
            raise FileNotFoundError

        if 'csv' not in conversion:
            conversions.pop(i)
            continue

        for j, csv in enumerate(conversion['csv']):
            if 'sheet' not in csv or csv['sheet'] is None:
                conversions[i]['csv'].pop(j)
                continue
            else:
                sheet = csv['sheet']

            if 'path' not in csv or csv['path'] is None:
                csv['path'] = os.path.join(directory, sheet + '.csv')
                conversions[i]['csv'][j] = csv
            elif os.path.isdir(csv['path']):
                csv['path'] = os.path.join(csv['path'], sheet + '.csv')
                conversions[i]['csv'][j] = csv
            elif os.path.dirname(csv['path']) is None:
                csv['path'] = os.path.join(directory, csv['path'])
                conversions[i]['csv'][j] = csv

        if len(conversion['csv']) == 0:
            conversions.pop(i)
            continue

    return conversions
