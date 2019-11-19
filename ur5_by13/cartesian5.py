#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
from moveit_msgs.msg import RobotTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler


def talker_by13():
       
        moveit_commander.roscpp_initialize(sys.argv)      
        rospy.init_node('moveit_ik_demo')

        arm = moveit_commander.MoveGroupCommander('manipulator')                
        end_effector_link = arm.get_end_effector_link()
                        
       
        reference_frame = 'base_link'
        arm.set_pose_reference_frame(reference_frame)         
      
        arm.set_named_target('home')
        arm.go()
        rospy.sleep(2)
               
      
        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x = 0.2
        target_pose.pose.position.y = 0.25
        target_pose.pose.position.z = 0.4
        target_pose.pose.orientation.x = 0.0820
        target_pose.pose.orientation.y = -0.0269758
        target_pose.pose.orientation.z = -1.273
        target_pose.pose.orientation.w = -0.003
        
      
        arm.set_start_state_to_current_state()
        
        arm.set_pose_target(target_pose, end_effector_link)
        

      
           
      
        arm.set_named_target('home')
        arm.go()

      
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        talker_by13()
    except rospy.ROSInterruptException:
        pass
