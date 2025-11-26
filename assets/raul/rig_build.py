from rigBuilds.assets.male.custom_rig import rigBiped
import pymel.core as pm
import importlib
importlib.reload(rigBiped)

def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    pm.parent('geo', 'rig')
    pm.parent('environment', 'rig')