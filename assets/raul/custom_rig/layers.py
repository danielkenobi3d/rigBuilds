from RMPY.rig import  rigStaticLayer
from RMPY.rig.facial import  rigFaceSquashStretch
from RMPY.rig.facial import  rigJaw
from RMPY.core import data_save_load
def facial_rig():
    head_squash_static_layers = rigStaticLayer.StaticLayer('head', 'mustacheRaul', 'eyesRaul', name='squashHead')
    head_squash_rig = rigFaceSquashStretch.RigFaceSquashStretch(rig_system = head_squash_static_layers.rig_system)
    head_squash_rig.create_point_base('C_squash00_reference_pnt', 'C_squash01_reference_pnt', 'C_squash02_reference_pnt')
    head_squash_rig.zero_joint

    jaw_static_layers = rigStaticLayer.StaticLayer('head', 'mustacheRaul', name='jaw')
    rig_jaw = rigJaw.RigJaw(rig_system = jaw_static_layers.rig_system)
    rig_jaw.create_point_base('C_jaw00_reference_pnt', 'C_jaw02_reference_pnt')

    data_save_load.load_skin_cluster(*head_squash_static_layers.static_geometries)
    data_save_load.load_skin_cluster(*jaw_static_layers.static_geometries)

if __name__=='__main__':
    facial_rig()






