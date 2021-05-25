#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas

from .base.base import FileDataSourceBaseClass


class ExcelDataSourceClass(FileDataSourceBaseClass):
    """
        Excel File Data Source Class.
    """

    def __init__(
        self,
        io,
        sheet_name=0,
        header=0,
        names=None,
        index_col=None,
        usecols=None,
        squeeze: bool = False,
        dtype=None,
        converters=None,
        true_values=None,
        false_values=None,
        skiprows=None,
        nrows=None,
        na_values=None,
        keep_default_na: bool = True,
        na_filter: bool = True,
        verbose: bool = False,
        parse_dates: bool = False,
        date_parser=None,
        thousands=None,
        comment=None,
        skipfooter: int = 0,
        convert_float: bool = True,
        mangle_dupe_cols: bool = True,
        sort_by: list = None,
        ascending: list = None,
    ):
        """
            Constructor.

            Args:
                io        : Source file path.
                sheet_name: Source sheet name.

            Returns:
                None
        """
        super().__init__(io=io)
        self._sheet_name = sheet_name
        self._header = header
        self._names = names
        self._index_col = index_col
        self._skiprows = skiprows
        self._sort_by = sort_by
        self._ascending = ascending

    def fetch(self):
        """
            Fetch data from Excel.

            Args:
                None

            Returns:
                namedtuple (key: column header, value: column)
        """
        dataframe = pandas.read_excel(
            io=self._io,
            sheet_name=self._sheet_name,
            header=self._header,
            names=self._names,
            index_col=self._index_col,
            skiprows=self._skiprows,
        )

        dataframe.dropna(how='all', inplace=True)

        sortExecute = all(
            v is not None for v in [
                self._sort_by,
                self._ascending,
            ]
        ) and (
            len(self._sort_by) == len(self._ascending)
        )

        if sortExecute:
            dataframe.sort_values(
                by=self._sort_by,
                ascending=self._ascending,
                inplace=True
            )

        for row in dataframe.itertuples():
            yield row
