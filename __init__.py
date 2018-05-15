#from modules import *
import os
import sys

absolute_path = os.path.realpath(__file__)
root_path = '/'.join(absolute_path.split('/')[0:-1])

print '-' * 80
print "FROM TOP __init__: "
print "absolute_path for top __init__.py: ", absolute_path
print "root_path: ", root_path

print '-' * 80

sys.path.append("{root}/modules".format(root=root_path))
# sys.path.append("{root}/modules/clique".format(root=root_path))
# sys.path.append("{root}/modules/yaml".format(root=root_path))
