# -*- coding: utf-8 -*-
"""m6plot - routines for computing map-based statistics 
"""

__all__ = [
    'calc',
    'corr',
    ]

for func in __all__:
    exec(f'from .{func} import *')
