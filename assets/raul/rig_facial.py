from RMPY.rig import rigFacial
from RMPY.rig import rigBlendShapeControls
from builder.pipeline import environment

def build():
    #initialize the environment
    env = environment.Environment()
    # getting the dictionary from the pipe config
    facial_definition = env.get_variables_from_path(environment.pipe_config.facial_definition)
    # creating the controls that are Bs on the Character
    rigBlendShapeControls.RigBlendShapeControls(root='C_facialControls_reference_pnt')
    # linking the controls to the geo based on the facial definition

    rigFacial.RigFacial(facial_definition.definition, prefix_geometry_list=facial_definition.prefix_geometry_list)


if __name__=='__main__':
    build()
