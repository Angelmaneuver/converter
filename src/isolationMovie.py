#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib
import re
from typing import List, NamedTuple, Tuple
from prefect import Flow, task
import ffmpeg

import task.util.yml as yml


class Definition(NamedTuple):
    outputs: List[Tuple[str, bool]]


class Condition(NamedTuple):
    src: pathlib.Path
    isolations: List[Tuple[pathlib.Path, bool]]


@task(name='Isolation')
def isolation(parameter: Tuple[Definition, Condition]) -> None:
    definition, condition = parameter

    for isolation in condition.isolations:
        dst, copy = isolation

        stream = ffmpeg.input(str(condition.src))

        if copy:
            stream = ffmpeg.output(stream, str(dst), c='copy')
        else:
            stream = ffmpeg.output(stream, str(dst))

        stream = ffmpeg.overwrite_output(stream)
        ffmpeg.run(stream)


with Flow("動画ファイル分離") as flow:
    config = yml.read(pathlib.Path().joinpath('config', 'isolationMovie.yml'))

    parameter1: List[Tuple[str, bool]] = list()

    for output in config['conditions']['output']:
        parameter1.append((output['format'], output['copy']))

    definition = Definition(parameter1)

    targetExtensions = """({})""".format(
        '|'.join(config['conditions']['targetExtensions'])
    )

    baseSource = pathlib.Path(config['input']['path'])
    recursive = config['input']['recursive']

    sources = [
        target for target in baseSource.glob(
            '**/*' if recursive else '*'
        ) if target.is_file()
    ]

    baseDestination = pathlib.Path(config['output']['path']).resolve()

    parameter2: List[Tuple[Definition, Condition]] = list()

    for source in sources:
        if re.search(targetExtensions, source.suffix):
            isolations: List[Tuple[pathlib.Path, bool]] = list()

            for isolationFormat in definition.outputs:
                isolationType, copy = isolationFormat

                isolations.append((
                    baseDestination.joinpath(
                                pathlib.Path(source).stem +
                                '.' +
                                isolationType
                    ),
                    copy
                ))

            parameter2.append((
                definition,
                Condition(
                    src=source,
                    isolations=isolations
                )
            ))

    isolation.map(parameter2)


if __name__ == '__main__':
    flow.run()
