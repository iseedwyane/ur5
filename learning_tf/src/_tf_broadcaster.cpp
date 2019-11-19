#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <turtlesim/Pose.h>
#include <geometry_msgs/PoseStamped.h>
std::string turtle_name;



void poseCallback(const geometry_msgs::PoseStampedConstPtr& msg){
  static tf::TransformBroadcaster br;
  tf::Transform transform;
  transform.setOrigin( tf::Vector3(msg->pose.position.x, msg->pose.position.y, msg->pose.position.z) );
  transform.setRotation( tf::Quaternion(msg->pose.orientation.x, msg->pose.orientation.y,msg->pose.orientation.z, msg->pose.orientation.w) );
  br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "camera","aruco"));
}

int main(int argc, char** argv){
  ros::init(argc, argv, "my_tf_broadcaster");
  
  ros::NodeHandle node;
  ros::Subscriber sub = node.subscribe("/aruco_single/pose", 10, &poseCallback);

  ros::spin();
  return 0;
};