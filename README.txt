How to compile and run the code

run on ubuntu 14.05.5 LTS
	ros-indigo

open 3 terminals
	terminal 1: add src folder, CMakeLists.txt, and package.xml to a ~/catkin_ws/src directory
			run catkin_make
			run roscore

	terminal 2: run rosrun turtlesim turtlesim_node
	terminal 3: run source ~/catkin_ws/devel.setup.bash
			rosrun mines_le_vinh robot_draw_node

view on the turtlesim_node

OR (repeat instructions with commands)

Assuming that you have git and ros-indigo installed with a catkin workspace

Open 3 Terminals:

	Commands to run on Terminal 1: 	cd ~/catkin_ws/src
					git clone https://github.com/vle1054/mines_le_vinh1
					cd ..
					catkin_make
					roscore

Continue after finishing commands on Terminal 1...

	Commands to run on Terminal 2:	rosrun turtlesim turtlesim_node
	Commands to run on Terminal 3: 	source ~/catkin_ws/devel/setup.bash
					rosrun mines_le_vinh robot_draw_node