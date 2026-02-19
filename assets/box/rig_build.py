from RMPY.rig import rigWorld
from RMPY.rig import rigFromHierarchy
import pymel.core as pm

def build_rig():
    rig_world = rigWorld.RigWorld()
    my_rig = rigFromHierarchy.RigFromHierarchy()
    my_rig.create_point_base(*pm.ls('C_COG00_reference_pnt'))
    my_rig.set_parent(rig_world)
    pm.parent('geo', 'rig')
    pm.parent('environment', 'rig')

