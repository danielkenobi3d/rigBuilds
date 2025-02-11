from builder.pipeline import environment
from RMPY.rig.switches import rigBoolSwitch
from RMPY.rig.switches import rigEnumSwitch
import pymel.core as pm

def build():
    visibility_control = 'C_settings00_world_ctr'
    visibility_attribute = 'visibility'
    env = environment.Environment()
    geometry_definition = env.get_variables_from_path(environment.pipe_config.geo_definition)
    if 'visibility' in vars(geometry_definition):
        for each_switch in geometry_definition.visibility:
            if type(geometry_definition.visibility[each_switch]) is list:
                bool_switch = rigBoolSwitch.RigBoolSwitch(control=visibility_control,
                                            attribute_name=each_switch)
                for each_geo in geometry_definition.visibility[each_switch]:
                    pm.connectAttr(bool_switch.attribute_output, f'{each_geo}.{visibility_attribute}')

            elif type(geometry_definition.visibility[each_switch]) is dict:
                enum_switch = rigEnumSwitch.RigEnumSwitch(control=visibility_control)
                enum_switch.add_enum_names(geometry_definition.visibility[each_switch].keys(), attribute_name=each_switch)
                for each_key in geometry_definition.visibility[each_switch]:
                    for each_geo in geometry_definition.visibility[each_switch][each_key]:
                        pm.connectAttr(enum_switch.switch[each_key].attribute_output, f'{each_geo}.{visibility_attribute}')
            else:
                print (f'visibility switch not supported {geometry_definition.visibility[each_switch]}')