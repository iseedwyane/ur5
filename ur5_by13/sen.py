import rospy, sys
import moveit_commander
from moveit_commander import MoveGroupCommander
from copy import deepcopy
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler
def talker_by13():
    	#init
    	moveit_commander.roscpp_initialize(sys.argv)
    	rospy.init_node('moveit_fk_demo')
        #cartesian = rospy.get_param('~cartesian', True)
        arm = MoveGroupCommander('manipulator')

        arm.set_pose_reference_frame('base_link')

	arm.allow_replanning(True)
        arm.set_goal_position_tolerance(0.001)
        arm.set_goal_orientation_tolerance(0.001)
       # arm.set_max_acceleration_scaling_factor(0.5)
        #arm.set_max_velocity_scaling_factor(0.5)

        end_effector_link = arm.get_end_effector_link()

        #arm.set_named_target('home')
 	arm.set_named_target('up')
        arm.go()
        rospy.sleep(2)

        target_pose = PoseStamped()
        target_pose.header.frame_id = 'base_link'
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x = 0.86
        target_pose.pose.position.y = 0.25
        target_pose.pose.position.z = 0.02832
        target_pose.pose.orientation.x = 0
        target_pose.pose.orientation.y = 0
        target_pose.pose.orientation.z = 0
        target_pose.pose.orientation.w = 1
        #next: find workspace

	arm.set_start_state_to_current_state()  
        arm.set_pose_target(target_pose, end_effector_link)

	traj = arm.plan()

	arm.execute(traj)


	#arm.shift_pose_target(2,-0.05,end_effector_link)
  	#arm.go()
	rospy.sleep(2)


   	moveit_commander.roscpp_shutdown()
    	moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        talker_by13()
    except rospy.ROSInterruptException:
        pass
