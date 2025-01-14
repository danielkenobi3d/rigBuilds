from RMPY.rig import rigFK

rig_finger = rigFK.RigFK()
rig_finger.create_point_base('L_pinky00_reference_pnt', 'L_pinky01_reference_pnt', 'L_pinky02_reference_pnt', 'L_pinky03_reference_pnt', 'L_pinky04_reference_pnt', orient_type='point_orient')
