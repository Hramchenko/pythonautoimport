# Copyright (C) 2012, by Hramchenko Vitaliy <hramchenko@bk.ru> under LGPLv3 license

import os
import sys

def append_modules(module, modules_dict):
    for k, v in modules_dict.items():
        imported_module = None
        if hasattr(module, k):
            continue
        try:
            import_command = 'import ' + v + ' as imported_module'
            exec(import_command)
            setattr(module, k, imported_module)
        except ImportError:
            None
        except AttributeError:
            None

def load_modules_dict(modules_dict):
    if sys.gettrace() == None:
        return
    for m in sys.modules.values():
        append_modules(m, modules_dict)

def load_scientific_modules():
    modules = dict(sp='scipy',
                   np='numpy',
                   mpl='matplotlib',
                   plt='matplotlib.pyplot',
                   sys='sys',
                   os='os',
                   cv2='cv2',
                   cv='cv2.cv',
                   pylab='pylab')
    load_modules_dict(modules)

