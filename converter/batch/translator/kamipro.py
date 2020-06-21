#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import converter.util.path as path
from converter.batch.translator.abc import TranslatorClass


class Csv2KaMiProTableListTranslatorClass(TranslatorClass):
    """
        Csv to KaMiPro html table list Translator Class.
    """

    def __init__(self):
        """
            Constructor.

            Args:
                None.

            Returns:
                None.
        """

        super().__init__(path.resource(__file__, 'config', 'kamipro.yaml'))
        self.__attack = ThresholdClass()
        self.__hp = ThresholdClass

    def execute(self, data, parameter):
        """
            Data translation execute method.

            Args:
                data : Translation target data.
                parameter : Translation parameter.

            Returns:
                Translated data.
        """

        self.rarity(parameter['rarity'])

        data['属性'] = self.config['attribute_html'][data['属性']]
        data['タイプ'] = self.config['type_html'][data['タイプ']]
        data['HP1'] = self.__get_status_html(data['HP1'], self.__hp.high, self.__hp.low)
        data['Attack1'] = self.__get_status_html(data['Attack1'], self.__attack.high, self.__attack.low)

        if data['HTML設定先1'] is not None:
            if data.get(data['HTML設定先1']) is None:
                data[data['HTML設定先1']] = ''

            data[data['HTML設定先1']] += data['HTML1']

        if data['HTML設定先2'] is not None:
            if data.get(data['HTML設定先2']) is None:
                data[data['HTML設定先2']] = ''

            data[data['HTML設定先2']] += data['HTML2']

        if '3' == data['エピソ－ド数']:
            data['HP2'] = self.__get_status_html(data['HP2'], self.__hp.high, self.__hp.low)
            data['Attack2'] = self.__get_status_html(data['Attack2'], self.__attack.high, self.__attack.low)
            format_str = self.config['format_3plus'] if '備考' in data else self.config['format_3']
        elif '2' == data['エピソ－ド数']:
            format_str = self.config['format_2plus'] if '備考' in data else self.config['format_2']
        else:
            format_str = self.config['format_1plus'] if '備考' in data else self.config['format_1']

        return format_str.format(**data)

    def __get_status_html(self, value, high_threshold, low_threshold):
        """
            Status html translator method.

            Args:
                value : value.
                high_threshold : high threshold.
                low_threshold : low threshold.

            Returns:
                Translated data.
        """

        try:
            value = int(value)
            result = format(value, '04')
        except ValueError:
            return value

        if value >= high_threshold:
            result = self.config['status']['html']['higher']['start']\
                     + result\
                     + self.config['status']['html']['higher']['close']
        elif value <= low_threshold:
            result = self.config['status']['html']['lower']['start']\
                     + result\
                     + self.config['status']['html']['lower']['close']

        return result

    def rarity(self, rarity):
        """
            Rarity setting method.

            Args:
                rarity: rarity (ssr|sr|r)

            Returns:
                None.
        """

        self.attack = rarity
        self.hp = rarity

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, rarity):
        self.__attack.high = self.config['status'][rarity]['high_attack']
        self.__attack.low = self.config['status'][rarity]['low_attack']

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, rarity):
        self.__hp.high = self.config['status'][rarity]['high_hp']
        self.__hp.low = self.config['status'][rarity]['low_hp']


class ThresholdClass(object):
    """
        Threshold Class.
    """

    def __init__(self, high=0, low=0):
        """
            Constructor.

            Args:
                high : high threshold.
                low : low threshold.

            Returns:
                None.
        """

        self.__high = high
        self.__low = low

    @property
    def high(self):
        return self.__high

    @high.setter
    def high(self, high):
        self.__high = high

    @property
    def low(self):
        return self.__low

    @low.setter
    def low(self, low):
        self.__low = low
