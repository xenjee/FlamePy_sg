import os

from lib.customprints.ansi_colors import sg_colors
# from modules import yaml
# import yaml
import subprocess as sb

# PySide stuff, included with Flame default install. Quick and lazy import *
from PySide.QtCore import *
from PySide.QtGui import *
from scripts.batch_selections.batch_selections_UI import SelectionsWidget

# Snippets
import scripts.batch_snippets.mvr_back_to_beauty as _backtobeauty
from scripts.batch_snippets import test_print2 as _testprint

from scripts.batch_snippets.input_dialog import InputDialogBox
#from scripts.batch_snippets.mvr_back_to_beauty_Layout import DialogShot

print sg_colors.grey3 + '-' * 80 + sg_colors.endc
print sg_colors.blue2 + "--- From CUA_tools ---" + sg_colors.endc


absolute_path = os.path.realpath(__file__)
root_path = '/'.join(absolute_path.split('/')[0:-2])

# adds entries to Flame contextual menu.


def getCustomUIActions():

    toolsAction1 = {}
    toolsAction1["name"] = "selections"
    toolsAction1["caption"] = "Selections"

    toolsAction2 = {}
    toolsAction2["name"] = "backtobeauty"
    toolsAction2["caption"] = "Backtobeauty"

    toolsAction3 = {}
    toolsAction3["name"] = "expressions_tips"
    toolsAction3["caption"] = "Expressions_tips"

    toolsGroup = {}
    toolsGroup["name"] = "Tools"
    toolsGroup["actions"] = (toolsAction1, toolsAction2, toolsAction3,)

    return (toolsGroup,)


# Defines a behavior for each action.
# in this case, Start appses a QT (PySide) app base on a main 'Qdialog' (TabDialog), with 3 types of operations split in 3 tabs.
# Each tab is a class: PathsTab, StaffTab, ExportPresetsTab.
# Each class contains a 'save' button to create or update a yaml config file that will later be used in the 'custom export hook' script.
def customUIAction(info, userData):

    if info['name'] == 'selections':
        import flame

        def get_selection():
            import flame

            print sg_colors.green1 + "--- def get_selection() inside CustomUiaction_selections.py ---" + sg_colors.endc
            print sg_colors.red2 + "--- remember: 2018.3 doesn't need '.get_value()', 2019 does ---" + sg_colors.endc
            return ["" + s.name + "" for s in flame.batch.selected_nodes.get_value()]

        yamlpath = "{root}/scripts/batch_selections/saved_nodes.yaml".format(root=root_path)

        # ############
        app = QApplication.activePopupWidget()
        # we call 'save_Load_selections_UI_04c.py' giving it 2 args:
        # -> the path to the yaml file and the selected nodes list
        form = SelectionsWidget(path=yamlpath, graphSelected=get_selection)
        form.show()
        app.exec_()

    if info['name'] == 'backtobeauty':

        def user_input_builds_btb():
            dialog = InputDialogBox()
            # dialog = DialogShot()
            dialog.show()
            if dialog.exec_():
                shot_text = str(dialog.shotName.text())
                print sg_colors.yellow1 + "shot_text: " + shot_text + sg_colors.endc
                elt_text = str(dialog.elementName.text())
                print sg_colors.yellow1 + "elt_text: " + elt_text + sg_colors.endc

                _backtobeauty.main(shot_text, elt_text)

        user_input_builds_btb()

    if info['name'] == 'expressions_tips':
        file_path = "{root}/lib/text_files/Expressions_particles_reformated.txt".format(root=root_path)

        print sg_colors.grey3 + file_path + sg_colors.endc
        sb.call(["open", file_path])


print sg_colors.orange1 + "--- End of CUA_tools ---" + sg_colors.endc
print sg_colors.grey3 + '-' * 80 + sg_colors.endc
