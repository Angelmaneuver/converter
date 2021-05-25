#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

import task.util.absorber as absorber
import task.util.yaml as yaml


class KamiProConverterClass():
    """
        KamiProConverter Class.
    """

    def __init__(self, rarity: str = '', additionalrarity: str = ''):
        """
            Constructor.

            Args:
                rarity:           Rarity.
                additionalRarity: Additional Rarity.

            Returns:
                None
        """
        self.__config = yaml.read(
            absorber.resource(__file__, 'config', 'kamipro.yml')
        )

        self.__headlines = ['あ', 'か', 'さ', 'た', 'な', 'は', 'ま', 'や', 'ら', 'わ']
        self.__rarity = rarity
        self.__additionalRarity = additionalrarity
        self.__formats = self.config['フォーマット']['Html']['Article']
        self.__icon_base_url = self.config['アイコン']['ベースURL']
        self.__icon_extension = '.jpg'
        self.__hp = StatusThresholdClass(
            high=self.config['閾値'][rarity]['HP']['High'],
            low=self.config['閾値'][rarity]['HP']['Low'],
            higher_format=self.config['閾値']['Html']['Higher'],
            lower_format=self.config['閾値']['Html']['Lower']
        )
        self.__attack = StatusThresholdClass(
            high=self.config['閾値'][rarity]['Attack']['High'],
            low=self.config['閾値'][rarity]['Attack']['Low'],
            higher_format=self.config['閾値']['Html']['Higher'],
            lower_format=self.config['閾値']['Html']['Lower'],
        )
        self.__html: list[str] = []

    def convert(self, row):
        """
            Data conversion method.

            Args:
                row: Conversion target data (per row).

            Returns:
                None
        """
        if row is None or type(row.神姫名) is not str:
            return

        episodes = int(row.エピソード数)
        remain_episodes = episodes

        temp = []

        if len(self.__headlines) > 0 and row.ひらがな[0] >= self.__headlines[0]:
            syllabary = ''
            last_index = 0

            for i, v in enumerate(self.__headlines):
                if row.ひらがな[0] >= v:
                    syllabary = v
                    last_index = i
                else:
                    break

            temp.append(
                self.config['フォーマット']['Html']['Index'].format(syllabary)
            )
            self.__headlines[0:last_index + 1] = []

        temp.append(self.formats['Start'].format(row.神姫名))

        for i in range(
            1,
            math.floor(episodes / 2) + math.floor(episodes % 2) + 1
        ):
            temp.extend(
                [
                    self.formats['Main']['Start'],
                    self.formats['Main']['Ribbon' + str(i)],
                    self.formats['Main']['ProfileStart'],
                    self.formats['Main']['CharacterDetailStart'],
                    (
                        self.formats['Main']['Icon1'].format(
                            self.icon_base_url +
                            self.rarity +
                            self.additionalRarity +
                            f'{row.No:03}' +
                            ('a' if i > 1 else '') +
                            self.icon_extension
                        )
                    ) if (str.strip(
                        getattr(row, 'エピソード' + str(1 if i == 1 else episodes))
                    ) != '不明') else (
                        self.formats['Main']['Icon2']
                    ),
                    self.formats['Main']['PersonalStart'],
                    self.formats['Main']['Status'].format(
                        self.config['フォーマット']['属性'][row.属性],
                        self.config['フォーマット']['タイプ'][row.タイプ],
                        self.hp.get_html(getattr(row, 'HP' + str(i))),
                        self.attack.get_html(getattr(row, 'Attack' + str(i))),
                    ),
                    self.formats['Main']['Profile'].format(
                        getattr(row, 'プロフィール' + str(i))
                    ),
                    self.formats['Main']['ProfileClose'],
                    self.formats['Main']['CharacterDetailClose'],
                    self.formats['Main']['EpisodeStart'],
                ]
            )

            for j in range(
                (math.floor(i / 2) * 2) + 1, (math.floor(i / 2) * 2) + 3
            ):
                if remain_episodes <= 0:
                    continue

                temp.append(
                    self.formats['Main']['Episode'].format(
                        getattr(row, 'エピソード' + str(j)),
                        getattr(row, 'タグ' + str(j)),
                        getattr(row, '内容' + str(j)),
                        getattr(row, 'あらすじ' + str(j)),
                    )
                )
                remain_episodes -= 1

            temp.extend(
                [
                    self.formats['Main']['EpisodeClose'],
                    self.formats['Main']['ProfileClose'],
                    self.formats['Main']['Close'],
                ]
            )

        temp.append(self.formats['Close'])

        self.__html.append(''.join(temp))

    def get_result(self) -> str:
        """
            Get conversion result method.

            Args:
                None

            Returns:
                Conversion result string.
        """
        return (
            self.config['フォーマット']['Html']['Start'] +
            ''.join(self.__html) +
            self.config['フォーマット']['Html']['Close']
        )

    @property
    def config(self):
        return self.__config

    @property
    def rarity(self):
        return self.__rarity

    @property
    def additionalRarity(self):
        return self.__additionalRarity

    @property
    def formats(self):
        return self.__formats

    @property
    def icon_base_url(self):
        return self.__icon_base_url

    @property
    def icon_extension(self):
        return self.__icon_extension

    @property
    def hp(self):
        return self.__hp

    @property
    def attack(self):
        return self.__attack


class StatusThresholdClass(object):
    """
        Status Threshold Class.
    """

    def __init__(
            self,
            high: int = 0,
            low: int = 0,
            higher_format: str = '',
            lower_format: str = '',
    ):
        """
            Constructor.

            Args:
                high:          High threshold.
                low:           Low threshold.
                higher_format: Html formatting when parameters are higher than
                               the threshold.
                lower_format : Html formatting when parameters are lower than
                               the threshold.

            Returns:
                None
        """
        self.__high = high
        self.__low = low
        self.__higher_format = higher_format
        self.__lower_format = lower_format

    def get_html(self, value, value_format: str = '{0:04.0f}'):
        """
            Compare the numeric values of the threshold and arguments and
            convert them to the corresponding format.

            Args:
                value:        numeric values.
                value_format: value conversion format (default is '{0:04.0f}')

            Returns:
                Html string.
        """
        if type(value) is str and value.isdecimal():
            value = int(value)

        elif type(value) not in [int, float]:
            return value

        str_value = value_format.format(value)
        result = str_value

        if value >= self.__high:
            result = self.__higher_format.format(str_value)

        elif value <= self.__low:
            result = self.__lower_format.format(str_value)

        return result
