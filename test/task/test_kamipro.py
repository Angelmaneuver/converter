#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch
import pathlib

import sys
sys.path.append(str((pathlib.Path(__file__).resolve().parent.parent.parent).resolve()))

from src.task import kamipro as testTarget
from src.task.dataSource.excel import ExcelDataSourceClass


class TestKamipro(unittest.TestCase):
    def test_converte(self):
        assumption = ''.join([
            '<section class="profiles">',
            '<h3>あ</h3>',
            '<h4>神姫3</h4><article><div><div class="ribbon"><div class="ribbon_left"></div><div class="ribbon_right"></div></div><div class="row"><div class="column"><div class="icon"><img src="/kamipro/SSRTest003.jpg" loading="lazy"></div><div class="personal row"><div class="column row-rebarse"><div class="status column"><div class="status_headline">属性</div><div><span class="wind">風</span></div><div class="status_headline">TYPE</div><div><span class="balance">Balance</span></div><div class="status_headline">HP</div><div><span class="higher">1700</span></div><div class="status_headline">ATTACK</div><div><span class="higher">8500</span></div></div><div class="sub_headline">Spec</div></div><div class="profile"><div class="headline">Profile</div><div><p>プロフィ－ル1</p></div></div></div></div><div class="column"><div class="episodes row"><div class="episode"><div class="headline">Episode</div><div><div class="headline">エピソ－ド1</div><div class="outline"><div class="column"><div class="sub_headline">タグ1</div><div class="play"><div>内容1</div></div></div><div><p>あらすじ1</p></div></div><div class="headline">エピソ－ド2</div><div class="outline"><div class="column"><div class="sub_headline">タグ2</div><div class="play"><div>内容2</div></div></div><div><p>あらすじ2</p></div></div></div></div></div></div></div></div><div><div class="ribbon" style="--background: #ff4454;"><div class="ribbon_left"></div><div class="ribbon_right" style="--context: ' + "'After Awaking'" + ';"></div></div><div class="row"><div class="column"><div class="icon"><img src="/kamipro/SSRTest003a.jpg" loading="lazy"></div><div class="personal row"><div class="column row-rebarse"><div class="status column"><div class="status_headline">属性</div><div><span class="wind">風</span></div><div class="status_headline">TYPE</div><div><span class="balance">Balance</span></div><div class="status_headline">HP</div><div>不明</div><div class="status_headline">ATTACK</div><div>不明</div></div><div class="sub_headline">Spec</div></div><div class="profile"><div class="headline">Profile</div><div><p>プロフィ－ル2</p></div></div></div></div><div class="column"><div class="episodes row"><div class="episode"><div class="headline">Episode</div><div><div class="headline">エピソ－ド3</div><div class="outline"><div class="column"><div class="sub_headline">タグ3</div><div class="play"><div>内容3</div></div></div><div><p>あらすじ3</p></div></div></div></div></div></div></div></div></article>',
            '<h3>わ</h3>',
            '<h4>神姫2</h4><article><div><div class="ribbon"><div class="ribbon_left"></div><div class="ribbon_right"></div></div><div class="row"><div class="column"><div class="icon"><img src="/kamipro/SSRTest002.jpg" loading="lazy"></div><div class="personal row"><div class="column row-rebarse"><div class="status column"><div class="status_headline">属性</div><div><span class="water">水</span></div><div class="status_headline">TYPE</div><div><span class="defense">Defense</span></div><div class="status_headline">HP</div><div>1699</div><div class="status_headline">ATTACK</div><div>8499</div></div><div class="sub_headline">Spec</div></div><div class="profile"><div class="headline">Profile</div><div><p>プロフィ－ル1</p></div></div></div></div><div class="column"><div class="episodes row"><div class="episode"><div class="headline">Episode</div><div><div class="headline">エピソ－ド1</div><div class="outline"><div class="column"><div class="sub_headline">タグ1</div><div class="play"><div>内容1</div></div></div><div><p>あらすじ1</p></div></div><div class="headline">エピソ－ド2</div><div class="outline"><div class="column"><div class="sub_headline">タグ2</div><div class="play"><div>内容2</div></div></div><div><p>あらすじ2</p></div></div></div></div></div></div></div></div><div><div class="ribbon" style="--background: #ff4454;"><div class="ribbon_left"></div><div class="ribbon_right" style="--context: ' + "'After Awaking'" + ';"></div></div><div class="row"><div class="column"><div class="icon"><img src="/kamipro/SSRTest002a.jpg" loading="lazy"></div><div class="personal row"><div class="column row-rebarse"><div class="status column"><div class="status_headline">属性</div><div><span class="water">水</span></div><div class="status_headline">TYPE</div><div><span class="defense">Defense</span></div><div class="status_headline">HP</div><div><span class="higher">2500</span></div><div class="status_headline">ATTACK</div><div>7500</div></div><div class="sub_headline">Spec</div></div><div class="profile"><div class="headline">Profile</div><div><p>プロフィ－ル2</p></div></div></div></div><div class="column"><div class="episodes row"><div class="episode"><div class="headline">Episode</div><div><div class="headline">エピソ－ド3</div><div class="outline"><div class="column"><div class="sub_headline">タグ3</div><div class="play"><div>内容3</div></div></div><div><p>あらすじ3</p></div></div></div></div></div></div></div></div></article>',
            '<h4>神姫1</h4><article><div><div class="ribbon"><div class="ribbon_left"></div><div class="ribbon_right"></div></div><div class="row"><div class="column"><div class="icon"><img src="/kamipro/SSRTest001.jpg" loading="lazy"></div><div class="personal row"><div class="column row-rebarse"><div class="status column"><div class="status_headline">属性</div><div><span class="fire">火</span></div><div class="status_headline">TYPE</div><div><span class="attack">Attack</span></div><div class="status_headline">HP</div><div><span class="lower">1499</span></div><div class="status_headline">ATTACK</div><div><span class="lower">6999</span></div></div><div class="sub_headline">Spec</div></div><div class="profile"><div class="headline">Profile</div><div><p>プロフィ－ル1</p></div></div></div></div><div class="column"><div class="episodes row"><div class="episode"><div class="headline">Episode</div><div><div class="headline">エピソ－ド1</div><div class="outline"><div class="column"><div class="sub_headline">タグ1</div><div class="play"><div>内容1</div></div></div><div><p>あらすじ1</p></div></div><div class="headline">エピソ－ド2</div><div class="outline"><div class="column"><div class="sub_headline">タグ2</div><div class="play"><div>内容2</div></div></div><div><p>あらすじ2</p></div></div></div></div></div></div></div></div><div><div class="ribbon" style="--background: #ff4454;"><div class="ribbon_left"></div><div class="ribbon_right" style="--context: ' + "'After Awaking'" + ';"></div></div><div class="row"><div class="column"><div class="icon"><img src="/kamipro/SSRTest001a.jpg" loading="lazy"></div><div class="personal row"><div class="column row-rebarse"><div class="status column"><div class="status_headline">属性</div><div><span class="fire">火</span></div><div class="status_headline">TYPE</div><div><span class="attack">Attack</span></div><div class="status_headline">HP</div><div><span class="higher">2350</span></div><div class="status_headline">ATTACK</div><div><span class="higher">8800</span></div></div><div class="sub_headline">Spec</div></div><div class="profile"><div class="headline">Profile</div><div><p>プロフィ－ル2</p></div></div></div></div><div class="column"><div class="episodes row"><div class="episode"><div class="headline">Episode</div><div><div class="headline">エピソ－ド3</div><div class="outline"><div class="column"><div class="sub_headline">タグ3</div><div class="play"><div>内容3</div></div></div><div><p>あらすじ3</p></div></div></div></div></div></div></div></div></article>',
            '</section>',
        ])

        dataSource = ExcelDataSourceClass(
            io=pathlib.Path(__file__).parent.joinpath('excel', 'test_kamipro.xlsx'),
            sheet_name='神姫リスト',
            header=None,
            names= ['No', '神姫名', 'ひらがな', '属性', 'タイプ', 'HP1', 'Attack1', 'HP2', 'Attack2', 'エピソード数', 'プロフィール1', 'プロフィール2', 'アビリティ1', '効果1', '使用間隔1', '効果時間1', 'アビリティ2', '効果2', '使用間隔2', '効果時間2', 'アビリティ3', '効果3', '使用間隔3', '効果時間3', 'アビリティ4', '効果4', '使用間隔4', '効果時間4', 'エピソード1', 'あらすじ1', '内容1', 'タグ1', 'エピソード2', 'あらすじ2', '内容2', 'タグ2', 'エピソード3', 'あらすじ3', '内容3', 'タグ3', 'HTML1', 'HTML設定先1', 'HTML2', 'HTML設定先2', '取得フラグ'],
            skiprows=4,
            sort_by=['ひらがな', 'No'],
            ascending=[True, True]
        )

        converter = testTarget.KamiProConverterClass('SSR', 'Test')

        for row in dataSource.fetch():
            converter.convert(row)

        self.assertEqual(assumption, converter.get_result())


if __name__ == '__main__':
    unittest.main()
