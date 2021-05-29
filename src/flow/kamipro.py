#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib
from typing import NamedTuple, Tuple, Any
from prefect import Flow, task

import task.util.absorber as absorber
import task.util.yml as yml
from task.dataSource.excel import ExcelDataSourceClass
from task.converter.kamipro import KamiProConverterClass


class Definition(NamedTuple):
    header:    Any
    names:     Any
    skipRows:  int
    sortBy:    Any
    ascending: Any


class Condition(NamedTuple):
    path:             str
    sheet:            str
    rarity:           str
    additionalRarity: str
    output:           str


@task(name='Convert')
def convert(parameter: Tuple[Definition, Condition]) -> Tuple[str, Condition]:
    definition, condition = parameter

    converter = KamiProConverterClass(
        condition.rarity,
        condition.additionalRarity
    )

    dataSource = ExcelDataSourceClass(
        io=condition.path,
        sheet_name=condition.sheet,
        header=definition.header,
        names=definition.names,
        skiprows=definition.skipRows,
        sort_by=definition.sortBy,
        ascending=definition.ascending
    )

    for row in dataSource.fetch():
        converter.convert(row)

    return (converter.get_result(), condition)


@task(name='Output Converted Data')
def output(parameter: Tuple[str, Condition]):
    converted, condition = parameter

    with open(condition.output, 'wt', encoding='utf-8_sig') as fw:
        fw.write(converted)


def execute():
    with Flow("神姫プロジェクトエピソ－ドメモ変換") as flow:
        config = yml.read(
            absorber.resource(__file__, 'config', 'kamipro.yml')
        )
        definition = Definition(
            header=config['header'],
            names=config['names'],
            skipRows=config['skipRows'],
            sortBy=config['sortBy'],
            ascending=config['ascending']
        )

        config = yml.read(pathlib.Path().joinpath('config', 'kamipro.yml'))
        baseDestination = pathlib.Path(config['output']['destination'])
        prefix = config['output']['prefix']
        suffix = config['output']['suffix']
        extension = '.' + config['output']['extension']
        parameter: list[Tuple[Definition, Condition]] = list()
        for input in config['inputs']:
            parameter.extend(
                list(map(lambda condition: (definition, Condition(
                    path=input['path'],
                    sheet=condition['sheet'],
                    rarity=condition['rarity'],
                    additionalRarity=condition['additionalRarity'],
                    output=baseDestination.joinpath(
                        prefix + condition['convertedName'] + suffix +
                        extension
                    )

                )), input['conditions']))
            )

        converted = convert.map(parameter)
        output.map(converted)

    flow.run()
