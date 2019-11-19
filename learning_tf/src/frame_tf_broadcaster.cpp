#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "my_tf_broadcaster");
  ros::NodeHandle node;

  tf::TransformBroadcaster br;
  tf::Transform transform;

  ros::Rate rate(10.0);
  while (node.ok()){
    transform.setOrigin( tf::Vector3(0.08129, 0.03178, 0) );
    transform.setRotation( tf::Quaternion(-0.68407, -0.22465, -0.662427, 0.2068019) );
    br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "tool0", "camera"));
    rate.sleep();
  }
  return 0;
};



//    transform.setOrigin( tf::Vector3(0.08164828, 0.06720414, -0.04457389) );
//    transform.setRotation( tf::Quaternion(-0.68407, -0.22465, -0.662427, 0.2068019) );
//
 //   transform.setOrigin( tf::Vector3(-0.0385339, -0.09149263, -0.04490688) );
  //  transform.setRotation( tf::Quaternion(0.91223, -0.0009196, -0.00476681, 0.4096450) );
  //  br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "ee_link", "camera"));