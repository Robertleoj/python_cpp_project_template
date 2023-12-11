cmake_minimum_required(VERSION 3.22)
project(project)
set(CMAKE_CXX_STANDARD 20)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# if you add anything into external
# add_subdirectory(external/module)

add_subdirectory(src)
