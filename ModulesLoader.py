# Copyright (C) 2012, by Hramchenko Vitaliy <hramchenko@bk.ru> under LGPLv3 license

import os, sys


current_dir = os.getcwd()
current_dir = os.path.abspath(current_dir)

def module_path(module):
    if hasattr(module, '__file__') == False:
        return None
    f = module.__file__
    f = os.path.abspath(f)
    return f
    
def is_module_local(module):
    path = module_path(module)
    if path != None:
        if path.startswith(current_dir):
            return True
    return False    

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

def process_local_modules(func, args=None):
    for m in sys.modules.values():
        if is_module_local(m):
            func(m, args)

def load_modules_dict(modules_dict):
    if sys.gettrace() == None:
        return
    process_local_modules(append_modules, modules_dict)

def load_scientific_modules():
    modules = dict(sp='scipy',
                   np='numpy',
                   mpl='matplotlib',
                   plt='matplotlib.pyplot',
                   sys='sys',
                   os='os',
                   cv='cv')
    load_modules_dict(modules)

