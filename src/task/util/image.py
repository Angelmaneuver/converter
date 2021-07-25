#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Union
from pathlib import Path
from PIL import Image


def convertWebp(
    src: Union[str, Path],
    dst: Union[str, Path],
    lossless: bool = True,
    quality: int = 80,
) -> None:
    """
        Image convert method.

        Args:
            src (Union[str, Path]):    Source file path.
            dst (Union[str, Path]):    Conversion result output destination
                                       path.
            lossless (bool, optional): Option, @see also. Defaults to True.
            quality (int, optional):   Option, @see also. Defaults to 80.

        Returns:
            None.

        @see:
            https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#webp
    """

    with Image.open(src, 'r') as image:
        image.save(dst, 'webp', lossless=lossless, quality=quality)
