# -*- coding: utf-8 -*-
"""m6plot.formatting - routines to customize the format of the plots
"""

__all__ = [
    'createXYcoords',
    'createXYlabels',
    'label',
    'linCI',
    'pmCI',
    'setFigureSize',
    ]

for func in __all__:
    exec(f'from .{func} import *')
