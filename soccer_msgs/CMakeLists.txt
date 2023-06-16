cmake_minimum_required(VERSION 3.0)
project(soccer_msgs)


find_package(catkin REQUIRED COMPONENTS roscpp std_msgs geometry_msgs message_generation)

add_message_files(
	FILES
	ball_output.msg
	path_output.msg
	field_output.msg
	goal_output.msg
	line_output.msg
	obstacle_output.msg
	vision_outputs.msg
	localization_output.msg
	localization_input.msg
	dilemma.msg
	deep_output.msg
)
 
generate_messages(
	DEPENDENCIES std_msgs geometry_msgs
)

catkin_package(
   CATKIN_DEPENDS message_runtime std_msgs geometry_msgs
)

