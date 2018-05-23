import os
import sys

if __name__ == '__main__':

    script, dl_python_path = sys.argv

    absolute_path = os.path.realpath(__file__)
    relative_path = '/'.join(absolute_path.split('/')[0:-3])
    #flamepy_triggers_path = '/'.join(absolute_path.split('/')[0:-2])

# ######################################################## PATHS
    print ''
    print '-' * 80
    print "This installer script:          ", script
    print "DL_PTYTHON_PATH:                ", dl_python_path
    print ''
    print "Note: DL_PTYTHON_PATH filepath is passed as an argument in the command line:"
    print "python /path/to/my/flamepy_install.py /path/to/dl_python_path_folder"
    print '-' * 80
    print ''

    target_dir = dl_python_path + "/flamepy_triggers"

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

# ######################################################## CREATE TRIGGERS

    # create __init__ file for module
    with open(dl_python_path + "/flamepy_triggers/__init__.py", "w+") as moduleinit:
        moduleinit.write('')

    # CREATE FLAME TRIGGER FILES
    # flame_trigger_apps
    with open(dl_python_path + "/flamepy_triggers/flame_trigger_apps.py", "w+") as trigger01:
        trigger01.write(
            "import os\n"
            "import sys\n"
            "\n"
            "absolute_path = os.path.realpath(__file__)\n"
            "top_parent_path = '/'.join(absolute_path.split('/')[0:-2])\n"
            "\n"
            "print '>>>>>>>>>>>>>> ABSOLUTE PATH >>>>>>>>>>>>>>>>>> :', absolute_path\n"
            "print '>>>>>>>>>>>>>> TOP PARENT PATH >>>>>>>>>>>>>>>>>> :', top_parent_path\n"
            "\n"
            "sys.path.append('{root}'.format(root=top_parent_path))\n"
            "from flamepy_sg.scripts.CUA_apps import *\n"
            "\n"
            "print '-' * 80\n"
            "print 'Flame_start.py - print sys.path'\n"
            "print (sys.path)\n"
            "print '-' * 80\n"
        )

    # flame_trigger_config
    with open(dl_python_path + "/flamepy_triggers/flame_trigger_config.py", "w+") as trigger02:
        trigger02.write(
            "import os\n"
            "import sys\n"
            "\n"
            "absolute_path = os.path.realpath(__file__)\n"
            "top_parent_path = '/'.join(absolute_path.split('/')[0:-2])\n"
            "\n"
            "print '>>>>>>>>>>>>>> ABSOLUTE PATH >>>>>>>>>>>>>>>>>> :', absolute_path\n"
            "print '>>>>>>>>>>>>>> TOP PARENT PATH >>>>>>>>>>>>>>>>>> :', top_parent_path\n"
            "\n"
            "sys.path.append('{root}'.format(root=top_parent_path))\n"
            "from flamepy_sg.scripts.CUA_config import *\n"
            "\n"
            "print '-' * 80\n"
            "print 'Flame_start.py - print sys.path'\n"
            "print (sys.path)\n"
            "print '-' * 80\n"
        )

    # flame_trigger_tools
    with open(dl_python_path + "/flamepy_triggers/flame_trigger_tools.py", "w+") as trigger03:
        trigger03.write(
            "import os\n"
            "import sys\n"
            "\n"
            "absolute_path = os.path.realpath(__file__)\n"
            "top_parent_path = '/'.join(absolute_path.split('/')[0:-2])\n"
            "\n"
            "print '>>>>>>>>>>>>>> ABSOLUTE PATH >>>>>>>>>>>>>>>>>> :', absolute_path\n"
            "print '>>>>>>>>>>>>>> TOP PARENT PATH >>>>>>>>>>>>>>>>>> :', top_parent_path\n"
            "\n"
            "sys.path.append('{root}'.format(root=top_parent_path))\n"
            "from flamepy_sg.scripts.CUA_tools import *\n"
            "\n"
            "print '-' * 80\n"
            "print 'Flame_start.py - print sys.path'\n"
            "print (sys.path)\n"
            "print '-' * 80\n"
        )

    # flame_trigger_exports
    with open(dl_python_path + "/flamepy_triggers/flame_trigger_exports.py", "w+") as trigger04:
        trigger04.write(
            "import os\n"
            "import sys\n"
            "\n"
            "absolute_path = os.path.realpath(__file__)\n"
            "top_parent_path = '/'.join(absolute_path.split('/')[0:-2])\n"
            "\n"
            "print '>>>>>>>>>>>>>> ABSOLUTE PATH >>>>>>>>>>>>>>>>>> :', absolute_path\n"
            "print '>>>>>>>>>>>>>> TOP PARENT PATH >>>>>>>>>>>>>>>>>> :', top_parent_path\n"
            "\n"
            "sys.path.append('{root}'.format(root=top_parent_path))\n"
            "from flamepy_sg.scripts.Export_hook import *\n"
            "\n"
            "print '-' * 80\n"
            "print 'Flame_start.py - print sys.path'\n"
            "print (sys.path)\n"
            "print '-' * 80\n"
        )


# end
