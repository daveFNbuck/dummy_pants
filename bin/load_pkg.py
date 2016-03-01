import pkgutil

import mod

modules = [module_name for _, module_name, _ in pkgutil.walk_packages(mod.__path__, 'mod.')]
print 'modules:', ''.join('\n  - %s' % module for module in modules)
