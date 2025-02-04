prefix_geometry_list = ['eyebrows']

definition = {
        'eyes': dict(
            type='blend_shape_definition',
            isSymetrical=True,
            baseMesh='eyes',
            control='L_facial00_eye_ctr',
            blendShapes=dict(LeyeCls={'connection': 'eyeClosed', 'value': 1}),
            attributes=dict(eyeClosed={'type': 'float', 'min': 0, 'max': 1}),
            order=['eyeClosed']
        ),
        'brows':dict(
            type='blend_shape_definition',
            isSymetrical=True,
            baseMesh='character',
            control='L_main00_brow_ctr',
            blendShapes=dict(
                LoutBrowsUp={'connection': 'translateX', 'value': 10},
                LoutBrowsDwn ={'connection': 'translateX', 'value': -10},
                LinBrowsUp ={'connection': 'translateY', 'value': 10},
                LinBrowsDwn ={'connection': 'translateY', 'value': -10}
                ),
            attributes=dict(translateX={'type': 'float', 'min':-10, 'max': 10},
                            translateY={'type': 'float', 'min':-10, 'max': 10}
                            ),
            order=['translateX', 'translateY']
        )
    }