from RMPY.rig import rigSingleJoint
from RMPY.rig import rigWorld


def custom_rig():
    balle_rig = rigSingleJoint.RigSingleJoint()
    balle_rig.create_point_base('C_balle00_reference_pnt')

    pivotBarrel_rig = rigSingleJoint.RigSingleJoint()
    pivotBarrel_rig.create_point_base('C_pivotBarrel00_reference_pnt', centered=True)

    balle_rig.set_parent(pivotBarrel_rig)

    hammer_rig = rigSingleJoint.RigSingleJoint()
    hammer_rig.create_point_base('C_hammer00_reference_pnt', centered=True)

    triger_rig = rigSingleJoint.RigSingleJoint()
    triger_rig.create_point_base('C_triger00_reference_pnt', centered=True)

    gauche_rig = rigSingleJoint.RigSingleJoint()
    gauche_rig.create_point_base('C_gauche00_reference_pnt', centered=True)

    hammer_rig.set_parent(gauche_rig)
    triger_rig.set_parent(gauche_rig)
    pivotBarrel_rig.set_parent(gauche_rig)
    rig_world = rigWorld.RigWorld()
    gauche_rig.set_parent(rig_world)


