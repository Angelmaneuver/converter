#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib
import re
from typing import List, NamedTuple, Tuple
from prefect import Flow, task

import task.util.yml as yml
import task.util.image as image


class Definition(NamedTuple):
    loseless: bool
    quality:  int


class Condition(NamedTuple):
    src: pathlib.Path
    dst: pathlib.Path
    delete: bool


@task(name='Convert')
def convert(parameter: Tuple[Definition, Condition]) -> None:
    definition, condition = parameter

    image.convertWebp(
        src=condition.src,
        dst=condition.dst,
        lossless=definition.loseless,
        quality=definition.quality
    )

    if condition.delete:
        condition.src.unlink()


with Flow("画像ファイル変換 - Webp") as flow:
    config = yml.read(pathlib.Path().joinpath('config', 'convertWebp.yml'))

    definition = Definition(
        loseless=config['conditions']['loseless'],
        quality=config['conditions']['quality'],
    )

    targetExtensions = """({})""".format(
        '|'.join(config['conditions']['targetExtensions'])
    )

    baseSource = pathlib.Path(config['input']['path'])
    recursive = config['input']['recursive']
    replace = config['input']['replace']
    delete = True if config['input']['delete'] or replace else False
    extension = config['output']['extension']
    sources = [
        target for target in baseSource.glob(
            '**/*' if recursive else '*'
        ) if target.is_file()
    ]

    baseDestination = pathlib.Path(config['output']['path'])

    parameter: List[Tuple[Definition, Condition]] = list()

    for source in sources:
        if re.search(targetExtensions, source.suffix):
            parameter.append((
                definition,
                Condition(
                    src=source,
                    dst=(
                        source.with_suffix('.' + extension)
                        if replace else
                        baseDestination.joinpath(
                            pathlib.Path(source).stem +
                            '.' +
                            config['output']['extension']
                        )
                    ),
                    delete=delete
                )
            ))

    convert.map(parameter)


if __name__ == '__main__':
    flow.run()
