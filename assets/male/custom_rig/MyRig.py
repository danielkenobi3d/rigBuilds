from RMPY.rig import rigFK
import pymel.core as pm

root_points = pm.ls('L_tail00_reference_grp')[0]

l_my_rig = rigFK.RigFK()
l_my_rig.create_point_base(*root_points.getChildren())

root_points = pm.ls('R_tail00_reference_grp')[0]
r_my_rig = rigFK.RigFK()
r_my_rig.create_point_base(*root_points.getChildren())
r_my_rig.set_parent(l_my_rig)