#!/usr/bin/env python
import ipdb
import sys
import rospy
import moveit_commander as mc
from birl_ur5_assembly_experiment.moveit_vars_getter import get_moveit_vars
from birl_ur5_assembly_experiment import hardcoded_data as hd

if __name__ == '__main__':
    mc.roscpp_initialize(sys.argv) 
    rospy.init_node("ur_go_home", anonymous=True)

    robot, group = get_moveit_vars()

    rospy.sleep(1)

    group.set_joint_value_target(hd.home_joint_angles)
    group.set_start_state_to_current_state()
    plan = group.plan()
    if not group.execute(plan):
        raise Exception("exec failed")

    group.clear_pose_targets()
    group.set_pose_target(hd.ram_fixed_pick_pose)
    group.set_start_state_to_current_state()
    plan = group.plan()
    if not group.execute(plan):
        raise Exception("exec failed")

    group.clear_pose_targets()
    group.set_pose_target(hd.ram_fixed_place_pose)
    group.set_start_state_to_current_state()
    plan = group.plan()
    if not group.execute(plan):
        raise Exception("exec failed")

    rospy.sleep(1)
    mc.roscpp_shutdown()
