# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/jire/clion-2019.3.3/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/jire/clion-2019.3.3/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jire/clion-project/libMultiRobotPlanning

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jire/clion-project/libMultiRobotPlanning/cmake-build-debug

# Utility rule file for clang-format.

# Include the progress variables for this target.
include CMakeFiles/clang-format.dir/progress.make

CMakeFiles/clang-format:
	clang-format -i /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/a_star.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/a_star_epsilon.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/assignment.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/cbs.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/cbs_ta.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/ecbs.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/ecbs_ta.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/neighbor.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/next_best_assignment.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/planresult.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/sipp.hpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/online_testcase.hpp /home/jire/clion-project/libMultiRobotPlanning/example/online_testcase.cpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/hie_mapf.hpp /home/jire/clion-project/libMultiRobotPlanning/example/hie_mapf.cpp /home/jire/clion-project/libMultiRobotPlanning/example/cbs_ol.cpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/cbs_ol.hpp /home/jire/clion-project/libMultiRobotPlanning/example/a_star.cpp /home/jire/clion-project/libMultiRobotPlanning/example/a_star_epsilon.cpp /home/jire/clion-project/libMultiRobotPlanning/example/assignment.cpp /home/jire/clion-project/libMultiRobotPlanning/example/cbs.cpp /home/jire/clion-project/libMultiRobotPlanning/example/cbs_ta.cpp /home/jire/clion-project/libMultiRobotPlanning/example/ecbs.cpp /home/jire/clion-project/libMultiRobotPlanning/example/ecbs_ta.cpp /home/jire/clion-project/libMultiRobotPlanning/example/mapf_prioritized_sipp.cpp /home/jire/clion-project/libMultiRobotPlanning/example/next_best_assignment.cpp /home/jire/clion-project/libMultiRobotPlanning/example/shortest_path_heuristic.cpp /home/jire/clion-project/libMultiRobotPlanning/example/shortest_path_heuristic.hpp /home/jire/clion-project/libMultiRobotPlanning/example/sipp.cpp /home/jire/clion-project/libMultiRobotPlanning/example/timer.hpp /home/jire/clion-project/libMultiRobotPlanning/example/a_star_seq.cpp /home/jire/clion-project/libMultiRobotPlanning/example/hie_mapf_barebone.cpp /home/jire/clion-project/libMultiRobotPlanning/include/libMultiRobotPlanning/hie_mapf_barebone.hpp

clang-format: CMakeFiles/clang-format
clang-format: CMakeFiles/clang-format.dir/build.make

.PHONY : clang-format

# Rule to build all files generated by this target.
CMakeFiles/clang-format.dir/build: clang-format

.PHONY : CMakeFiles/clang-format.dir/build

CMakeFiles/clang-format.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/clang-format.dir/cmake_clean.cmake
.PHONY : CMakeFiles/clang-format.dir/clean

CMakeFiles/clang-format.dir/depend:
	cd /home/jire/clion-project/libMultiRobotPlanning/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jire/clion-project/libMultiRobotPlanning /home/jire/clion-project/libMultiRobotPlanning /home/jire/clion-project/libMultiRobotPlanning/cmake-build-debug /home/jire/clion-project/libMultiRobotPlanning/cmake-build-debug /home/jire/clion-project/libMultiRobotPlanning/cmake-build-debug/CMakeFiles/clang-format.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/clang-format.dir/depend

