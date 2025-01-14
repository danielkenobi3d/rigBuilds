from RMPY.rig import rigFacial
from RMPY.rig import rigBlendShapeControls
import pymel.core as pm
from RMPY.rig import rigHierarchy
from RMPY.rig import rigStaticLayer
from RMPY.rig.switches import rigFloatSwitch
from RMPY.core import rig_core
from RMPY.creators import blendShape
from builder.pipeline import environment



def build():
    create_facial_rig()
    create_jaw_layers()


def create_facial_rig():
    env = environment.Environment()
    facial_definition = env.get_variables_from_path(environment.pipe_config.default_facial_definition)

    facial_controls = rigBlendShapeControls.RigBlendShapeControls(root='C_facialControls_reference_pnt')

    rigFacial.RigFacial(facial_definition.definition,
                        prefix_geometry_list=facial_definition.prefix_geometry_list)

    pm.parentConstraint('neck_C0_head_jnt', facial_controls.rig_system.controls, mo=True)
    pm.scaleConstraint('neck_C0_head_jnt', facial_controls.rig_system.controls, mo=True)

    pm.setAttr('character.visibility', False)
    for each in facial_definition.direct_blendshape:
        static_connection(each, facial_definition.direct_blendshape[each])


def static_connection(source, destination):
    destination_bs = blendShape.BlendShape.by_node(destination)
    destination_bs.add_as_target(source)
    rig_hierarchy = rigHierarchy.RigHierarchy()
    pm.parent(source, rig_hierarchy.geometry)
    pm.setAttr('{}.visibility'.format(source), False)


def create_jaw_layers():
    env = environment.Environment()
    facial_definition = env.get_variables_from_path(environment.pipe_config.default_facial_definition)

    geometries = facial_definition.jaw_layer
    static_layer = rigStaticLayer.StaticLayer(*geometries, name='mouthOpen')
    mouth_close = rigStaticLayer.StaticLayer(*geometries, name='mouthClosed', rig_system=static_layer.rig_system)

    float_switch = rigFloatSwitch.FloatSwitch(control='C_joint00_jaw_ctr', attribute_name='lipSeal')

    for index, each_geo in enumerate(geometries):
        blend_shape = rig_core.BlendShape.by_node(each_geo)
        float_switch.attribute_output >> pm.Attribute(
            '{}.{}'.format(blend_shape.node, static_layer.static_geometries[index]))
        float_switch.attribute_output_false >> pm.Attribute(
            '{}.{}'.format(blend_shape.node, mouth_close.static_geometries[index]))


if __name__ == '__main__':
    pass
    # build()
    # rigFacial.RigFacial(facial_rig_definition.definition, prefix_geometry_list=['lowRez', 'LeyeWet', 'ReyeWet'])
    # create_facial_rig()
    # float_switch = rigFloatSwitch.FloatSwitch(control='C_joint00_jaw_ctr', attribute_name='lipSeal')
    # float_switch.attribute_output >> pm.Attribute('blendShape1.{}'.format('C_character00_mouthOpen_msh'))
    # float_switch.attribute_output_false >> pm.Attribute('blendShape1.{}'.format('C_character00_mouthClosed_msh'))
    # rigFacial.RigFacial(facial_rig_definition.eyes_dict)

