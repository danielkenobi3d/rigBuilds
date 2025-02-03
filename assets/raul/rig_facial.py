from RMPY.rig import rigFacial
from RMPY.rig import rigBlendShapeControls

def build():
    facial_rig = {
        'eyes': dict(
            type='blend_shape_definition',
            isSymetrical=True,
            baseMesh='character',
            control='L_facial00_eye_ctr',
            blendShapes=dict(LeyeCls={'connection': 'eyeClosed', 'value': 1}),
            attributes=dict(eyeClosed={'type': 'float', 'min': 0, 'max': 1}),
            order=['eyeClosed']
        )
    }
    rigBlendShapeControls.RigBlendShapeControls(root='C_facialControls_reference_pnt')

    rigFacial.RigFacial(facial_rig)

build()
