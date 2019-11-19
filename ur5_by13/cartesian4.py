import rospy, sys
import moveit_commander
from moveit_commander import MoveGroupCommander
from copy import deepcopy

def talker_by13():
    	#init
    	moveit_commander.roscpp_initialize(sys.argv)
    	rospy.init_node('moveit_fk_demo')
        cartesian = rospy.get_param('~cartesian', True)
        arm = MoveGroupCommander('manipulator')

        #arm.set_pose_reference_frame('base_link')

        #arm.set_goal_position_tolerance(0.001)
       # arm.set_goal_orientation_tolerance(0.001)
       # arm.set_max_acceleration_scaling_factor(0.5)
        #arm.set_max_velocity_scaling_factor(0.5)

        end_effector_link = arm.get_end_effector_link()

        arm.set_named_target('home')
        arm.go()
        rospy.sleep(1)

        start_pose = arm.get_current_pose(end_effector_link).pose

        waypoints = []

        wpose = deepcopy(start_pose)
        wpose.position.x -= 0.2
        wpose.position.y -= 0.2
	#wpose.position.z += 0.6 
        #wpose.position.x = 0.8
        #wpose.position.y = 0.9
	#wpose.position.z = 0.9

        arm.set_pose_target(wpose)  
        arm.go()
        rospy.sleep(1)

        




   	moveit_commander.roscpp_shutdown()
    	moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        talker_by13()
    except rospy.ROSInterruptException:
        pass
