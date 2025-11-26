import dwpicker
import maya.cmds as cmds

if cmds.getAttr('L_root00_arm_ctr.IkFkSwitch'):
    cmds.setAttr('L_root00_arm_ctr.IkFkSwitch', 0)
    dwpicker.set_layer_visible("L_arm_ik", False)
    dwpicker.set_layer_visible("L_arm_FK", True)
else:
    cmds.setAttr('L_root00_arm_ctr.IkFkSwitch', 10)
    dwpicker.set_layer_visible("L_arm_ik", True)
    dwpicker.set_layer_visible("L_arm_FK", False)