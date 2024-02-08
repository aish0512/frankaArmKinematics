## *********************************************************
##
## File autogenerated for the franka_example_controllers package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [], 'groups': [{'name': 'Controller_Gains', 'type': 'apply', 'state': True, 'cstate': 'true', 'id': 1, 'parent': 0, 'parameters': [{'name': 'leader_damping_scaling', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'Factor to be multiplied with initial leader d_gains', 'min': 0.0, 'max': 8.0, 'srcline': 9, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'follower_stiffness_scaling', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'Factor to be multiplied with initial p-gains of follower arm, damping will also be adapted', 'min': 0.1, 'max': 1.3, 'srcline': 12, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::CONTROLLER_GAINS', 'parentclass': 'DEFAULT', 'parentname': 'Default', 'field': 'DEFAULT::controller_gains', 'upper': 'CONTROLLER_GAINS', 'lower': 'controller_gains'}, {'name': 'Force_Feedback', 'type': '', 'state': True, 'cstate': 'true', 'id': 2, 'parent': 0, 'parameters': [{'name': 'force_feedback_idle', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'Applied feedback force when leader arm is idle', 'min': 0.0, 'max': 1.0, 'srcline': 18, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'force_feedback_guiding', 'type': 'double', 'default': 0.98, 'level': 0, 'description': 'Applied feedback force when leader arm is guided', 'min': 0.0, 'max': 1.0, 'srcline': 21, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::FORCE_FEEDBACK', 'parentclass': 'DEFAULT', 'parentname': 'Default', 'field': 'DEFAULT::force_feedback', 'upper': 'FORCE_FEEDBACK', 'lower': 'force_feedback'}, {'name': 'Cartesian_Contact', 'type': '', 'state': True, 'cstate': 'true', 'id': 3, 'parent': 0, 'parameters': [{'name': 'leader_contact_force_threshold', 'type': 'double', 'default': 4.0, 'level': 0, 'description': 'Force threshold at leader endeffector to determine whether the arm is in contact.', 'min': 0.1, 'max': 10.0, 'srcline': 26, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'follower_contact_force_threshold', 'type': 'double', 'default': 5.0, 'level': 0, 'description': 'Force threshold at follower endeffector to determine whether the arm is in contact.', 'min': 0.1, 'max': 10.0, 'srcline': 30, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::CARTESIAN_CONTACT', 'parentclass': 'DEFAULT', 'parentname': 'Default', 'field': 'DEFAULT::cartesian_contact', 'upper': 'CARTESIAN_CONTACT', 'lower': 'cartesian_contact'}, {'name': 'Max_Velocities', 'type': '', 'state': True, 'cstate': 'true', 'id': 4, 'parent': 0, 'parameters': [], 'groups': [{'name': 'Dq_MaxLower', 'type': 'tab', 'state': True, 'cstate': 'true', 'id': 5, 'parent': 4, 'parameters': [], 'groups': [{'name': 'dq_max_lower', 'type': 'apply', 'state': True, 'cstate': 'true', 'id': 6, 'parent': 5, 'parameters': [{'name': 'dq_l_1', 'type': 'double', 'default': 0.8, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.17, 'srcline': 39, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_l_2', 'type': 'double', 'default': 0.8, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.17, 'srcline': 40, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_l_3', 'type': 'double', 'default': 0.8, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.17, 'srcline': 41, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_l_4', 'type': 'double', 'default': 0.8, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.17, 'srcline': 42, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_l_5', 'type': 'double', 'default': 2.5, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.6, 'srcline': 43, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_l_6', 'type': 'double', 'default': 2.5, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.6, 'srcline': 44, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_l_7', 'type': 'double', 'default': 2.5, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.6, 'srcline': 45, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::MAX_VELOCITIES::DQ_MAXLOWER::DQ_MAX_LOWER', 'parentclass': 'DEFAULT::MAX_VELOCITIES::DQ_MAXLOWER', 'parentname': 'Dq_MaxLower', 'field': 'DEFAULT::MAX_VELOCITIES::DQ_MAXLOWER::dq_max_lower', 'upper': 'DQ_MAX_LOWER', 'lower': 'dq_max_lower'}], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::MAX_VELOCITIES::DQ_MAXLOWER', 'parentclass': 'DEFAULT::MAX_VELOCITIES', 'parentname': 'Max_Velocities', 'field': 'DEFAULT::MAX_VELOCITIES::dq_maxlower', 'upper': 'DQ_MAXLOWER', 'lower': 'dq_maxlower'}, {'name': 'Dq_MaxUpper', 'type': 'tab', 'state': True, 'cstate': 'true', 'id': 7, 'parent': 4, 'parameters': [], 'groups': [{'name': 'dq_max_upper', 'type': 'apply', 'state': True, 'cstate': 'true', 'id': 8, 'parent': 7, 'parameters': [{'name': 'dq_u_1', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.17, 'srcline': 49, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_u_2', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.17, 'srcline': 50, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_u_3', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.17, 'srcline': 51, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_u_4', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.17, 'srcline': 52, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_u_5', 'type': 'double', 'default': 2.5, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.6, 'srcline': 53, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_u_6', 'type': 'double', 'default': 2.5, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.6, 'srcline': 54, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'dq_u_7', 'type': 'double', 'default': 2.5, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 2.6, 'srcline': 55, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::MAX_VELOCITIES::DQ_MAXUPPER::DQ_MAX_UPPER', 'parentclass': 'DEFAULT::MAX_VELOCITIES::DQ_MAXUPPER', 'parentname': 'Dq_MaxUpper', 'field': 'DEFAULT::MAX_VELOCITIES::DQ_MAXUPPER::dq_max_upper', 'upper': 'DQ_MAX_UPPER', 'lower': 'dq_max_upper'}], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::MAX_VELOCITIES::DQ_MAXUPPER', 'parentclass': 'DEFAULT::MAX_VELOCITIES', 'parentname': 'Max_Velocities', 'field': 'DEFAULT::MAX_VELOCITIES::dq_maxupper', 'upper': 'DQ_MAXUPPER', 'lower': 'dq_maxupper'}], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::MAX_VELOCITIES', 'parentclass': 'DEFAULT', 'parentname': 'Default', 'field': 'DEFAULT::max_velocities', 'upper': 'MAX_VELOCITIES', 'lower': 'max_velocities'}, {'name': 'Max_Acceleration', 'type': '', 'state': True, 'cstate': 'true', 'id': 9, 'parent': 0, 'parameters': [], 'groups': [{'name': 'Ddq_MaxLower', 'type': 'tab', 'state': True, 'cstate': 'true', 'id': 10, 'parent': 9, 'parameters': [], 'groups': [{'name': 'ddq_max_lower', 'type': 'apply', 'state': True, 'cstate': 'true', 'id': 11, 'parent': 10, 'parameters': [{'name': 'ddq_l_1', 'type': 'double', 'default': 0.8, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 15.0, 'srcline': 60, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_l_2', 'type': 'double', 'default': 0.8, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 7.5, 'srcline': 61, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_l_3', 'type': 'double', 'default': 0.8, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 10.0, 'srcline': 62, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_l_4', 'type': 'double', 'default': 0.8, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 12.5, 'srcline': 63, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_l_5', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 15.0, 'srcline': 64, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_l_6', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 20.0, 'srcline': 65, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_l_7', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 20.0, 'srcline': 66, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXLOWER::DDQ_MAX_LOWER', 'parentclass': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXLOWER', 'parentname': 'Ddq_MaxLower', 'field': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXLOWER::ddq_max_lower', 'upper': 'DDQ_MAX_LOWER', 'lower': 'ddq_max_lower'}], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXLOWER', 'parentclass': 'DEFAULT::MAX_ACCELERATION', 'parentname': 'Max_Acceleration', 'field': 'DEFAULT::MAX_ACCELERATION::ddq_maxlower', 'upper': 'DDQ_MAXLOWER', 'lower': 'ddq_maxlower'}, {'name': 'Ddq_MaxUpper', 'type': 'tab', 'state': True, 'cstate': 'true', 'id': 12, 'parent': 9, 'parameters': [], 'groups': [{'name': 'ddq_max_upper', 'type': 'apply', 'state': True, 'cstate': 'true', 'id': 13, 'parent': 12, 'parameters': [{'name': 'ddq_u_1', 'type': 'double', 'default': 6.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 15.0, 'srcline': 70, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_u_2', 'type': 'double', 'default': 6.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 7.5, 'srcline': 71, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_u_3', 'type': 'double', 'default': 6.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 10.0, 'srcline': 72, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_u_4', 'type': 'double', 'default': 6.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 12.5, 'srcline': 73, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_u_5', 'type': 'double', 'default': 15.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 15.0, 'srcline': 74, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_u_6', 'type': 'double', 'default': 20.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 20.0, 'srcline': 75, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ddq_u_7', 'type': 'double', 'default': 20.0, 'level': 0, 'description': 'Description', 'min': 0.1, 'max': 20.0, 'srcline': 76, 'srcfile': '/home/aishwarya/Desktop/ROS_panda_arm/src/franka_example_controllers/cfg/teleop_param.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXUPPER::DDQ_MAX_UPPER', 'parentclass': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXUPPER', 'parentname': 'Ddq_MaxUpper', 'field': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXUPPER::ddq_max_upper', 'upper': 'DDQ_MAX_UPPER', 'lower': 'ddq_max_upper'}], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXUPPER', 'parentclass': 'DEFAULT::MAX_ACCELERATION', 'parentname': 'Max_Acceleration', 'field': 'DEFAULT::MAX_ACCELERATION::ddq_maxupper', 'upper': 'DDQ_MAXUPPER', 'lower': 'ddq_maxupper'}], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::MAX_ACCELERATION', 'parentclass': 'DEFAULT', 'parentname': 'Default', 'field': 'DEFAULT::max_acceleration', 'upper': 'MAX_ACCELERATION', 'lower': 'max_acceleration'}], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

