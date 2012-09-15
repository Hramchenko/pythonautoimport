# Your import instructions

#      ...

import ExampleModule
import ModulesLoader


# Warning! Call ModulesLoader.load_modules_dict only when
# all your own modules are imported! 

modules = dict(os='os', string='string')
ModulesLoader.load_modules_dict(modules)

# For scientific calculations you also could use 
# ModulesLoader.load_scientific_modules() for importing
# popular modules
ModulesLoader.load_scientific_modules()

ExampleModule.my_func()
